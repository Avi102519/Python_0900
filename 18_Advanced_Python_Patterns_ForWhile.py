#!/usr/bin/env python
# coding: utf-8

# - if
# - else
# - if else
# - nested if
# - if elif else

# In[1]:


# Check if the number if even or not
x=4
r=x%2
if r==0:
    print('Even Number')    


# In[2]:


x=4
r=x%2
if r==0:
print('Even Number')


# In[3]:


#indentation can be atleast one space for print statement
x=4
r=x%2
if r==0:
 print('Even Number')


# In[4]:


# if the condition not match then no output will be displayed
x=5
r=x%2
if r == 0:
    print('Even Number')


# In[5]:


#condition is not met however the code prints the last statement
x = 5
r=x%2
if r==0:
    print('Even Number')
print('Odd Number')


# In[6]:


x=8
r=x%2
if r == 0:
 print('Even Number')
print('Odd Number')


# In[7]:


#Two if conditions will be executed no matter with the conditional value
x= 9
r=x%2
if r == 0:
    print('Even Number')
if r != 0:
    print('Odd Number')


# In[8]:


# if else condition
x= 9
r= x%2
if r==0:
    print('Even Number')
else:
    print('Odd Number')


# In[9]:


x=8
r=x%2
if r==0:
    print('Even Number')
else:
    print('Odd Number')


# In[10]:


#Nested if
x= 3
r=x%2
if r==0:
    print('Even number')
    
    if x>5:
        print('Greater than number 5')
else:
    print('Odd Number')


# In[11]:


x = 4
r = x%2
if r == 0:
    print('Even Number')
    
    if x>5:
        print('Greater than number 5')
else:
    print('Odd Number')


# In[12]:


x= 4
r=x%2
if r==0:
    print('Even Number')
    if x>5:
        print('Greater than number 5')
    else:
        print('Smaller than number 5')
else:
    print('Odd Number')


# In[13]:


x = 1
if x==1:
    print('one')
if x==2:
    print('Two')
if x==3:
    print('Three')
if x==4:
    print('Four')


# In[14]:


x=1
if x==1:
    print('One')
elif x==2:
    print('Two')
elif x==3:
    print('Three')
elif x==4:
    print('Four')


# In[16]:


x=10
if x==1:
    print('One')
elif x==2:
    print('Two')
elif x==3:
    print('Three')
elif x==4:
    print('Four')

else:
    print('Number not found')


# # Loops

# In[17]:


i = 1
while i<=5:
    print('Data Science')
    i= i+1


# In[19]:


i = 1
while i<=5:
    print('data science',i)
    i= i+1


# In[20]:


i = 5
while i>=1:
    print('data science')
    i = i-1


# In[21]:


i = 5
while i>=1:
    print('data science',i)
    i= i-1


# In[23]:


i = 1
while i<=5:
    print('data science')
    j=1
    while j<=4:
        print('technology')
        j=j+1
    i=i+1
    print()
        


# In[1]:


i = 1
while i<=2:
    j=0
    while j<=2:
        print(i*j, end = " ")
        j+=1
    print()
    i+=1


# In[2]:


i = 1
while i<=4:
    j=0
    while j<=3:
        print(i*j, end = " ")
        j+=1
    print()
    i+=1


# In[3]:


name= 'nit'
print(type(name))


# In[4]:


for i in name:
    print(i)


# In[5]:


l = [1,2,3,4]


# In[6]:


for i in l:
   print(i) 


# In[7]:


for i in range(2,5):
    print(i)


# In[7]:


# 5 table
j = 12
for i in range(1,11):
    print(j, '*',i,'=', i*j)


# In[8]:


#Generic table generation code
j= int(input('enter your table number'))
for i in range(1,11):
    print(j, '*',i,'=', i*j)
    


# In[10]:


#Nested while with 'end' function at the print 
i = 1
while i<= 2:
    j= 0
    while j<=2:
        print(i*j,end=' ')
        j+=1
    print()
    i+=1


# In[11]:


#Nested while with no 'end' function at the print
i = 1
while i <=4:
    j = 0
    while j<=3:
        print(i*j, ' ')
        j+=1
    print()
    i+=1


# In[12]:


# While loop works with iteration ot certation.
# For loop works work with sequence or list.


# In[14]:


name = 'nit'
for i in name:
    print (i)


# In[15]:


name1 = [1,2,3,'nit']
for i in name1:
    print(i)


# In[16]:


name2 = [1,2,3,4.5,'Hi']
for i in name2:
    print(i)


# In[17]:


for i in range(5):
    print(i)


# In[18]:


for i in range(2,5):
    print(i)


# In[19]:


for i in range(1,10,3):
    print(i)


# In[20]:


for i in range(1,21):
    print(i)


# In[21]:


#for loop with if condition
for i in range(1,51):
    if i %5 ==0:
        print(i)


# In[22]:


for i in range(1,51):
    if i %3==0:
        print(i)


# #LETS DISCUSS ABOUT 3 KEYWORDS -- BREAK || CONTINUE || PASS
# #BREAK STATEMNT - if you apply break statment in a loop then it will end the loop
# #Pass = skips block of code( function, class etc)
# #Continue= skips 1 step/iteration during loop 
# #Break= jumps out of the function/loop

# In[25]:


#Write a code to chocolate vending machine
x= int(input('How many chocolates you want:'))
i =1
while i<=x:
    print('Chocolate')
    i+=1


# - If the user wants 10 choclet but vending machine has only 5 choclate so what you do on those scenario
# - Below are the 3 options
# - 1. stop the transaction by you
# - 2. You can give only 5 choclates
# - 3. Vending machine display the result as we are out of the stock
# - Now lets try in the code

# In[26]:


ava = 5 #the machine has only 5 chocolates
x = int(input('How many chocolates you want:?'))
i =1
while i<x:
    print('chocolate')
    i+=1


# In[28]:


ava_cho = 5
x= int(input('How many chocolates you want'))
i = 1
while i<=x:
    if i>ava_cho:
        break
    print('Chocolate')
    i+=1
print('Bye for now')    


# In[29]:


ava_cho = 5
x= int(input('How many chocolates you want'))
i = 1
while i<=x:
    if i>ava_cho:
        print('out of stock')
        break
    print('Chocolate')
    i+=1
print('Bye for now')   


# In[30]:


for i in range(1,11):
    print(i)


# In[31]:


#if i want only 5 numbers with a range of 11
for i in range(1,11):
    if i ==6:
        break
    print(i)


# In[32]:


#conitnue dont print on if condition
for i in range(1,11):
    if i == 3:
        continue
    print(i)


# In[33]:


for i in range(1,11):
    if i ==3:
        continue
    print('hello:',i)


# In[34]:


# Pass statement- pass the code if error is expected
for i in range(1,11)


# In[35]:


for i in range(1,11):
    pass


# # you need to print the number from 1 to 50 but dont print the number which is divisible by 3 or 5 

# In[36]:


for i in range(1,51):
    if i%3 ==0:
        print(i)
print('end')


# In[37]:


for i in range(1,51):
    if i %3 ==0:
        continue
    print(i)
print('end')


# In[38]:


for i in range(1,51):
    if i%3==0 or i%5 ==0: 
        continue # this continue skips the numbers divisible by 3 or 5
    print(i)


# In[39]:


for i in range(1,51):
    if i%3==0 and i%5 ==0:
        continue
    print(i)


# In[40]:


for i in range(1,50):
    if i%3 == 0 or i%5 == 0:
        continue
    print(i)
print('end') 


# In[41]:


for i in range(1,51):
    if (i%2 ==0):
        continue
    else:
        print(i)
print('bye')


# In[43]:


print('# # # #')
print('# # # #')
print('# # # #')
print('# # # #')


# In[44]:


for i in range(1,5):
    i =i+1
    print(' # # # # ')


# In[45]:


for i in range(1,5):
    if i<=5:
        print(' # # # # ')


# In[46]:


for j in range(4):
    print('#')


# In[47]:


for j in range(4):
    print(' # # # # ')


# In[49]:


for j in range(4):
    print('#',end =" ")


# In[50]:


for j in range(4):
    print('#',end =" ")
for j in range(4):
    print('#',end =" ")


# In[51]:


for j in range(4):
    print('#',end =" ")
print()
for j in range(4):
    print('#',end =" ")


# In[52]:


for j in range(4):
    print('#',end =" ")
print()
for j in range(4):
    print('#',end =" ")
print()
for j in range(4):
    print('#',end =" ")
print()
for j in range(4):
    print('#',end =" ")


# In[53]:


for i in range(4):
    for j in range(4):
        print('#',end=" ")
    print()


# In[54]:


for i in range(4):
    for j in range(i+1):
        print('#', end= " ")
    print()


# In[55]:


for i in range(1,5):
    print("#"*i)


# In[57]:


for i in range(1,5):
    for j in range(4):
        if i>j:
            print("#",end=" ")
    print()


# In[58]:


list[int](range(5))


# In[59]:


for i in range(4):
    for i in range(i):
        print('#', end=" ")
    print()


# In[60]:


for i in range(4):
    for j in range(i+1):
        print('#', end="  ")
    print()


# In[61]:


for i in range(4):
    for j in range(4-i):
        print('#', end="  ")
    print()


# In[62]:


for i in range(1,5):
    print("# "*(5-i))


# - For|Else in python
# - In other language for else not supportable but in python it is supportable
# 
# eg- lets print the number from 1- 20 & we dont want print number which is divisible by 5

# In[63]:


nums = [12,15,18,21,26,30,40]

for num in nums:
    if num % 5 == 0:
        print(num) 


# In[64]:


nums = [12,14,18,21,25,30,35]

for num in nums:
    if num % 5 == 0:
        print(num)  


# In[65]:


nums = [12,14,18,21,25,20]

for num in nums:
    if num % 5 == 0:
        print(num)  


# In[66]:


nums = [12,14,18,21,20,25]

for num in nums:
    if num % 5 == 0:
        print(num)  
        break


# In[67]:


nums = [12,14,18,21,20,25]

for num in nums:
    if num % 5 == 0:
        print(num)  
        break


# In[68]:


nums = [10,14,18,21,5,10]

for num in nums:
    if num % 5 == 0:
        print(num)  
        break 


# In[69]:


nums = [7,14,18,21,23,27] #hear there is no number which is divisible by 5 we got output as blank

for num in nums:
    if num % 5 == 0:
        print(num)  
        break


# In[70]:


nums = [7,14,18,21,23,27,29] #hear there is no number which is divisible by 5 we got output as blank

for num in nums:
    if num % 5 == 0:
        print(num)  
        break
    else:
        print('Number Not Found') 


# In[71]:


nums = [7,14] #hear there is no number which is divisible by 5 we got output as blank
for num in nums:
    if num % 5 == 0:
        print(num)  
        break
    else:
        print('Number Not Found') 


# In[72]:


nums = [7,14,18,21,23,27] #hear there is no number which is divisible by 5 we got output as blank

for num in nums:
    if num % 5 == 0:
        print(num)  
        break
else:
        print('Number Not Found') 


# In[73]:


nums = [10,14,18,21,20,27,30] #hear there is no number which is divisible by 5 we got output as blank

for num in nums:
    if num % 5 == 0:
        print(num)  
        #break
else:
        print('Not Found')


# In[74]:


nums = [10,14,18,21,20,27] #hear there is no number which is divisible by 5 we got output as blank
for num in nums:
    if num % 5 == 0:
        print(num)  
        break
else:
        print('Not Found')


# - prime number - how to check given number is prime number or not(7,13,19)

# In[76]:


num = 14

for i in range(2,num):
    if num % i == 0:
        print('Not prime Number')
        break
else:
    print('Prime Number')


# In[77]:


num = 13

for i in range(2,num):
    if num % i == 0:
        print('Not prime Number')
        break
else:
    print('Prime Number')


# In[ ]:




