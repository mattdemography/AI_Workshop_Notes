
# coding: utf-8

# In[1]:


# import pandas library
import pandas as pd


# In[2]:


path="https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df = pd.read_csv(path, header=None)


# In[5]:


df.head()


# In[7]:


headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
df.columns = headers


# In[11]:


df.head()


# In[7]:


df.dtypes


# In[8]:


df.describe()


# In[12]:


df


# <div class="alert alert-danger alertdanger" style="margin-top: 10px">
# <h3> Question #1: </h3>
# <b><li> from https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html <b> 
# <b><li> read "homes.csv" file <b> 
# <b><li> Check the bottom 10 rows of data frame "df":</b>
# </div>

# In[19]:


# Question 1


# In[ ]:


df.to_csv("homes.csv")

