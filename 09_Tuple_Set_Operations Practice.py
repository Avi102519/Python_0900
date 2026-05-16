#!/usr/bin/env python
# coding: utf-8

# In[70]:


t1 = ()


# In[71]:


t2 =(10,20,30)


# In[72]:


t3 = (10.77,30.88,50.99)


# In[73]:


t4 = ('one','two','three')


# In[74]:


t5 = ('Aira',[10,20,30],25,(25,35),(12,26))


# In[75]:


t6 = (100,'Aira','15.678')


# In[76]:


t7 = ('aira',30,[50,100],[150,90],{'john','David'},(99,200))


# # Indexing

# In[77]:


t2[0]


# In[78]:


t5[-1]


# # Slicing

# In[79]:


t = (0,1,2,3,4,5,6,7,8,9)


# In[80]:


t[:3]# returns first 3 vlues


# In[81]:


t[0:8] # returns 0 till 7 th index


# In[82]:


t[:]


# In[83]:


t[::]


# In[84]:


t[-1]


# In[85]:


t[-10:-3]


# In[86]:


t[-3:-7]


# In[87]:


t[9:1]


# In[88]:


del t[0] #deleting one element is not possible in tuple


# In[ ]:


t[0]= 100 #replacing the one element is not possible


# In[ ]:


del t # deleting entire tuple is possible


# # Loop through a tuple

# In[ ]:


t = ('one','two','three','four','five','six','seven','eight','nine','ten')


# In[ ]:


for i in t:
    print(i)


# In[ ]:


for i in enumerate(t):
    print(i)


# In[ ]:


t


# # Membership

# In[ ]:


'one' in t


# In[ ]:


'Eleven' in t


# In[ ]:


if 'four' in t:
    print('Four in tuple')
else:
    print('Four not in tuple')


# In[ ]:


if 'Eleven' in t:
    print('Eleven in tuple')
else:
    print('Eleven not in tuple')


# # Index Position

# In[ ]:


t.index('one')


# In[ ]:


t.index('five')


# In[ ]:


t.index('ten')


# In[ ]:


t10 = (22,88,44,9,100,6,1,33,33)


# In[ ]:


t10.sort()


# In[ ]:


sorted(t10)


# In[ ]:


sorted(t10,reverse= True)


# # Set

# In[ ]:


s = set()


# In[ ]:


type(s)


# In[ ]:


s1= {1,2,3}


# In[ ]:


s1


# In[ ]:


type(s1)


# In[ ]:


s2={100,3,25,76,45,20,50}
s2


# In[ ]:


s3 ={10+15j,9.89,14}
s3


# In[ ]:


print(s)
print(s1)
print(s2)


# In[ ]:


s2.add(35)


# In[ ]:


s2


# In[ ]:


s3 = s2.copy()


# In[ ]:


s3


# In[ ]:


print(s2)
print(s3)


# In[ ]:


s2[2]


# In[ ]:


s2.pop()


# In[ ]:


s2


# In[ ]:


s2.pop()


# In[ ]:


s2


# In[ ]:


s2.remove()


# In[ ]:


s2.remove(100)


# In[ ]:


s2.discard(100)


# In[ ]:


s2


# In[ ]:


s2.remove(45)


# In[ ]:


s2


# In[ ]:


s2.discard(45) #doesn't throughs an error even if it is not in the set


# In[ ]:


s2.remove(45) #throughs an error if the element is not in the set


# In[ ]:


s2


# In[ ]:


s2[2]= 9


# In[89]:


a ={1,2,3,4,5}
b= {4,5,6,7,8}
c= {8,9,10}


# In[90]:


a.union(b)


# In[91]:


a.union(b,c)


# In[92]:


b.union(a,c)


# In[93]:


a|b|c


# In[94]:


c|a|b


# In[95]:


print(a)
print(b)
print(c)


# In[96]:


a.intersection(b)


# In[97]:


a.intersection(c)


# In[98]:


b.intersection(c)


# In[99]:


c.intersection(b)


# In[100]:


a & b


# In[101]:


a&b&c


# In[102]:


# Difference (-)


# In[103]:


a.difference(b)


# In[104]:


b.difference(a)


# In[105]:


a.symmetric_difference(b)


# In[106]:


b^c


# In[107]:


a^b^c


# In[108]:


a.intersection_update(b)


# In[109]:


a


# In[112]:


a1 ={1,2,3,4,5}
b1= {4,5,6,7,8}
c1= {8,9,10}


# In[113]:


a2 ={1,2,3,4,5}
b2= {4,5,6,7,8}
c2= {8,9,10}


# In[114]:


a1.intersection_update(b1)


# In[115]:


a1


# In[116]:


b1.difference_update(c1)


# In[117]:


b1


# In[118]:


b1.symmetric_difference_update(c1)


# In[119]:


b1


# In[120]:


a2 ={1,2,3,4,5}
b2= {4,5,6,7,8}
c2= {8,9,10}


# In[121]:


a2.update(b1)


# In[122]:


a2


# In[124]:


#Superset,subset,disjoint


# ### 

# In[125]:


a3 ={1,2,3,4,5,6,7,8,9}
b3 = {3,4,5,6,7,8}
c3 ={10,20,30,40}


# In[126]:


a3.issuperset(b3)


# In[127]:


a3.isdisjoint(c2)


# In[128]:


a3.isdisjoint(c3)


# In[129]:


a3.isdisjoint(b3)


# In[130]:


b3.issubset(a3)


# In[131]:


b3.isdisjoint(c3)


# In[132]:


a3 ={1,2,3,4,5,6,7,8,9}
b3 = {3,4,5,6,7,8}
c3 ={10,20,30,40}


# In[138]:


#Python
#Copy code
print(type({}))


# In[137]:


dic = {1: 'A', 2: 'E', 3: 'I'}
dic[4] = 'O'
print(dic)


# In[139]:


list1 = ['a', 'b', 'g', 1, 5]


# In[141]:


print(list1.pop())


# In[142]:


list1


# In[143]:


var = 2
print(2 == 2.0)


# In[144]:


num = 4 + 0j
print(type(num))


# In[145]:


a = 'Python' + ".py"
print(a)


# In[146]:


print(str(True), end=" ")
int("4.5")


# In[147]:


set1 = {1, 5, 6, 4, 3}
print(set1)


# In[153]:


x = 50
def fun1():
    x = 25
    print(x)
fun1()
print(x)


# In[154]:


x = 75
def myfunc():
    x = x + 1
    print(x)
myfunc()
print(x)


# In[155]:


print(type(0xFF))


# In[156]:


str1 = 'Ault\'Kelly'


# In[157]:


str1


# In[158]:


str1 = 'Ault\\'Kelly'
str1


# In[159]:


str1 = """Ault'Kelly"""
str1


# In[160]:


aTuple = (1, 'Jhon', 1+3j)
print(type(aTuple[2:3]))


# In[161]:


print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))


# In[164]:


def func1():
    a = 50
    return a
func1()
print(a)


# In[165]:


print(type({}) 


# In[166]:


type(range(5))


# In[167]:


print(type(10))


# In[168]:


x = "Hello"
print(type(x))


# In[169]:


x = 3.14
print(type(x))


# In[170]:


str1 = '''str'''


# In[171]:


str1


# In[172]:


str1 = 'str1'


# In[173]:


str1


# In[174]:


str1 = "str1"


# In[175]:


str1 = 'str1'


# In[176]:


print(type(10))


# In[177]:


x = "Hello"
print(type(x))


# In[178]:


x = 3.14
print(type(x))


# In[179]:


x = 10
y = "20"
print(x + int(y))


# In[180]:


x = {"apple", "banana", "cherry"}
print(type(x))


# In[181]:


x = {"name": "John", "age": 30}
print(type(x))


# In[182]:


x = True
type(x)


# In[183]:


x = [1, 2, 3]
print(type(x))


# In[ ]:




