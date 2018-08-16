
# coding: utf-8

# # Image Manipulation using Numpy and Scipy

# ## Import required packages

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy import misc
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Import a test image

# In[ ]:


face_img = misc.face()
plt.imshow(face_img[:,:,:])


# ## Show the different color channels

# In[ ]:


fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(15,5))

for c, ax in zip(range(3), axs):
    tmp_im = np.zeros(face_img.shape, dtype="uint8")
    tmp_im[:,:,c] = face_img[:,:,c]
    ax.imshow(tmp_im)
    ax.set_axis_off()


# ## Show R Channel in Gray Scale

# In[ ]:


r_channel = face_img[:,:,1]

# Plot the r_channel variable
plt.imshow(r_channel, cmap='gray')


# ## Define the kernels

# In[ ]:


kernel1 = np.array([[ -1, -2, -1],
                    [  0,  0,  0],
                    [  1,  2,  1]])

kernel2 = np.array([[ -1, 0, 1],
                    [ -2, 0, 2],
                    [ -1, 0, 1]])


# ## Find convolved gradients 

# In[ ]:


grad1 = signal.convolve2d(face_img[:,:,1], kernel1, boundary='symm', mode='same')
grad2 = signal.convolve2d(face_img[:,:,1], kernel2, boundary='symm', mode='same')


# ## Plot the results

# In[ ]:


fig, (ax_orig, ax_mag1, ax_mag2) = plt.subplots(1, 3, figsize=(21, 21))
ax_orig.imshow(face_img[:,:,0], cmap='gray')
ax_orig.set_title('Original')
ax_orig.set_axis_off()
ax_mag1.imshow(grad1, cmap='gray')
ax_mag1.set_title('Convolution using Gradient 1')
ax_mag1.set_axis_off()
ax_mag2.imshow(grad2, cmap='gray')
ax_mag2.set_title('Convolution using Gradient 2')
ax_mag2.set_axis_off()


# ## Save an image

# In[ ]:


misc.imsave('grad1.png', grad1)


# ## Let's play with the kernels

# In[ ]:


kernel1 = np.array( ... )

kernel2 = np.array( ... )

grad1 = signal.convolve2d(face_img[:,:,1], kernel1, boundary='symm', mode='same')
grad2 = signal.convolve2d(face_img[:,:,1], kernel2, boundary='symm', mode='same')

fig, (ax_orig, ax_mag1, ax_mag2) = plt.subplots(1, 3, figsize=(21, 21))
ax_orig.imshow(face_img[:,:,0], cmap='gray')
ax_orig.set_title('Original')
ax_orig.set_axis_off()
ax_mag1.imshow(grad1, cmap='gray')
ax_mag1.set_title('Convolution using Gradient 1')
ax_mag1.set_axis_off()
ax_mag2.imshow(grad2, cmap='gray')
ax_mag2.set_title('Convolution using Gradient 2')
ax_mag2.set_axis_off()

