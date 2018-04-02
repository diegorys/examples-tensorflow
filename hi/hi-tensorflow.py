import tensorflow as tf

first = tf.placeholder("float")
second = tf.placeholder("float")

y_sum = tf.add(first, second)
y_mul = tf.mul(first, second)

sess = tf.Session()

print sess.run(y_sum, feed_dict={first: 2, second: 3})
print sess.run(y_mul, feed_dict={first: 2, second: 3})