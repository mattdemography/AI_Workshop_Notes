
# coding: utf-8

# # Linear Algebra Review
# Python is a great programming language and with the help of a few popular libraries such numpy and matplotlib it becomes a powerful environment for Linear Algebra computing.
# 
# Numpy Documentation - This brief overview has touched on many of the important things that you need to know about numpy, but is far from complete. Check out the [numpy reference](http://docs.scipy.org/doc/numpy/reference/) to find out much more about numpy.
# 
# ##### 1) Matrices and Vectors 
# Rectangulare array of numbers
# <img src="image/matrix.png">
# 
# ## Numpy Array 

# In[11]:


import numpy as np


# ##### 1) Matrices and Vectors 
# A numpy array is a grid of values, all of the same type, and is indexed by a tuple of nonnegative integers.

# In[12]:


# Create a rank 1 array
a = np.array(
    [
        [1,2,3,4],
        [1,4,5,6],
        [1,2,3,4]
    ]
)  
print (a)
print (type(a))            
print (a.shape)


# ##### 1.1) Change an element of the array 

# In[13]:


a = np.array(
    [
        [1,2,3,4],
        [1,4,5,6],
        [1,2,3,4]
    ])
print (a)
a[0,0] = 100
print ()
print (a)


# ##### 1.2) Numpy functions

# <font color="red"> **Datatypes**

# In[14]:


a = np.array(
    [
        [1,2,3,4],
        [1,4,5,6],
        [1,2,3,4]
    ]
)
print (a)
print (type(a[0,0]))
print ()
a = np.array(
    [
        [1.2,2,3,4],
        [1,4,5,6],
        [1,2,3,4]
    ]
)  
print (a)
print (type(a[0,0]))


# <font color="red"> **Compute sum of all elements in matrix**

# In[15]:


x = np.array([
        [1,2,1],[3,4,1]])

print (x)
print (np.sum(x))  
print (np.sum(x, axis=0))  
print (np.sum(x, axis=1))  


# <font color="red"> **Create an array of all zeros**

# In[16]:


a = np.zeros((4,4))  
a


# <font color="red"> **Create an array of all ones ** 

# In[17]:


a = np.ones((2,5))   
a             


# <font color="red"> **Create a constant array**

# In[18]:


a = np.full((4,4), 7)  
a               


# <font color="red"> **Create an identity matrix**

# In[19]:


a = np.eye(4)       
a            


# <font color="red"> **Create an array filled with random values**

# In[20]:


a = np.random.random((5,5)) 
a                    


# <font color="red"> **slicing to pull out the subarray**

# In[21]:


a = np.array(
    [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
    ])
print (a)
print ()
b = a[:1, :3]
print (b)


# ##### 2) Matrix Addition
# <img src="image/matrix-sum.png">

# In[22]:


x = np.ones((4,7))
print (x)
y = np.full((4,7), 4.3)
print (y)
z = x+y
print ()
print (z)


# In[30]:


x = np.array(
    [
        [1.2,2,3,4],
        [1,4,5,6],
        [1,2,3,4]
    ])
print (x)
y = np.array(
    [
        [1,2,3,4],
        [1,4,5,6],
        [1,2,3,4]
    ])
print (y)
print ()
z = np.add(x, y)
print (z)


# ##### 2) Matrix Subtraction  
# <img src="image/matrix-sub.png">

# In[24]:


z = x - y
print (z)
print ()
z = np.subtract(x, y)
print (z)


# ##### 3) Matrix Vector Multiplication
# <img src="image/matrix-vector.png">

# In[25]:


x = np.array(
    [
        [1,0,-1],
        [1,2,-1],
        [1,0,-1],
        [1,0,-1]
    ])
print (x)
y = np.array([1,1,2])
print (y)
z = np.dot(x, y)
print (z)


# ##### 3.1) Matrix Multiplication
# <img src="image/matrix-dot.png">

# In[26]:


x = np.array(
    [
        [1,2,3],
        [4,5,6]
    ])
print (x)
y = np.array(
    [
        [7,8],
        [9,10],
        [11,12]
    ])
print (y)
print ()
z = np.dot(x, y)
print (z)
print ()
z = np.dot(y, x)
print (z)


# ##### 4) Matrix Transpose
# <img src="image/matrix-transpose.png">
# 

# In[27]:


x = np.array([[0,1,2,0], [0,3,4,5]])
print (x) 
print ()
print (x.T) 


# <font color="red"> **Note that taking the transpose of a rank 1 array does nothing**

# In[28]:


x = np.array([0,1,2,3])
print (x)
print (x.shape)
y = x.T
print (y.shape) 


# <font color="red"> **Create an empty matrix with the same shape as x**    

# In[29]:


x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
print (x)
print ()
v = np.array([1, 5, 1])
y = np.empty_like(x)   

for i in range(4):
    y[i, :] = x[i, :] + v

print (y)

