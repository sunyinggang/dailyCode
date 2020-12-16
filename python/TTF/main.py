import numpy as np
import tensorflow as tf
import tensorflow_federated as tff
from matplotlib import pyplot as plt


emnist_train, emnist_test = tff.simulation.datasets.emnist.load_data()

example_dataset = emnist_train.create_tf_dataset_for_client(
    emnist_train.client_ids[0])
#
# example_element = next(iter(example_dataset))
#
# example_element['label'].numpy()
#
# plt.imshow(example_element['pixels'].numpy(), cmap='gray', aspect='equal')
# plt.grid(False)
# _ = plt.show()

figure = plt.figure(figsize=(20, 4))
j = 0

for example in example_dataset.take(40):
  plt.subplot(4, 10, j+1)
  plt.imshow(example['pixels'].numpy(), cmap='gray', aspect='equal')
  plt.axis('off')
  j += 1

_ = plt.show()