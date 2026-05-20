#!/usr/bin/env python
# coding: utf-8

# # Numpy Crash Course

# In[24]:


import numpy as np


# In[25]:


np.version


# In[26]:


np.__version__


# In[27]:


my_list= [0,1,2,3,4,5]
my_list


# In[29]:


type(my_list)


# # Creating array from list

# In[30]:


arr = np.array(my_list)


# In[31]:


arr


# In[32]:


print(type(my_list))
print(type(arr))


# In[33]:


np.arange(10)


# In[34]:


np.arange(10,20)


# # Creating Array with a step of 2 between 10 and 19

# In[61]:


np.arange(10,20,2)


# # Creating array with a step of 5 between 10 and 19

# In[62]:


np.arange(10,20,5)


# In[63]:


np.arange(10,20,3)


# In[35]:


np.arange(10,50,5)


# In[36]:


np.arange(20,10)


# In[37]:


np.arange(-20,10) # first argument always less than second argument


# # Creating an array with float zeros

# In[38]:


np.zeros(3) #Parameter Tuning


# # Creating an array with int zeros

# In[39]:


np.zeros(3,dtype = int) # Hyper Parameter Tuning


# In[40]:


np.zeros([2,2])


# In[41]:


np.zeros([2,2],dtype = int)


# In[18]:


np.zeros([10,10],dtype = int)


# # Generate an array with float ones

# In[42]:


np.ones(4)


# In[43]:


np.ones(4,dtype = int)


# In[44]:


np.ones([2,2],dtype = int)


# In[22]:


np.ones([10,10],dtype = int) #Unambigous(reprFormat)represen... includes ',s',() and linebrakes


# In[64]:


np.twos(3)


# In[46]:


np.rand(3)


# # Code to generate an array of 3 random float values

# In[47]:


np.random.rand(3) #np as library,random -module, rand-Package


# In[48]:


np.random.rand(3,4)


# In[49]:


np.random.rand(3,4)


# In[50]:


np.random.randint(3)


# In[66]:


np.random.rand(2,2)


# # to generate an array of random int values

# In[52]:


np.random.randint(10,20)


# In[53]:


print(np.random.randint(1,20,4))


# In[54]:


m= np.random.randint(1,10,(4,6)) #pretty-printing (__str__) rules,removes,',s',(),linebrakes
print(m)


# In[67]:


np.random.randint(1,10,(4,6))


# In[55]:


m[0] # first row


# In[ ]:


m[0] =[7,5,3,9,5,1] #Array Manipulation


# In[56]:


m


# In[57]:


m[2]


# In[58]:


m[-3]


# In[59]:


m[0,4]


# In[60]:


m[-2,-3]


# In[70]:


k = range(0,10)
print(k)


# In[73]:


m


# In[74]:


len(m)


# In[76]:


m.shape


# In[77]:


m[:]


# In[78]:


m[]


# In[79]:


m[::]


# In[80]:


m[0:4]


# In[81]:


m1 = np.random.randint(1,10,(9,9))


# In[82]:


m1


# In[83]:


m1[0:9:3]


# In[84]:


m1[::2]


# In[85]:


m1[::5]


# In[86]:


m1


# In[87]:


m1[::-1]


# In[89]:


m1[::-4]


# In[90]:


arr


# In[91]:


arr.shape()


# In[92]:


arr.shape


# In[93]:


arr.reshape(2,3)


# In[94]:


n = arr.reshape(2,3)
n


# In[95]:


arr


# In[96]:


arr.reshape(4,2)


# In[97]:


arr.reshape(1,6)


# In[98]:


arr.reshape(6,1)


# In[99]:


m


# In[100]:


m[2,4]


# In[101]:


m[2:4]


# In[102]:


m[:,2] # to print columns


# In[104]:


m[:,-3]


# In[105]:


m1[2:]


# In[106]:


m1


# In[107]:


m1[:4]


# In[109]:


m1[1:4, 1:3]


# In[110]:


m1


# In[111]:


m1[3:8, 3:8]


# # Masking or filter in Matrix

# In[112]:


m1


# In[113]:


m1.shape


# In[114]:


id(m1)


# In[115]:


type(m1)


# In[116]:


m1.info


# In[117]:


m1.info()


# In[118]:


m1<5


# In[119]:


m1[m1<5]


# In[120]:


m1[m1<=5]


# In[121]:


m1[m1!=5]


# In[122]:


m1[m1==5]


# In[123]:


m1[m1>5]


# In[ ]:




