import tensorflow as tf

class Autoencoder(object):
    def __init__(self, n_input, n_hidden1,n_hidden2,n_hidden3, transfer_function=tf.nn.softplus, optimizer = tf.train.AdamOptimizer()):
        self.n_input = n_input
        self.n_hidden1 = n_hidden1
        self.n_hidden2 = n_hidden2
        self.n_hidden3 = n_hidden3
        self.transfer = transfer_function

        network_weights = self._initialize_weights()
        self.weights = network_weights

        # model
        self.x = tf.placeholder(tf.float32, [None, self.n_input])
        self.hidden1 = self.transfer(tf.add(tf.matmul(self.x, self.weights['w1']), self.weights['b1']))
        self.hidden2 = self.transfer(tf.add(tf.matmul(self.hidden1, self.weights['w2']), self.weights['b2']))
        self.hidden3 = self.transfer(tf.add(tf.matmul(self.hidden2, self.weights['w3']), self.weights['b3']))
        self.reconstruction = tf.add(tf.matmul(self.hidden3, self.weights['w4']), self.weights['b4'])

        # cost
        self.cost = 0.5 * tf.reduce_sum(tf.pow(tf.subtract(self.reconstruction, self.x), 2.0))
        self.optimizer = optimizer.minimize(self.cost)

        init = tf.global_variables_initializer()
        self.sess = tf.Session()
        self.sess.run(init)


    def _initialize_weights(self):
        all_weights = dict()
        all_weights['w1'] = tf.get_variable("w1", shape=[self.n_input, self.n_hidden1],
            initializer=tf.contrib.layers.xavier_initializer())
        all_weights['b1'] = tf.Variable(tf.zeros([self.n_hidden1], dtype=tf.float32))
        all_weights['w2'] = tf.get_variable("w2", shape=[self.n_hidden1, self.n_hidden2],
            initializer=tf.contrib.layers.xavier_initializer())
        all_weights['b2'] = tf.Variable(tf.zeros([self.n_hidden2], dtype=tf.float32))
        all_weights['w3'] = tf.get_variable("w3", shape=[self.n_hidden2, self.n_hidden3],
            initializer=tf.contrib.layers.xavier_initializer())
        all_weights['b3'] = tf.Variable(tf.zeros([self.n_hidden3], dtype=tf.float32))
        all_weights['w4'] = tf.Variable(tf.zeros([self.n_hidden3, self.n_input], dtype=tf.float32))
        all_weights['b4'] = tf.Variable(tf.zeros([self.n_input], dtype=tf.float32))
        return all_weights

    def partial_fit(self, X):
        cost, opt = self.sess.run((self.cost, self.optimizer), feed_dict={self.x: X})
        return cost

    def calc_total_cost(self, X):
        return self.sess.run(self.cost, feed_dict = {self.x: X})

    def transform(self, X):
        return self.sess.run(self.hidden3, feed_dict={self.x: X})

    def generate(self, hidden = None):
        if hidden is None:
            hidden = self.sess.run(tf.random_normal([1, self.n_hidden]))
        return self.sess.run(self.reconstruction, feed_dict={self.hidden: hidden})

    def reconstruct(self, X):
        return self.sess.run(self.reconstruction, feed_dict={self.x: X})

    def getWeights(self):
        return self.sess.run(self.weights['w1'],self.weights['w2'],self.weights['w3'],self.weights['w4'],self.weights['w5'],self.weights['w6'])

    def getBiases(self):
        return self.sess.run(self.weights['b1'],self.weights['b2'],self.weights['b3'],self.weights['b4'],self.weights['b5'],self.weights['b6'])

