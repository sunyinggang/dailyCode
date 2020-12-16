import tensorflow as tf
import numpy as np
from collections import namedtuple
import math

from Model import AlexNet
from Dataset import Dataset

# The definition of fed model
# namedtuple创建一个和tuple类似的对象，而且对象拥有可访问的属性
# X: 输入
# Y: 输出
# DROP_RATE: 下降率
# train_op: tf计算图中的训练节点（一般是optimizer.minimize(xxx)）
# loss_op: 亏损操作
# acc_op:
FedModel = namedtuple('FedModel', 'X Y DROP_RATE train_op loss_op acc_op')

class Clients:
    def __init__(self, input_shape, num_classes, learning_rate, clients_num):
        self.graph = tf.Graph()
        self.sess = tf.Session(graph=self.graph)

        # `net` 是一个list，依次包含模型中FedModel需要的计算节点（看上面）
        net = AlexNet(input_shape, num_classes, learning_rate, self.graph)
        self.model = FedModel(*net)

        # initialize
        with self.graph.as_default():
            self.sess.run(tf.global_variables_initializer())

        # 加载数据集
        self.dataset = Dataset(tf.keras.datasets.cifar10.load_data,
                        split=clients_num)

    def run_test(self, num):
        with self.graph.as_default():
            batch_x, batch_y = self.dataset.test.next_batch(num)
            feed_dict = {
                self.model.X: batch_x,
                self.model.Y: batch_y,
                self.model.DROP_RATE: 0
            }
        return self.sess.run([self.model.acc_op, self.model.loss_op],
                             feed_dict=feed_dict)

    def train_epoch(self, cid, batch_size=32, dropout_rate=0.5):
        """
            Train one client with its own data for one epoch
            cid: Client id
        """
        dataset = self.dataset.train[cid]

        with self.graph.as_default():
            for _ in range(math.ceil(dataset.size // batch_size)):
                batch_x, batch_y = dataset.next_batch(batch_size)
                feed_dict = {
                    self.model.X: batch_x,
                    self.model.Y: batch_y,
                    self.model.DROP_RATE: dropout_rate
                }
                self.sess.run(self.model.train_op, feed_dict=feed_dict)

    def get_client_vars(self):
        """ Return all of the variables list """
        with self.graph.as_default():
            tt = tf.trainable_variables()
            print(tt)
            client_vars = self.sess.run(tf.trainable_variables())
        return client_vars

    def set_global_vars(self, global_vars):
        """ Assign all of the variables with global vars """
        with self.graph.as_default():
            all_vars = tf.trainable_variables()
            for variable, value in zip(all_vars, global_vars):
                variable.load(value, self.sess)

    def choose_clients(self, ratio=1.0):
        """ randomly choose some clients """
        client_num = self.get_clients_num()
        choose_num = math.floor(client_num * ratio)
        # np.random.permutation()对原来的数组进行重新洗牌
        return np.random.permutation(client_num)[:choose_num]

    def get_clients_num(self):
        return len(self.dataset.train)