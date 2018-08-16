
# coding: utf-8

# # Linear Regression

# In[1]:


import warnings
warnings.filterwarnings("ignore")


# In[2]:


import tensorflow as tf
import numpy
import pandas as pd  
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


learning_rate = 0.01
training_epochs = 1000
display_step = 50


# In[ ]:


## Load Data


# In[4]:


path = 'data/2-data.txt'  
data = pd.read_csv(path, header=None, names=['X', 'Y']) 
print (data.head(5))
print (data.describe())


# In[5]:


# Training Data
x_train = data['X'].tolist()
y_train = data['Y'].tolist()


# In[6]:


#x_train = [2,3,4,5,6]
#y_train = [3,6,7,10,12]
n_samples = len(x_train)


# In[7]:


plt.plot(x_train, y_train, 'b.', label='data')


# In[11]:


# Model parameters
W = tf.Variable([.1], dtype=tf.float32)
b = tf.Variable([.1], dtype=tf.float32)

# Model input and output
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
linear_model = tf.add(tf.multiply(x, W), b)

# Loss
loss = tf.reduce_sum(tf.square(linear_model-y))/(2*n_samples) # sum of the squares

# optimizer
optimizer = tf.train.GradientDescentOptimizer(0.1)
train = optimizer.minimize(loss)

# Initialize the variables (i.e. assign their default value)
init = tf.global_variables_initializer()

# For saving the model
saver = tf.train.Saver()


# ## Training and Saving a Model

# In[12]:


# Training loop
sess = tf.Session()
sess.run(init) # reset values to wrong
for epoch in range(training_epochs):
    for (x_, y_) in zip(x_train, y_train):
        sess.run([train], {x: x_, y: y_})
    print ("epoch=", epoch, sess.run([W, b], {x: x_, y: y_}))
# Evaluate training accuracy
curr_W, curr_b, curr_loss = sess.run([W, b, loss], {x: x_train, y: y_train})
# Saving the model
saver.save(sess,'saved_models/my_linear_model.ckpt')
print("W: %s b: %s loss: %s"%(curr_W, curr_b, curr_loss))


# In[13]:


# Prediction example
Prediction_X = numpy.asarray([10.5, 24.2])    


# In[14]:


# Graphic display
plt.plot(x_train, y_train, 'b.', label='Testing data')
plt.plot(x_train, x_train*curr_W+curr_b, 'y-', label='Fitted line')
plt.plot(Prediction_X, Prediction_X*curr_W+curr_b, 'ro', label='Prediction')
plt.legend()
plt.show()


# ## Loading a Model

# In[15]:


with tf.Session() as sess:
    # Restore the model
    saver.restore(sess,'saved_models/my_linear_model.ckpt')
    # Fetch Back Results
    restored_W , restored_b = sess.run([W,b])


# In[16]:


# Graphic display (Using restored weight and bias)
plt.plot(x_train, y_train, 'b.', label='Testing data')
plt.plot(x_train, x_train*curr_W+curr_b, 'y-', label='Fitted line')
plt.plot(Prediction_X, Prediction_X*restored_W+restored_b, 'ro', label='Prediction')
plt.legend()
plt.show()

