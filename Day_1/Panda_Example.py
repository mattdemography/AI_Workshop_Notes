
# coding: utf-8

# In[8]:


import pandas as pd
#df.head() - five rows
#df.dtypes - check data type
#df.describe() - statistically summarize data
#df.describe(include="all") - Full summary statistics
#df["var_name"] - Access a column

path="https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df2 = pd.read_csv(path, header=None)
df2.head()


# In[9]:


headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
df2.columns = headers
df2.head()


# In[12]:


df2.dtypes


# In[13]:


df2.describe()


# In[63]:


path2="https://people.sc.fsu.edu/~jburkardt/data/csv/homes.csv"
df3 = pd.read_csv(path2, header=None)
df3=df3.rename(columns=df3.iloc[0]) #Renames first row to column names
df3=df3.drop(df.index[0]) #Remove the row that contained the column names
#df3.columns = headers[2]


# In[64]:


df3.head()


# In[37]:


df3.tail(10)

