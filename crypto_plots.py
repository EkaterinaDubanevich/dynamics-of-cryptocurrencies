#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import os
import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams
rcParams['figure.figsize'] = 15, 10
sns.set(style="whitegrid")


# In[2]:


df = pd.read_csv(r'path', sep = ',')
df['Date'] = pd.to_datetime(df.Date)
df.dtypes
sg = pd.DataFrame()


# In[3]:


path = r""
os.listdir (path)


# In[4]:


for (current_path, dirs, files) in os.walk(path):
    for file in files:
        data_path = (current_path + '\\' + file)
        a = pd.read_csv(data_path, sep = ',')
        df = pd.concat((df, a))
        


# In[5]:


df


# In[6]:


for (current_path, dirs, files) in os.walk(path):
    for i in [name for name in a]:
        data_path = (current_path + '\\' + file)
        a = pd.read_csv(data_path, sep = ',')
        a['Date'] = pd.to_datetime(a.Date)
        sns.lineplot(data = a, x= 'Date', y = 'High')


# In[7]:


df[df.Name == 'Bitcoin' ].Close


# In[8]:


df.info()


# In[9]:


df['Date'] = pd.to_datetime(df.Date)


# In[17]:


get_ipython().run_cell_magic('time', '', "sns.lineplot(data=df, x=df.Date, y=np.log(df.Close), hue='Name');")


# In[15]:


sns.lineplot(data=df, x=df.Date, y=df.Close);


# In[ ]:


df.Name.unique()


# In[14]:


for name in df.Name.unique():
    print(name)
    sns.lineplot(data=df[df.Name == name], x='Date', y='Close');
    plt.show()

