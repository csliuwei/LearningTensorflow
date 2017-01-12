import tensorflow as tf

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

c =  a + b
d = tf.mul(a,b)

with tf.Session() as sess:
    print(sess.run(c, feed_dict={a:20,b:4}))
    print(sess.run(d,feed_dict={a:10,b:5}))
