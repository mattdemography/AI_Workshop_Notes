
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


filename = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'


# In[3]:


headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]


# In[4]:


df = pd.read_csv(filename, names = headers)


# In[6]:


df.dtypes
df.head()


# # Dealing with missing data:
# replace "?" to NaN

# In[7]:


df.replace("?", np.nan, inplace = True)
df.head(10)


# In[25]:


df.describe()
df2=df[['price', 'bore', 'stroke']]


# In[13]:


missing_data = df.isnull()  #Takes all missings and give 'True' value.
missing_data.head(5)


# "True" stands for missing value, while "False" stands for not missing value.

# In[14]:


missing_data["normalized-losses"].value_counts()


# In[15]:


missing_data.columns.values.tolist()


# ### Count missing values in each column

# In[16]:


for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")    


# <a id="ref3"></a>
# ## Deal with missing data
# **How to deal with missing data:**
# 
# 1. Drop data
# 2. Replace data

# #### Calculate the average of the column:

# In[17]:


avg = df["normalized-losses"].astype("float").mean(axis =0)
print(avg)


# #### Replace "NaN" by mean value in "normalized-losses" column:

# In[18]:


df["normalized-losses"].replace(np.nan, avg, inplace = True)


# #### Calculate the mean value for 'bore' column:

# In[19]:


avg=df['bore'].astype('float').mean(axis=0)
print(avg)


# #### Replace NaN by mean value:

# In[20]:


df['bore'].replace(np.nan, avg, inplace= True)


# ## Question  #1: 
# 
# According to the example above, replace NaN in "stroke" column by mean:

# In[41]:


print(df[['price', 'bore', 'stroke']].describe())
print(df.dtypes)
df2['price']=df2['price'].astype('float')
df2['bore']=df2['bore'].astype('float')
df2['stroke']=df2['stroke'].astype('float')
print(df2.dtypes)


# In[44]:


avg_stroke=df2['stroke'].astype('float').mean(axis=0)
print(avg_stroke)
print(df[['price', 'stroke', 'bore']].describe())
df2['stroke'].replace(np.nan, avg_stroke, inplace=True)
df2.describe()


# avg = df["stroke"].astype("float").mean(axis = 0)
# df["stroke"].replace(np.nan, avg, inplace = True)

# #### Calculate the mean value for the  'horsepower' column:

# In[45]:


avg=df['horsepower'].astype('float').mean(axis=0)
print(avg)


# #### Replace "NaN" by mean value :

# In[46]:


df['horsepower'].replace(np.nan, avg, inplace= True)


# In[47]:


avg_5=df['peak-rpm'].astype('float').mean(axis=0)


# ### To see which values are present in a particular column, use the ".value_counts()":

# In[48]:


df['num-of-doors'].value_counts()


# ### The most common value, use the ".idxmax()"

# In[49]:


df['num-of-doors'].value_counts().idxmax()


# In[50]:


df["num-of-doors"].replace(np.nan, "four", inplace = True)


# Finally, let's drop all rows that do not have price data:

# In[51]:


# simply drop whole row with NaN in "price" column
df.dropna(subset=["price"], axis=0, inplace = True)

# reset index, because we droped two rows
df.reset_index(drop = True, inplace = True)


# ## Correct  data format
# 
# <div>** .dtype()** to check the data type</div>
# <div>** .astype()** to change the data type</div>

# In[52]:


df.dtypes


# #### Convert data types to proper format:

# In[53]:


df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")


# In[54]:


df.dtypes


# # Data Normalization

# In[55]:


df.head()


# In[56]:


df['city-L/100km'] = 235/df["city-mpg"]
df.head()


# ## Question  #2:
# According to the example above, transform mpg to L/100km in the column of "highway-mpg", and change the name of column to "highway-L/100km":

# ### transform mpg to L/100km by mathematical operation (235 divided by mpg)
# df["highway-mpg"] = 235/df["highway-mpg"]
# 
# ### rename column name from "highway-mpg" to "highway-L/100km"
# df.rename(columns={'"highway-mpg"':'highway-L/100km'}, inplace=True)
# 
# ### check your transformed data 
# df.head()

# <a id="ref6"></a>
# # Data Normalization 

# In[57]:


df['length'] = df['length']/df['length'].max()
df['width'] = df['width']/df['width'].max()


# ## Questiont #3:
# According to the example above, normalize the column "height":

# In[58]:


df['height']=(df['height'] - df['height'].mean())/df['height'].std()
df[["height"]].head()


# df['height'] = df['height']/df['height'].max() 
# df[["length","width","height"]].head()

# In[59]:


df.to_csv('clean_df.csv')

