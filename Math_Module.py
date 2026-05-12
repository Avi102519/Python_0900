#!/usr/bin/env python
# coding: utf-8

# ### import math module 
# https://docs.python.org/3/library/math.html

# In[12]:


x=sqrt(25)


# In[13]:


import math #math is module/library
math.sqrt(25) #Sqrt is a inbuilt function in math module/library


# In[14]:


x= math.sqrt(25)
x


# In[15]:


x1 = math.sqrt(15)
x1


# In[16]:


math.floor(2.3) #floor function retuns the lower limit of the decimal


# In[17]:


math.ceil(2.1) #Ceil function returns the highest limit of the value


# In[18]:


print(math.floor(2.9))


# In[19]:


print(math.ceil(2.1))


# In[20]:


print(math.pow(3,2)) #1st number squares with second number


# In[21]:


print(math.pow(2,8))


# In[22]:


print(math.pow(2,))


# In[23]:


print(math.pi) #These are constant values


# In[24]:


print(math.e) #these are constant values


# In[25]:


math.e


# In[26]:


math.pi


# In[27]:


import math as m #Assigning math module to m; it is easy to call as required
m.sqrt(10)


# In[28]:


from math import sqrt,pow #math module has many functions if you want to call specific function then use the fn
pow(5,2)


# In[29]:


help(math)


# In[31]:


#code optimization
#instead of calling the math functions multiple times use * to refer all functions in Math module


# # User input function in python || command line input

# In[34]:


x= input()
y= input()
z=x+y
print(z) #Console is waiting for user to enter input
#also if you work in idle


# In[36]:


print(type(x))
print(type(y))


# In[37]:


#input box defaults to string type so the + button is not going to add and concatnates
x1 = input('Enter the 1st number')
y1 = input('Enter the 2nd number')
z1= x1+y1
print(z1)


# In[38]:


x1 = input('Enter the 1st number') #whenrver you works in input function it always give you string
a1 =int(x1)
y1 = input('Enter the 2 nd number')
b1= int(y1)
z1=a1+b1
print(z1)


# #for the above code notice we are using many lines because of that some memory is getting wasted

# In[39]:


x2 = int(input('enter 1st value'))
y2 = int(input('enter 2nd value'))
z2= x2+y2
print(z2)


# #lets take input from the user in string format

# In[47]:


str = input('enter a char')


# In[48]:


type(str)


# In[49]:


str[1:]


# In[50]:


str[2:4]


# In[51]:


str[-3]


# In[52]:


str[-5]


# In[55]:


str1 = input('enter a string')[4:8]
str1


# In[57]:


print(str1)


# In[61]:


str2 = input('Enter SSN')[5:]
str2


# # Use eval function for Expressions

# In[62]:


g = eval(input('Enter an expression'))
print(g)


# In[ ]:




