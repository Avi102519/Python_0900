#!/usr/bin/env python
# coding: utf-8

# # Python Basics

# In[1]:


3


# In[2]:


5


# In[3]:


3+5


# In[4]:


_


# In[5]:


_+2


# In[6]:


_-4


# In[7]:


_/2 # float division


# In[8]:


_+3


# In[9]:


_//2 # int division


# In[10]:


6//2


# In[11]:


6.0/2


# In[12]:


8.0//2


# In[13]:


9+8-3*4


# In[14]:


3+(4*5)-6//8*6


# In[15]:


4+5-10*3


# In[16]:


6//2.0


# In[21]:


import keyword
keyword.kwlist


# # Python Variables

# In[26]:


first_name = 'Durandhar'
Last_Name = 'Adityadhar'
country = 'India'
city = 'Kashmir'
age = '42'
is_married = 'Married'
skills = ['Director','Storywriter','Producer','Screenplay']
person_info = {
    'firstname':'Jaskirat',
    'lastname':'Singh',
    'country':'India',
    'city':'Patankot'
    }


# In[27]:


print('First_Name:', first_name)
print('First Name Length:', len(first_name))
print('Last_Name:', Last_Name)
print('Last Name Length:', len(Last_Name))
print('Country:', country)
print('City:', city)
print('Age:', age)
print('Martial status:', is_married)
print('Skills:', skills)
print('PersonalInformation:', person_info)


# # Declaring multiple variables in one line

# In[29]:


first_name, Last_Name, country, city, age, is_married, skills, person_info


# In[30]:


#id()
#length()
#Print()
#type()


# In[31]:


#float-- The value with Decimal


# In[32]:


f = 110.34


# In[33]:


type(f)


# In[34]:


#e for Exponential #only for e no other alphabets works


# In[35]:


2e0


# In[36]:


2e1


# In[37]:


2e2


# In[38]:


2e3


# In[39]:


2a1


# In[40]:


e2


# In[41]:


1e2


# In[42]:


1e3


# # String

# In[43]:


s= welcome
s


# In[44]:


True


# In[45]:


s = 'welcome'
s


# In[46]:


id(s)


# In[47]:


len(s)


# In[48]:


s1 = "Welcome to Nit"


# In[49]:


s2 = '''welcome
to
nit'''


# In[51]:


s3 = "welcome"


# In[52]:


id(s)


# In[53]:


id(s3)


# # String Indexing & String Slicing

# In[54]:


s[1:6:2]


# In[55]:


s[2:]


# In[56]:


s[:7]


# In[57]:


s[:5]


# In[58]:


s[:10]


# In[59]:


s[:1000]


# In[60]:


s[1000]


# In[61]:


a= 'Coolstuff'


# In[62]:


a[2:9]


# In[63]:


a[1]


# In[64]:


a[3:5]


# In[65]:


len(a)


# In[66]:


a[-2:-6]


# In[67]:


a


# In[68]:


a[-6:-2]


# In[69]:


a[1:]


# In[70]:


a[:9]


# In[71]:


a[6:1]


# In[72]:


a[2:9]


# In[73]:


a[]


# In[74]:


a[:]


# In[75]:


a[4]


# In[76]:


a[-9]


# In[77]:


a[-10]


# In[78]:


a = 10.6


# In[79]:


int(a)


# In[80]:


type(a)


# In[81]:


id(a)


# In[84]:


import keyword
keyword.kwlist


# In[85]:


c=10+20j


# In[86]:


c.real


# In[87]:


c.imag


# In[88]:


c.conjugate


# In[89]:


type(c)


# In[90]:


True


# In[91]:


False


# In[92]:


t= True
f= False


# In[93]:


t+f


# In[94]:


t-f


# In[95]:


t*f


# In[96]:


t/f


# In[97]:


t//f


# In[98]:


f/t


# In[99]:


f//t


# In[100]:


type(np.nan)


# In[101]:


print(True*2)


# In[102]:


poll_data = 7


# In[103]:


type(poll_data)


# In[104]:


dict(range(9))


# In[105]:


set(range(9))


# In[106]:


list(range(9))


# In[107]:


tuple(range(9))


# In[108]:


obj_data = ()
type(obj_data)


# In[109]:


np.nan


# In[110]:


import sys
import keyword
import operator
from datetime import datetime


# # Keywords

# In[111]:


#keywords are the reserve words in python and can't be used as an identifier


# In[112]:


print(keyword.kwlist)


# In[113]:


len(keyword.kwlist)


# # Identifiers

# In[114]:


#An identifier is a name given to entities like class, functions, variables, etc. 
#it helps to differentiate one entity from another


# In[115]:


1var = 0 #identifier can't start with number


# In[116]:


val2@ =35


# In[117]:


import =125


# In[118]:


'''Correct way of defining an identifier
identifier is a combination of latters in lowercase and uppercase'''
val2=10


# In[120]:


val_=99


# # Comments in Python

# In[121]:


#Single line comment
val1=10


# In[122]:


#Multi
#line
#Comment
val3=10


# In[123]:


'''
Multiple
line
comment'''
val4 = 10


# # Statement

# In[124]:


#Instructions that a Python interpreter can execute


# In[125]:


p = 20
q = 20
r=q
p, type(p), hex(id(p)) , id(p)


# In[126]:


q, type(q), hex(id(q))


# In[127]:


r, type(r), hex(id(r))


# In[128]:


p =20
p = p+10 #Variable Overwriting
p


# # Variable Assignment

# In[129]:


intvar = 10 #Integer variable
floatvar = 2.57 #Float variable
strvar = "Python Language" #String variable
print(intvar)
print(floatvar)
print(strvar)


# # Multiple Assignments

# In[130]:


intvar, floatvar, strvar = 10,2.57,"Python Language" #commas can seperate variables
print(intvar)
print(floatvar)
print(strvar)


# In[131]:


p1 = p2=p3 =p4 =44 #All Variables are pointing to same value
print(p1,p2,p3,p4)


# # Data Types
# Numeric

# In[133]:


var9 = 10.89
print(var9)
print(type(var9)) #Type of object
print(sys.getsizeof(var9)) #size of integer object in bytes
print(var9, "is float?", isinstance(var9,float))


# In[134]:


var9 = 10
print(var9)
print(type(var9)) #Type of object
print(sys.getsizeof(var9)) #size of integer object in bytes
print(var9, "is Integer?", isinstance(var9,int))


# In[135]:


var9 = 10+20j
print(var9)
print(type(var9)) #Type of object
print(sys.getsizeof(var9)) #size of integer object in bytes
print(var9, "is complex?", isinstance(var9,complex))


# In[136]:


sys.getsizeof(int())


# In[137]:


sys.getsizeof(float())


# In[138]:


sys.getsizeof(complex())


# # Boolean
# Boolean data type can have only two possible values true or false

# In[139]:


bool1 = True


# In[140]:


bool2 = False


# In[141]:


print(type(bool1))


# In[142]:


print(type(bool2))


# In[143]:


isinstance(bool1,bool)


# In[144]:


bool(0)


# In[145]:


bool(1)


# In[146]:


bool(None)


# In[147]:


bool(False)


# # Strings
# String Creation

# In[148]:


str1 = "HELLO PYTHON"
print(str1)


# In[149]:


mystr = 'Hello World'  #String using single quotes
print(mystr)


# In[150]:


mystr1 = '''Hello
              World''' #Define string using triple quotes
print(mystr1)


# In[152]:


mystr2 = ('Have a '
         'Greatday ' 
         'Everyone')
print(mystr2)


# In[155]:


str3 = 'Woohoo '
str3 = str3*6
str3


# In[156]:


len(str3)


# # String Indexing
# 

# In[157]:


mystr2


# In[158]:


mystr2[0] #First character in string "str1"


# In[159]:


mystr2[len(mystr2)-1] #Last character in string using len function


# In[161]:


mystr2[-1] #last character in string


# In[163]:


mystr2[8] #Fetch 9th element of string


# # String Slicing

# In[164]:


mystr2[0:5]


# In[165]:


mystr2[6:12]


# In[166]:


mystr2[-6:]


# In[167]:


mystr2[:6]


# In[168]:


mystr2[0:10:2]


# In[169]:


mystr2


# In[170]:


mystr2[::2]


# In[ ]:




