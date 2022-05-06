#!/usr/bin/env python
# coding: utf-8

# In[16]:


import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,1,100)
print(x)


# In[17]:


y = np.exp(x)
print(y)


# In[23]:


plt.plot(x,y)
plt.xlabel('Time [milliseconds]')
plt.ylabel('Awesomeness')
plt.show()


# In[ ]:




