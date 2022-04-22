#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np

def my_function():
    print(np.sin(x))
    print(np.cos(x))


# This function returns sin(x) and cos(x), where x is between 0 and 2pi. 

# In[5]:


x = np.linspace(0, 2 * np.pi, 1000)
my_function()


# In[13]:


for i in x:
    print(i)
for i in np.sin(x):
    print(i)
for i in np.cos(x):
    print(i)


# In[ ]:




