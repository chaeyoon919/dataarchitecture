#!/usr/bin/env python
# coding: utf-8

# In[6]:


pip install pandas


# In[13]:


import pandas as pd
bank_data = pd.read_csv("dataset/bank_data.csv")


# In[17]:


print(type(bank_data))


# In[21]:


print(bank_data)


# In[23]:


pip install pymongo


# In[1]:


from pymongo import MongoClient
client = MongoClient('127.0.0.1',27017)
print(client)


# In[ ]:




