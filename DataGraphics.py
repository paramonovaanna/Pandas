#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[2]:


df = pd.read_csv("C:\\Users\\ASUS\\Documents\\advertising.csv")


# In[3]:


fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(70, 20))
axes[0].plot(df['TV'], '--r', df['Sales'])
axes[0].set_title('TV - Sales')
axes[1].plot(df['Radio'], '--r', df['Sales'])
axes[1].set_title('Radio - Sales')
axes[2].plot(df['Newspaper'], '--r', df['Sales'])
axes[2].set_title('Newspaper - Sales')


# In[4]:


df1 = pd.read_csv("C:\\Users\\ASUS\\Documents\\weights-heights.csv")


# In[5]:


figs, axes = plt.subplots(nrows=1, ncols=1, figsize=(70, 20))
data1 = (np.array(df1['Weight']) - min(np.array(df1['Weight']))) / (max(np.array(df1['Weight'])) - min(np.array(df1['Weight'])))
data2 = (np.array(df1['Height']) - min(np.array(df1['Height']))) / (max(np.array(df1['Height'])) - min(np.array(df1['Height'])))
axes.plot(data2, '--r', data1)


# In[6]:


df2 = pd.read_csv("C:\\Users\\ASUS\\Documents\\winequality-red.csv", sep=';')


# In[7]:


fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(40, 10))
axes[0].plot(df2['citric acid'], '--r', df2['chlorides'])
axes[1].plot(df2['fixed acidity'], '--r', df2['quality'])


# In[ ]:




