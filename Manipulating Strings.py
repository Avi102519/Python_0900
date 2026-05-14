#!/usr/bin/env python
# coding: utf-8

# # Manipulating Strings
# Escape Characters
# An escape character is created by typing a backslash'\' followed by the character you want to insert.
# 
# '\' --Single quote
# "\"--Double quote
# '\t'--Tab
# '\n'--Newline(line break)
# '\\'--Backslash
# '\b'--Backspace
# '\ooo'--Octal Value
# '\r'--Carriage Return

# In[1]:


print("Hello there!\nHow are you?\nI\'m doing fine.")


# # Raw strings
# a raw string entirely ignores all escape characters and prints any backslash that appears in the string.

# In[2]:


print(r"Hello there!\nHow are you?\nI\'m doing fine.")


# Raw strings are mostly used for regular expression definition.

# # Multiline Strings

# In[5]:


print(
"""Dear Aira

Swe's cat has been arrested for catnapping,
cat burglary, and extortion.

Sincerely
AV""") 


# # Indexing and Slicing strings
# H e l l o   W o r l d  !
# 0 1 2 3 4 5 6 7 8 9 10 11

# Indexing

# In[6]:


i = 'Hello World!'
i[0]


# In[7]:


i[4]


# In[8]:


i[-1]


# # Slicing

# In[9]:


i[0:5]


# In[10]:


i[:5]


# In[11]:


i[6:-1]


# In[12]:


i[11:2]


# In[13]:


i[11:-1]


# In[14]:


i[11:-9]


# In[15]:


i[-12:-9]


# In[16]:


i[-9:-12]


# In[17]:


i[6:9]


# In[18]:


i[2:-2]


# In[19]:


i[:-1]


# In[20]:


i[::-1]


# In[21]:


m = i[0:5]
m


# # The in and not in operations

# In[22]:


'Hello' in 'Hello World'


# In[23]:


'Hello' in 'Hello'


# In[24]:


'HELLO' in 'HELLO world'


# In[25]:


'Hello' in 'HELLO'


# In[26]:


'' in 'i'


# In[27]:


'cats' not in 'cats and dogs'


# # Upper(), Lower() and title()
# Transforms a string to upper, lower and title case:

# In[28]:


a = 'Hello world!'
a.upper()


# In[29]:


a.lower()


# In[30]:


a.title()


# In[31]:


b= a.lower()
b


# In[32]:


b.title()


# # isupper() and islower() methods
# Returns 'True' or 'False' after evaluating if a string is in upper or lower case:

# In[33]:


i='Hello world!'
i.islower()


# In[34]:


i.isupper()


# In[35]:


'HELLO'.isupper()


# In[36]:


'abc12345'.islower()


# In[37]:


'12345'.islower()


# In[38]:


'12345'.isupper()


# # The is X string methods
# Method      Description
# isalpha()---returns 'True' if the string consists only of letters.
# isalnum()---returns 'True' if the string consists only of letters and numbers.
# isdecimal()-returns 'True' if the string consists only of numbers
# isspace()---returns 'True' if the string consists only spaces, tabs, and new-lines
# istitle()---returns `True` if the string consists only of words that begin with an
# uppercase letter followed by only lowercase characters.

# # startswith() and endswith()

# In[39]:


'Hello world!'.startswith('Hello')


# In[40]:


'Hello world'.endswith('Hello')


# In[41]:


'abc123'.startswith('abcdef')


# In[42]:


'abc123'.endswith('12')


# In[43]:


'Hello world!'.startswith('Hello world!')


# In[44]:


'Hello world!'.endswith('Hello world!')


# # Join() and split()
# join()
# The `join()` method takes all the items in an iterable, like a list, dictionary, tuple or set,
# and joins them into a string. You can also specify a separator.

# In[51]:


','.join(['My','is'])


# In[50]:


''.join(['My''MynameisSimon','name','is','Simon'])


# In[52]:


','.join(['my','name','is','Aira'])


# In[53]:


', '.join(['cats', 'rats', 'bats'])


# In[54]:


' '.join(['cats','rats','bats'])


# In[55]:


'Aira'.join(['I Love','.','is beautiful'])


# # Split()
# The split method splits a string into a list. By default it seperate the items with whitespace,but user can 
# select a character of choice

# In[56]:


'My name is Aira'.split()


# In[57]:


'I LoveAira.Airais beautiful'.split('Aira')


# In[58]:


'My name is Simon'.split('m')


# In[59]:


'My name is Simon'.split(' ')


# # Justifying text with rjust().ljust() and center()
# an optional second argument to rjust() and ljust() will specify a fill character apart from a space character

# In[60]:


'Hello'.rjust(10)


# In[61]:


'Hello'.ljust(10)


# In[62]:


'Hello'.center(20)


# In[63]:


'Hello'.rjust(20,*)


# In[64]:


'Hello'.rjust(20,'*')


# In[65]:


'Hello'.rjust(10,'&')


# In[66]:


'Hello'.center(10,'@')


# # Removing whitespace with strip(),rstrip() and lstrip()

# In[67]:


k = '     Hello World!       '
k.strip()


# In[68]:


k.lstrip()


# In[69]:


k.rstrip()


# In[70]:


p = 'SpamSpamBaconSpamEggsSpamSpam'
p.strip('amSp')


# # The Count Method
# Counts the number of occurrences of a given character or substring in the string it is
# applied to. Can be optionally provided start and end index.

# In[71]:


S = 'One Aira only Aira, Smart Aira, Great Aira. Caring Aira'
s.count('Aira')


# In[72]:


S.count('Aira')


# In[73]:


S.count('a')


# In[74]:


S.replace('A','a')


# In[75]:


S.count('a')


# In[76]:


S


# In[77]:


S1 = S.replace('A','a')


# In[78]:


S1.count('a')


# In[79]:


S.count('a',6) # returns count of e after 'one sh' i.e 6 chars since beginning of string


# In[80]:


S.count('a',7) 


# # Replace Method
# Replaces all occurances of a given substring with another substring. Can be optionally provided a third argument to limit the number of replacements. Returns a new string.

# In[81]:


S1.replace("aira","Swe")


# In[82]:


S1


# In[83]:


S2 = S1.replace('aira',"swe",1)


# In[84]:


S2


# In[85]:


S3 = "I like apples, Apples are my favorite fruit"
S3.replace("apples","Oranges")


# In[ ]:




