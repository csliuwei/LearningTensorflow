import tensorflow as tf

a = tf.constant(10)
b = tf.constant(20)

c = a + b

sess = tf.Session()

print(sess.run(c))
