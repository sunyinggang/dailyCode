import tensorflow as tf
from tqdm import tqdm

from Client import Clients

def buildClients(num):
    learning_rate = 0.0001
    num_input = 32  # image shape: 32*32
    num_input_channel = 3  # image channel: 3
    num_classes = 10  # Cifar-10 total classes (0-9 digits)

    #create Client and model
    return Clients(input_shape=[None, num_input, num_input, num_input_channel],
                  num_classes=num_classes,
                  learning_rate=learning_rate,
                  clients_num=num)


def run_global_test(client, global_vars, test_num):
    client.set_global_vars(global_vars)
    acc, loss = client.run_test(test_num)
    print("[epoch {}, {} inst] Testing ACC: {:.4f}, Loss: {:.4f}".format(
        ep + 1, test_num, acc, loss))


#### SOME TRAINING PARAMS ####
# Clients的模型数量
CLIENT_NUMBER = 100
# 每轮挑选clients跑跑看的比例
CLIENT_RATIO_PER_ROUND = 0.12
# epoch上限
epoch = 360


#### CREATE CLIENT AND LOAD DATASET ####
# 创建客户端并加载数据集
client = buildClients(CLIENT_NUMBER)

#### BEGIN TRAINING ####
# 开始训练
global_vars = client.get_client_vars()
print(global_vars)
for ep in range(epoch):
    # 用来收集Clients端的参数，全部叠加起来（节约内存）
    client_vars_sum = None

    # 随机挑选一些Clients进行训练
    random_clients = client.choose_clients(CLIENT_RATIO_PER_ROUND)

    # 用这些Clients进行训练，收集它们更新后的模型
    for client_id in tqdm(random_clients, ascii=True):
        # 将Server端的模型加载到Client模型上
        client.set_global_vars(global_vars)

        # 训练这个下标的Client
        client.train_epoch(cid=client_id)

        # 获取当前Client的模型变量值
        current_client_vars = client.get_client_vars()

        # 把各个层的参数叠加起来
        if client_vars_sum is None:
            client_vars_sum = current_client_vars
        else:
            for cv, ccv in zip(client_vars_sum, current_client_vars):
                cv += ccv

    # 把叠加后的Client端模型变量 除以 本轮参与训练的Clients数量
    # 得到平均模型、作为新一轮的Server端模型参数
    global_vars = []
    for var in client_vars_sum:
        global_vars.append(var / len(random_clients))

    # 跑一下测试集、输出一下
    run_global_test(client, global_vars, test_num=600)


#### FINAL TEST ####
run_global_test(client, global_vars, test_num=10000)