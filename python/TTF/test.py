import tensorflow as tf
import numpy as np


def add_layer(inputs, in_size, out_size, activation_function=None):
    # tf.random_normal() 函数用于从“服从指定正态分布的序列”中随机取出指定个数的值。
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1,out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

x_data = np.linspace(-1,1,300)[:,np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5

l1 = add_layer()