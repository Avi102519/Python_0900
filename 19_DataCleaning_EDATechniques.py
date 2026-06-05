#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


emp = pd.read_excel(r"/Users/aviswe/Desktop/900/Materials/June26/4-June/Rawdata1.xlsx")


# In[3]:


emp


# In[4]:


id(emp)


# In[5]:


emp.columns


# In[6]:


emp.shape #Dimensions of the data frame


# In[7]:


emp.head()


# In[8]:


emp.tail()


# In[9]:


emp.info


# In[10]:


emp.isnull()


# In[11]:


emp.isna()


# In[12]:


emp.isnull().sum()


# In[13]:


emp.columns


# In[14]:


emp.dtypes


# In[15]:


#!pip install --upgrade openpyx


# In[16]:


emp.isnull().sum()


# In[17]:


type(emp)


# In[18]:


emp.info()


# In[19]:


emp.describe() #Descriptive statistics


# # Data Cleaning

# In[20]:


emp.columns


# In[21]:


emp.head()


# In[22]:


emp['Name'] # name is having some regexpressions


# In[23]:


emp['Name'] = emp['Name'].str.replace(r'\W','',regex=True)


# In[24]:


emp['Name']


# In[25]:


emp['Domain'] = emp['Domain'].str.replace(r'\W','',regex=True)


# In[26]:


emp


# In[27]:


emp['Age'] = emp['Age'].str.extract('(\d+)')


# In[28]:


emp


# In[29]:


emp['Location'] = emp['Location'].str.replace(r'\W','',regex= True)


# In[30]:


emp


# In[31]:


emp['Salary'] = emp['Salary'].str.replace(r'\W','',regex= True)


# In[32]:


emp


# In[33]:


emp['Exp'] = emp['Exp'].str.extract('(\d+)')


# In[34]:


emp


# In[35]:


clean_data= emp.copy()
clean_data


# In[36]:


clean_data.isnull().sum()


# In[37]:


# fill missing values
emp['Age']


# In[38]:


import numpy as np


# In[39]:


clean_data['Age'] = clean_data['Age'].fillna(np.mean(pd.to_numeric(clean_data['Age'])))


# In[40]:


clean_data


# In[41]:


clean_data['Exp']= clean_data['Exp'].fillna(np.mean(pd.to_numeric(clean_data['Exp'])))


# In[42]:


clean_data


# In[43]:


clean_data['Location']= clean_data['Location'].fillna(np.mean(pd.to_numeric(clean_data['Location'])))


# In[44]:


clean_data['Location']= clean_data['Location'].fillna(clean_data['Location'].mode()[0])
#0-Mode to a column attribute


# In[45]:


clean_data


# In[46]:


id(clean_data)


# In[47]:


clean_data.info()


# In[48]:


clean_data.columns


# In[49]:


clean_data['Age'] = clean_data['Age'].astype(int)
clean_data['Exp'] = clean_data['Exp'].astype(int)
clean_data['Age'] = clean_data['Age'].astype(int)

clean_data['Name'] = clean_data['Name'].astype('category')
clean_data['Domain'] = clean_data['Domain'].astype('category')
clean_data['Location'] = clean_data['Location'].astype('category')
#astype- System designed data type- user defined datatype


# In[50]:


clean_data.info()


# In[51]:


clean_data


# In[52]:


clean_data.to_csv('clean_data.csv')


# In[53]:


import os
os.getcwd()


# In[ ]:




