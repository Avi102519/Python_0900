#!/usr/bin/env python
# coding: utf-8

# # int Typecasting
# Bool,Complex,numeric string and float data types can be converted to int.
# Complex and text string can't be converted to int.
# int accepts one argument, it wont accept more than one arguments

# In[1]:


int(12.3)


# In[2]:


int('Ten')


# In[3]:


int(True)


# In[4]:


int(False)


# In[5]:


int(1+2j)


# In[14]:


int(10)


# In[15]:


int('10')


# In[7]:


int(2.3,4.5)


# # float Typecasting
# Bool,int and float data types can be converted to float.
# Complex and text string can't be converted to float
# float accepts one argument, it wont accept more than one arguments

# In[8]:


float(10)


# In[9]:


float('10')


# In[10]:


float('Ten')


# In[11]:


float(2+3j)


# In[12]:


float(True)


# In[13]:


float(False)


# # bool Typecasting
# float,int,complex and string data types can be converted to bool.
# bool accepts one argument, it wont accept more than one arguments

# In[16]:


bool(10)


# In[17]:


bool(12.3)


# In[18]:


bool('10')


# In[19]:


bool('Ten')


# In[20]:


bool(2+3j)


# In[21]:


bool(2,3)


# # Complex Typecasting
# float,int and bool data types can be converted to complex.
# complex accepts two argument, it wont accept more than two arguments

# In[22]:


complex(1)


# In[23]:


complex(2.3,3.4)


# In[24]:


complex(True,False)


# In[25]:


complex('one')


# In[26]:


complex(3,4,6)


# In[27]:


complex(one)


# # String Typecasting
# float,int complex and bool data types can be converted to string.
# String accepts one argument, it wont accept more than one argument

# In[28]:


str(1)


# In[29]:


str(2.3)


# In[30]:


str(1+2j)


# In[31]:


str('one')


# In[32]:


str(1,2)


# In[ ]:




