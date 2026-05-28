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


# In[56]:


ds.columns


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


# In[90]:


#filter1 = [ds['InternetUsers']<2]
Filter1 = ds.InternetUsers < 2 


# In[91]:


#filter2 = [ds['BirthRate']>40]
Filter2 = ds.BirthRate >40


# In[93]:


#ds[(ds['BirthRate'] > 40) & (ds['InternetUsers'] < 2)]
#ds[filter1 & filter2]
ds[Filter1 & Filter2]


# In[57]:


ds['IncomeGroup'].unique()


# In[58]:


ds['IncomeGroup'].nunique()


# In[59]:


ds[ds.IncomeGroup == 'High income']


# In[60]:


ds[ds.IncomeGroup == 'Low income']


# In[61]:


import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.figsize'] = 6,2 # rcParams -- Reduce the size-6 width and 2 height

import warnings
warnings.filterwarnings('ignore') # dont display/ignore the warning messages
#pandas- Dataframes
#Numpy -- nd array
#Matplotlib--Visualizaion
#Seaborn- Distribution Visualization


# In[64]:


ds['InternetUsers']


# In[68]:


vis1 = plt.distplot(ds['InternetUsers'])


# In[67]:


vis1 = sns.distplot(ds['InternetUsers'])
#distplot can be drawn suing one varaible which is called Univariate Analysis


# In[69]:


vis2 = sns.displot(ds['InternetUsers'])


# In[72]:


vis3 = sns.distplot(ds['InternetUsers'],bins = 15)


# In[73]:


vis4 = sns.boxplot(data = ds,x= 'IncomeGroup',y = 'BirthRate')


# In[74]:


vis5 = sns.lmplot(data=ds,x= 'InternetUsers',y = 'BirthRate')


# In[76]:


vis6 = sns.lmplot(data=ds,x= 'InternetUsers',y = 'BirthRate',fit_reg = False)


# In[77]:


vis6 = sns.lmplot(data=ds,x= 'InternetUsers',y = 'BirthRate',fit_reg = False,hue = 'IncomeGroup')


# In[78]:


vis6 = sns.lmplot(data=ds,x= 'InternetUsers',y = 'BirthRate',fit_reg = True,hue = 'IncomeGroup')


# In[ ]:




