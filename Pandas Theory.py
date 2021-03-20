#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
sr = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])


# In[4]:


sr


# In[5]:


sr.index.name = 'index'


# In[6]:


sr


# In[7]:


sr * 2


# In[8]:


sr.values


# In[9]:


sr.index


# In[12]:


df = pd.DataFrame({'country': ['France', 'Russia', 'Belarus'], 
                   'population': [17.04, 12.03, 10.0], 
                   'square': [2567, 2345, 234456]}, index=['a', 'b', 'c'])


# In[13]:


df


# In[14]:


df['country']


# In[17]:


df.country


# In[18]:


df.loc['a']


# In[19]:


df.iloc[0]


# In[ ]:


df = pd.read_csv("file_name") # считывает из файла в таблицу сразу 

