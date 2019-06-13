#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# ## Changing Options with Attributes and Dot Syntax

# In[34]:


data = np.random.randint(0, 100, [1000, 50])
df = pd.DataFrame(data)
df.tail(2)


# In[35]:


pd.options.display.max_rows = 4


# In[36]:


pd.options.display.max_columns = 8


# In[37]:


df


# ## Changing `pandas` Options with Methods

# In[42]:


data = np.random.randint(0, 100, [1000, 50])
df = pd.DataFrame(data)
df.tail(2)


# In[43]:


pd.get_option("max_rows")


# In[44]:


pd.get_option("max_columns")


# In[47]:


pd.set_option("max_columns", 20)


# In[50]:


pd.options.display.max_columns = 10


# In[52]:


pd.get_option("mAX_columns")


# In[55]:


pd.reset_option("max_columns")


# In[56]:


pd.get_option("max_columns")


# In[57]:


pd.describe_option("max_columns")


# ## The `precision` Option

# In[58]:


df = pd.DataFrame(np.random.randn(5, 5))
df


# In[59]:


pd.get_option("precision")


# In[60]:


pd.set_option("precision", 2)


# In[63]:


df


# In[62]:


pd.reset_option("precision")


# ## The `chop_threshold()` Option

# In[66]:


df = pd.DataFrame(np.random.randn(10, 10))
df


# In[69]:


pd.set_option("chop_threshold", 1)


# In[71]:


pd.reset_option("chop_threshold")


# In[72]:


df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




