import tensorflow as tf

import os

# setting for optimization
learning_rate = 0.001
decay = 0.9
training_epochs = 10
batch_size= 100
p_keep_conv_value = 0.8
p_keep_hidden_value = 0.5

# set variabels
X = tf.placeholder(tf.float32,[None,28,28,1])
Y = tf.placeholder(tf.float32,[None,10])

p_keep_conv = tf.placeholder(tf.float32)
p_keep_hidden = tf.placeholder(tf.float32)

print('Preparing MNIST data ...')

from tensorflow.examples.tutorials.mnist import input_data
script_dir = os.path.dirname(os.path.abspath(__file__))
mnist = input_data.read_data_sets(script_dir + "/../mnist/data/", one_hot=True)

print("building CNN models")

W1 = tf.Variable(tf.random_normal([3,3,1,32], stddev=0.01))
