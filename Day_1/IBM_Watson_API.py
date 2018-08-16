
# coding: utf-8

# ## IBM Watson API Service

# In[ ]:


get_ipython().system('pip install --upgrade --user --force watson-developer-cloud')


# In[1]:


import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, EmotionOptions


# ## Input test files and sentence

# In[2]:


text_to_analyze ='I am learning so much from this AI course. Python is awesome and super easy to learn' 

file1 = open("data/news1.txt","r") 

file2 = open("data/news2.txt", "r")


# ## Initialize Natural Language Understanding API Service

# In[3]:


natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2017-02-27',
    username='10b31e8e-0f4d-44dc-b28e-5bed2d295fae',
    password='f1AE14yyUQtt')


# ## Run the API Service on test sentence

# In[4]:


response = natural_language_understanding.analyze(
    text=text_to_analyze,
    features=Features(emotion=EmotionOptions()))


# In[5]:


print(json.dumps(response, indent=2))


# ## Run the API Service on test file 1

# In[6]:


response = natural_language_understanding.analyze(
    text=file1.read(),
    features=Features(entities=EntitiesOptions(), keywords=KeywordsOptions()))


# In[7]:


print(json.dumps(response, indent=2))


# In[8]:


response = natural_language_understanding.analyze(
    text=file2.read(),
    features=Features(entities=EntitiesOptions(), keywords=KeywordsOptions()))


# In[9]:


print(json.dumps(response, indent=2))

