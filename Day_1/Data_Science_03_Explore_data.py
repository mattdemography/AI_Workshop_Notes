
# coding: utf-8

# In[1]:


get_ipython().system('pip install --user seaborn')


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


df = pd.read_csv("clean_df.csv")


# In[8]:


print(df.head())
df.dtypes


# ## Visualization

# In[13]:


df.dtypes


# calculate the correlation between variables  of type "int64" or "float64" using the method "corr"

# In[9]:


df.corr()


# ## Question  #1: 
# <li>Find the correlation : bore, stroke, compression-ratio, and horsepower.
# <li>Hint: if you would like to select those columns  use the following syntax: <li>df[['bore','stroke' ,'compression-ratio','horsepower']]

# ## Visualization

# scatterplot of "engine-size" and "price"

# In[19]:


# Engine size as potential predictor variable of price
sns.regplot(x="engine-size", y="price", data=df)
plt.ylim(0,)


# As the engine-size goes up, the price goes up

# In[13]:


df[["engine-size", "price"]].corr()


# correlation between 'engine-size' and 'price' is approximately  0.87

# In[20]:


sns.regplot(x="highway-mpg", y="price", data=df)


# As the highway-mpg goes up, the price goes down

# 
# We can examine the correlation between 'highway-mpg' and 'price' and see it's approximately  -0.704:

# In[21]:


df[['highway-mpg', 'price']].corr()


# ### Weak Linear Relationship

# In[22]:


sns.regplot(x="peak-rpm", y="price", data=df)


# In[23]:


df[['peak-rpm','price']].corr()


# ## Question  3
# <li>Find the correlation  between x="stroke", y="price". Describe the correlation 

# In[25]:


print(sns.regplot(x="stroke", y="price", data=df))
df[['stroke','price']].corr()


# ## Boxplots

# In[29]:


df["body-style"].value_counts()


# In[30]:


sns.boxplot(x="body-style", y="price", data=df)


# In[31]:


sns.boxplot(x="engine-location", y="price", data=df)


# In[43]:


sns.boxplot(x="drive-wheels", y="price", data=df)


# ## 3. Descriptive Statistical Analysis

# In[48]:


df.describe()


# In[47]:


df[['price']].describe()


# In[ ]:


df.describe()


# In[49]:


df.describe(include=['object'])


# ### Value Counts

# In[50]:


df['drive-wheels'].value_counts()


# Present as Dataframe :

# In[52]:


df['drive-wheels'].value_counts().to_frame()


# In[53]:


drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()
drive_wheels_counts.rename(columns={'drive-wheels': 'value_counts'}, inplace=True)
drive_wheels_counts


# In[54]:


drive_wheels_counts.index.name = 'drive-wheels'
drive_wheels_counts


# In[55]:


engine_loc_counts = df['engine-location'].value_counts().to_frame()
engine_loc_counts.rename(columns={'engine-location': 'value_counts'}, inplace=True)
engine_loc_counts.index.name = 'engine-location'
engine_loc_counts.head(10)


# ## Grouping

# In[58]:


df['drive-wheels'].value_counts().to_frame()


# In[59]:


df['drive-wheels'].unique()


# In[62]:


df[['drive-wheels','body-style','price']]


# In[63]:


df_group_one=df_group_one.groupby(['drive-wheels'],as_index= False).mean()
df_group_one


# In[64]:


df_group_one=df_group_one.groupby(['drive-wheels']).mean()
df_group_one


# In[65]:


df_gptest=df[['drive-wheels','body-style','price']]
grouped_test1=df_gptest.groupby(['drive-wheels','body-style'],as_index= False).mean()
grouped_test1

