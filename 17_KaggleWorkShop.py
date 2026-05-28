#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[6]:


movies = pd.read_csv(r'/Users/aviswe/Desktop/900/Materials/May26/28-May/movie.csv')
ratings = pd.read_csv(r'/Users/aviswe/Desktop/900/Materials/May26/28-May/rating.csv')
tags = pd.read_csv(r'/Users/aviswe/Desktop/900/Materials/May26/28-May/tag.csv')


# In[3]:


movies.shape


# In[14]:


print(type(movies))


# In[4]:


movies.columns


# In[16]:


movies.head(20)


# In[7]:


tags.shape


# In[8]:


tags.columns


# In[15]:


tags.head(20)


# In[10]:


ratings.shape # Data Analysis in Excel is limited to 1048576
#The purpose of building pandas is if the data is greater than 1048576 rows.
#For bigdata pandas cant hanndel then we use Apache Spark


# In[11]:


ratings.columns


# In[12]:


ratings.head()


# In[13]:


#to remove timestamp
print(movies.columns)
print(tags.columns)
print(ratings.columns)


# In[17]:


#For current analysis we dont need timestamp and hence removing them.
del ratings['timestamp']
del tags['timestamp']


# In[18]:


ratings.head()


# In[19]:


tags.head()


# # Series

# In[20]:


#iloc= Index locking. user can customize to lock the index
row_0 = tags.iloc[0]


# In[21]:


row_0


# In[22]:


type(row_0)


# In[23]:


print(row_0)


# In[24]:


row_0.index


# In[25]:


row_0.name


# In[26]:


row_0['userId']


# In[27]:


'rating' in row_0


# In[28]:


row_0 = row_0.rename('firstRow')


# In[30]:


row_0.name


# # Data Frames

# In[31]:


tags.head()


# In[32]:


tags.index


# In[34]:


tags.columns


# In[36]:


tags.iloc[[0,11,500]] # user can lock the specified indexes


# # Descriptive Statistics

# In[37]:


#lets look how the ratings are distributed
ratings['rating'].describe()


# In[38]:


ratings.describe()


# In[40]:


ratings['rating'].min()


# In[41]:


ratings['rating'].max()


# In[42]:


ratings['rating'].std()


# In[43]:


ratings['rating'].mode()
#The mode of a set of values is the value that appears most often


# In[44]:


ratings.corr() #Compute pairwise correlation of columns, excluding NA/null values.


# In[45]:


filter1 = ratings['rating']>10
print(filter1)
filter1.any()


# # Data cleaning: Handling Missing Data

# In[46]:


movies.shape


# In[47]:


movies.isnull().any().any()


# movies dataset is not having any null values

# In[48]:


ratings.shape


# In[49]:


ratings.isnull().any().any()


# ratings dataset is not having any null values

# In[50]:


tags.shape


# In[51]:


tags.isnull().any().any()


# tags dataset is having null values

# In[52]:


tags= tags.dropna()


# In[53]:


tags.shape


# In[54]:


tags.isnull().any().any()


# we have removed null values from the tags datset

# # Data Visualization

# In[55]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[56]:


ratings.hist(column='rating',figsize=(10,5))


# In[57]:


ratings.boxplot(column='rating',figsize=(10,5))


# # Slicing Out Columns

# In[58]:


tags['tag'].head()


# In[60]:


movies[['title','genres']].head()


# In[61]:


ratings[-10:]


# In[62]:


tag_counts = tags['tag'].value_counts()
tag_counts[-10:]


# In[63]:


tag_counts[:10].plot(kind = 'bar',figsize=(10,5))


# In[ ]:




