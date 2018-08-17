
# coding: utf-8

# In[1]:


import networkx as nx
import numpy as np
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'notebook')


# In[2]:


# Instantiate the graph
G1 = nx.Graph()
# add node/edge pairs
G1.add_edges_from([(0, 1),
                   (0, 2),
                   (0, 3),
                   (1, 7),
                   (1, 6),
                   (2, 4),
                   (2, 5),
                   (3, 8)])


# In[3]:


G1.nodes()


# In[4]:


G1.edges()


# In[5]:


# draw the network G1
nx.draw_networkx(G1)


# In[6]:


print(list(nx.dfs_edges(G1,0)))


# In[7]:


print(list(nx.bfs_edges(G1, 0)))


# In[14]:


print(nx.shortest_path(G1, source=5, target=7)) #Find Shortest Path

