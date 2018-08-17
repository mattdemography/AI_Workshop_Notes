
# coding: utf-8

# ## Travelling salesman problem - To find the shortest roads that connects a set of cities

# In[1]:


import itertools
import copy
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'notebook')


# ## Load Data
# - node1 & node2: names of the nodes connected.
# - trail: edge attribute indicating the abbreviated name of the trail for each edge. For example: rs = red square
# - distance: edge attribute indicating trail length in miles.
# - color: trail color used for plotting.
# - estimate: edge attribute indicating whether the edge distance is estimated from eyeballing the trailmap (1=yes, 0=no) as some distances are not provided. This is solely for reference; it is not used for analysis.

# In[2]:


edgelist = pd.read_csv('https://gist.githubusercontent.com/brooksandrew/e570c38bcc72a8d102422f2af836513b/raw/89c76b2563dbc0e88384719a35cba0dfc04cd522/edgelist_sleeping_giant.csv')


# In[3]:


edgelist


# ## Create Graph

# In[4]:


g = nx.Graph()


# In[5]:


# Add edges and edge attributes
for i, elrow in edgelist.iterrows():
    g.add_edge(elrow[0], elrow[1], attr_dict=elrow[2:].to_dict())


# In[6]:


# draw the network 
nx.draw_networkx(g)


# In[7]:


# Edge list example
print(elrow[0]) # node1
print(elrow[1]) # node2
print(elrow[2:].to_dict()) # edge attribute dict


# In[8]:


g.nodes()


# In[9]:


g.edges(data=True)


# g.neighbors('v_end_west')

# In[10]:


g.degree()


# In[11]:


g.has_edge('v_end_west','b_rd_dupe')

