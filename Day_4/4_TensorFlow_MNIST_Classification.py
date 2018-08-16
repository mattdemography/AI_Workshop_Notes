
# coding: utf-8

# # MNIST Hand Written Digit Recognition

# # Import Required Packages

# In[1]:


## Suppress useless warnings
import warnings
warnings.filterwarnings('ignore')


# In[2]:


import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt
from pylab import *
old_v = tf.logging.get_verbosity()
tf.logging.set_verbosity(tf.logging.ERROR)
tf.logging.set_verbosity(old_v)
get_ipython().run_line_magic('matplotlib', 'inline')


# # Define the Hyper Parameters

# In[3]:


learning_rate = 0.1 #Define learning rate - https://users.ics.aalto.fi/jhollmen/dippa/node22.html
display_step = 50
epochs = 500


# # Input Data

# In[4]:


mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# Load data
X_train = mnist.train.images
Y_train = mnist.train.labels
X_test = mnist.test.images
Y_test = mnist.test.labels

print ("\nShape of Train Image Data: ", X_train.shape)
print ("Shape of Train Label Data: ", Y_train.shape)
print ("Shape of Test Image Data: ", X_test.shape)
print ("Shape of Test Label Data: ", Y_test.shape)


# # Plot some images in MNIST

# In[5]:


fig, ax = plt.subplots(6, 6, figsize = (12, 12))
fig.suptitle('First 36 images in MNIST')
fig.tight_layout(pad = 0.3, rect = [0, 0, 0.9, 0.9])
for x, y in [(i, j) for i in range(6) for j in range(6)]:
    ax[x, y].imshow(X_train[x + y * 6].reshape((28, 28)), cmap = 'gray')
    title = str(np.where(Y_train[x + y * 6]==1)[0])
    ax[x, y].set_title(title)


# In[6]:


# Input pixels, flattened
x = tf.placeholder("float", [None, 784])
# Known labels
y_ = tf.placeholder("float", [None,10])

# Variables
w1 = tf.Variable(tf.zeros([784,20])) #This is the connectivity of nodes? 7,840 variables + b to learn
w12= tf.Variable(tf.zeros([20,10]))
b1 = tf.Variable(tf.zeros([20])) #Exactly 10 variables
b = tf.Variable(tf.zeros([10])) #Exactly 10 variables

# Define model
y1 = tf.nn.softmax(tf.matmul(x,w1) + b1)
y = tf.nn.softmax(tf.matmul(y1,w12) + b)

# Climb on cross-entropy

cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1])) #Use cross entropy if classification mean square if regression

optimizer = tf.train.GradientDescentOptimizer(learning_rate)
train_step = optimizer.minimize(cross_entropy)

# Just initialize
init = tf.global_variables_initializer()


# In[7]:


sess = tf.Session()
sess.run(init) # reset values to wrong
# Define accuracy
correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

# Actually train
train_acc = np.zeros(epochs//10)
test_acc = np.zeros(epochs//10)

for i in range(epochs):
    # Record summary data, and the accuracy
    print ("Epoch: ", i, ", Loss: ", sess.run(cross_entropy, {x: X_train.reshape([-1,784]), y_: Y_train}))
    sess.run([train_step,cross_entropy] , {x: X_train.reshape([-1,784]), y_: Y_train})

    if i % 10 == 0:
        # Check accuracy on train set
        A = sess.run (accuracy, {x: X_train.reshape([-1,784]),y_: Y_train})
        train_acc[i//10] = A
        # And now the test set
        A = sess.run (accuracy, {x: X_test.reshape([-1,784]), y_: Y_test})
        #print (A)
        test_acc[i//10] = A

curr_W, curr_b, curr_cross_entropy = sess.run([W, b, cross_entropy], {x: X_train.reshape([-1,784]), y_: Y_train})
print("Training Done...!!")


# In[8]:


curr_W, curr_b, curr_cross_entropy = sess.run([W, b, cross_entropy], {x: X_train.reshape([-1,784]), y_: Y_train})


# # Accuracy Plots

# In[9]:


# Plot the accuracy curves
plt.plot(train_acc,'bo')
plt.plot(test_acc,'rx')
# Notice that accuracy flattens out
print("Training Accuracy", train_acc[-1])
print("Testing Accuracy", test_acc[-1])
#The training set fits to 90% accuracy of the digits


# In[10]:


# Look at a subplot of the weights for each font
f, plts = plt.subplots(10, sharex=True, figsize=(3,30))

for i in range(10):
    plts[i].pcolor(curr_W[:,i].reshape([28,28]), cmap=plt.cm.gray_r)

