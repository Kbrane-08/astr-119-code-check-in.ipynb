#!/usr/bin/env python
# coding: utf-8

# Import numpy and matplotlib.pyplot as usual

# In[34]:


import numpy as np
import matplotlib.pyplot as plt


# Declare integer i, set equal to zero. Declare a float x, set equal to 119

# In[35]:


i = 0
x = 119


#  Use a for loop, iterate i from 0 to 119 inclusive. For each even value (including 0) of i, add 3 to x. For each odd value of i, subtract 5 from x

# In[ ]:


for i in range(120):
    # adding x with 3 if i is even
    if i%2 == 0:
      x = x + 3
    # else subtracting 5 from x
    else:
      x = x - 5


# Print the final value of x in scientific notation using 2 decimal places

# In[36]:


print(f"{x:.2E}")

