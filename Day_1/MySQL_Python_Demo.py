
# coding: utf-8

# # Import required libraries

# In[1]:


import csv
import getpass
import MySQLdb
import pandas as pd
from sqlalchemy import create_engine


# # Setup the Database Connection w/ Python

# In[3]:


PASS = getpass.getpass('Password:')


# In[4]:


# http://docs.sqlalchemy.org/en/latest/dialects/mysql.html
# http://docs.sqlalchemy.org/en/latest/core/connections.html
DATABASE = 'firstdb'
engine = create_engine("mysql+mysqldb://root:"+PASS+"@localhost/")
engine.execute("create database "+DATABASE)
engine = create_engine("mysql+mysqldb://root:"+PASS+"@localhost/"+DATABASE)
connection = engine.connect()


# # Load Dataset to Python

# In[5]:


# https://archive.ics.uci.edu/ml/datasets/iris
# https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
iris = pd.read_csv('data/iris.data', header=None)


# In[6]:


iris[:5]


# # Add records to MYSQL Database

# In[7]:


iris.to_sql('iris_data', con=engine, if_exists='append', index=False)


# ## `pandas.DataFrame.to_sql` Documentation
# ### https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_sql.html

# In[7]:


iris.to_sql('iris_data', con=engine, if_exists='replace', index=False)


# # Read from MySQL Database using Python

# In[8]:


result = connection.execute("select * from iris_data")


# ### Pythoninc way of doing it

# In[9]:


for row in result:
    print(row)


# ### Read from SQL using Python Pandas

# In[10]:


result = connection.execute("select * from iris_data")
pd.DataFrame.from_records(result)


# ## Alternate way to execute SQL Commands

# In[11]:


sql_command = "select * from iris_data"
df = pd.read_sql(sql_command, con=connection)


# In[12]:


df

