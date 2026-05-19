#!/usr/bin/env python
# coding: utf-8

# # Range

# In[2]:


range(5)


# In[3]:


for i in range(5):
    print(i)


# In[4]:


range(10,20)


# In[5]:


print(range(10,20))


# In[6]:


range(0,20,2)


# In[29]:


list[int](range(10,20))


# In[30]:


list[int](range(10,50,5))


# # Dict

# In[7]:


d= {1:'app',2:'bap',3:'cap'}
d


# In[8]:


d[1]


# In[9]:


d[4]='dap'
d


# In[14]:


keys ={10,20,30,40}
values = {'gap','pap','map','nap'}


# In[15]:


d.items()


# In[16]:


d


# In[17]:


d[5] = [1,2,3]
d


# In[18]:


d[2+3j] = True


# In[19]:


d


# In[20]:


keys = {'a','b','c','d'}
value = [10,20,30]
d2 = dict.fromkeys(keys,value)
d2


# In[21]:


value.append(40)
d2


# In[22]:


d3 = {10,20,30,40}
d3.add(70)
d3


# In[23]:


ds = frozenset[int](d3)
ds


# In[24]:


type[int](ds)


# In[25]:


ds.add(100)


# In[26]:


ds.remove(10)


# In[27]:


ds


# In[28]:


ds.pop()


# In[ ]:




