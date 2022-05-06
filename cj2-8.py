#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,1,100)
print(x)


# In[3]:


y = np.sin(x)
print(y)
z = np.cos(x)
print(z)


# In[9]:


fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(x,y)
ax1.set_title('sin(x)')
ax2.plot(x,z)
ax2.set_title('cos(x)')
plt.show()


# In[ ]:




