#!/usr/bin/env python
# coding: utf-8

# In[20]:


import matplotlib.pyplot as plt
import numpy as np
import random

rng = np.random.default_rng()
x = rng.normal(size=1000)
x


# In[24]:


plt.hist(x, density=True, bins=100)
plt.xlabel('x')
plt.ylabel('samples')


# In[ ]:





# In[ ]:




