#!/usr/bin/env python
# coding: utf-8

# # Day-14 Python Challenge

# # Pandas Library

# In[2]:


import pandas as pd


# In[7]:


df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
df.head() ## Head function use to show top 5 five content of the data


# # Tail Function

# In[8]:


df.tail()


# # Check datatypes in dataset

# In[10]:


df.dtypes


# # Decribe function

# In[12]:


df.describe()


# In[19]:


df[['Name','Age','Ticket']].head() 


# # Object Function

# In[22]:


df.dtypes == 'object'  ## Use to check integer value in a columns 


# In[23]:


df.dtypes == 'float'


# In[32]:


df[df.dtypes[df.dtypes == 'float64'].index].head()


# In[33]:


df[df.dtypes[df.dtypes == 'int64'].index].head()


# In[37]:


df.columns


# In[41]:


df['Embarked'].head()


# # Slicing Function

# In[42]:


df[['Embarked']][4:11]


# In[43]:


df[['Embarked']][4:11:2]


# In[44]:


df[['Name','Embarked']][4:11:2]


# # Create new column

# In[62]:


df['Lats_Column'] = 0
df.head()[0:5:2]


# # Insert Function

# In[63]:


df.insert(loc = 3, column = 'Food', value = 0)
df


# In[65]:


df.head()

