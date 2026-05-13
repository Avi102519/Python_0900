#!/usr/bin/env python
# coding: utf-8

# In[1]:


l =[]


# In[2]:


type(l)


# In[3]:


l


# In[6]:


len(l)


# In[7]:


l1 = [10,20,30] #Passed 3 values in a list l1


# In[8]:


l1


# In[9]:


len(l1)


# In[10]:


l1.append(90)
l1


# In[11]:


l1.append(40)
l1.append(50)
l1.append(60)


# In[12]:


l1


# In[13]:


l1.append(10)


# In[14]:


l1


# In[15]:


len(l1)


# In[16]:


l1.append('70,80')


# In[17]:


l1


# In[18]:


l1.append('55','65')


# In[19]:


l1.append(['a','b','c'])
l1


# In[20]:


l2=[34,5.3,'Aira',1+2j,True]
l2


# In[21]:


print(l)
print(l1)
print(l2)


# In[23]:


print(len(l))
print(len(l1))
print(len(l2))


# In[26]:


print(id(l))
print(id(l1))
print(id(l2))


# In[27]:


print(type(l))
print(type(l1))
print(type(l2))


# In[28]:


l1


# In[29]:


#list Membership
10 in l1


# In[30]:


'abc' in l1


# In[31]:


['a','b','c'] in l1


# In[32]:


100 in l1


# In[33]:


l2


# In[34]:


l3


# In[35]:


l3 = l2.copy()
l3


# In[36]:


print(id(l2))
print(id(l3))


# In[37]:


l3


# In[38]:


l3.clear()


# In[39]:


l3


# In[40]:


l3.append('chukka')
l3


# In[41]:


del(l3)


# In[42]:


l3


# In[43]:


l2.count()


# In[44]:


count(l2)


# In[45]:


l2.count(10)


# In[46]:


l1.count(10)


# In[47]:


l1[:]


# In[48]:


l1[-1]


# In[51]:


l1[4:]


# In[53]:


l1[3:-1]


# In[54]:


l1[0:10:3]


# In[55]:


l1[::1]


# In[56]:


l1[::2]


# In[57]:


l1[::3]


# In[58]:


l1[::-1]


# In[59]:


l1[::-3]


# In[ ]:




