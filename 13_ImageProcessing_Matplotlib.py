#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[ ]:


#pip install --upgrade matplotlib


# In[2]:


import matplotlib.pyplot as plt # Library for Visualizations


# In[3]:


from PIL import Image # Python Imaging Library


# In[4]:


img = Image.open(r'/Users/aviswe/Desktop/830/Datasets/Shoes.jpg')


# In[5]:


img


# In[6]:


type(img)


# In[8]:


img_arr = np.asarray(img)
img_arr


# In[9]:


img_arr.shape


# In[10]:


plt.imshow(img)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




