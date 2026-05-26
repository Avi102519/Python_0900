#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install numpy==1.26.4 pandas==2.3.3


# In[3]:


#pip install --upgrade openpyxl


# In[4]:


import pandas as pd


# In[6]:


#ds=pd.read_excel(r"/Users/aviswe/Desktop/900/Datasets/data.xlsx")
ds=pd.read_excel(r"/Users/aviswe/Desktop/900/Datasets/data.xlsx")


# In[7]:


len(ds)


# In[8]:


id(ds)


# In[9]:


pd.__version__


# In[10]:


ds.shape


# In[11]:


ds.head()


# In[12]:


ds.tail()


# In[13]:


ds.info()


# In[14]:


len(ds.columns)


# In[15]:


ds.dtypes


# In[16]:


ds


# In[17]:


ds.columns


# In[18]:


ds['CountryName']


# In[19]:


ds['CountryCode']


# In[20]:


ds[['BirthRate', 'InternetUsers']]


# In[21]:


ds_numerical_data = ds[['BirthRate', 'InternetUsers']]
ds_categorical_data = ds[['CountryName', 'CountryCode','IncomeGroup']]


# In[22]:


ds_numerical_data


# In[23]:


ds_categorical_data


# In[24]:


ds_numerical_data.head(1)


# In[25]:


print(ds.columns)
print(ds_numerical_data.columns)
print(ds_categorical_data.columns)


# In[26]:


ds[:]


# In[27]:


ds[10:11:10]


# In[28]:


ds[10:100:20]


# In[29]:


ds[2:5]


# In[30]:


ds[::5]


# In[31]:


ds[2:-1]


# In[32]:


ds[::-1]


# In[33]:


ds[::-5]


# In[34]:


ds.isnull()


# In[35]:


ds.isna()


# In[36]:


ds.isnull().sum()


# In[37]:


ds.describe() # descriptive statistics, Bydefault it shares the numerical data  


# In[38]:


ds_categorical_data.describe()


# In[39]:


ds_numerical_data.describe()


# In[40]:


ds.columns


# In[41]:


ds.columns=['a','b','c','d','e'] #Renaming the columns names
ds


# In[42]:


ds.columns = ['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers','IncomeGroup']


# In[43]:


ds


# In[44]:


ds.columns


# In[45]:


ds['mycalc']= ds.InternetUsers * ds.BirthRate


# In[46]:


ds.head()


# In[47]:


ds= ds.drop('mycalc',axis = 1)


# In[48]:


ds


# In[49]:


ds['InternetUsers']<2


# In[50]:


ds[ds['InternetUsers']<2]


# In[51]:


len(ds[ds['InternetUsers']<2])


# In[52]:


len(ds[ds['BirthRate']>40])


# In[53]:


ds[ds['BirthRate']>40]


# In[55]:


ds[(ds['BirthRate'] > 40) & (ds['InternetUsers'] < 2)]


# In[ ]:




