#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import matplotlib.pyplot as plt
import random
x = np.random.random((1000,1))
print(x)


# In[10]:


plt.hist(x, density=True, bins=100)
plt.xlabel('random number')
plt.ylabel('sample')


# In[ ]:




