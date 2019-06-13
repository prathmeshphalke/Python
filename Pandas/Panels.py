#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pandas_datareader import data


# In[3]:


companies = ["MSFT", "GOOG", "AAPL", "YHOO", "AMZN"]

p = data.DataReader(name = companies, data_source = "google", start = "2010-01-01", end = "2016-12-31")

p


# ## The Axes of the Panel

# In[7]:


companies = ["MSFT", "GOOG", "AAPL", "YHOO", "AMZN"]

p = data.DataReader(name = companies, data_source = "google", start = "2010-01-01", end = "2016-12-31")

p


# In[9]:


p.items


# In[10]:


p.major_axis


# In[11]:


p.minor_axis


# In[12]:


p.axes


# ## Panel Attributes

# In[31]:


companies = ["MSFT", "GOOG", "AAPL", "YHOO", "AMZN"]

p = data.DataReader(name = companies, data_source = "google", start = "2010-01-01", end = "2016-12-31")

p


# In[35]:


p.axes
p.items
p.major_axis
p.minor_axis


# In[36]:


p.ndim


# In[37]:


p.dtypes


# In[38]:


p.shape


# In[39]:


p.size


# In[40]:


5 * 1688 * 5


# ## Extracting `DataFrames` from a `Panel` Using Bracket Notation

# In[42]:


companies = ["MSFT", "GOOG", "AAPL", "YHOO", "AMZN"]

p = data.DataReader(name = companies, data_source = "google", start = "2010-01-01", end = "2016-12-31")

p


# In[43]:


p.items


# In[46]:


p["Volume"]


# ## Extracting with the `.loc[]`, `.iloc[]`, and `.ix[]` Methods

# In[47]:


companies = ["MSFT", "GOOG", "AAPL", "YHOO", "AMZN"]

p = data.DataReader(name = companies, data_source = "google", start = "2010-01-01", end = "2016-12-31")

p


# In[48]:


p.items


# In[52]:


p.loc["Low", "2014-04-08", "GOOG"]


# In[55]:


p.iloc[3, 200, 3]


# In[59]:


p.ix["High", 500, 4]


# ## Convert `Panel` to a `MultiIndex DataFrame` (and Vice Versa)

# In[66]:


companies = ["MSFT", "GOOG", "AAPL", "YHOO", "AMZN"]

p = data.DataReader(name = companies, data_source = "google", start = "2010-01-01", end = "2016-12-31")

p


# In[68]:


df = p.to_frame()
df.head()


# In[70]:


p2 = df.to_panel()
p2


# ## The `.major_xs()` Method

# In[82]:


companies = ["MSFT", "GOOG", "AAPL", "YHOO", "AMZN"]

p = data.DataReader(name = companies, data_source = "google", start = "2010-01-01", end = "2016-12-31")

p


# In[84]:


p.items
p["Volume"]


# In[85]:


p.major_axis


# In[88]:


p.major_xs("2013-12-20")


# ## The `.minor_xs()` Method

# In[89]:


companies = ["MSFT", "GOOG", "AAPL", "YHOO", "AMZN"]

p = data.DataReader(name = companies, data_source = "google", start = "2010-01-01", end = "2016-12-31")

p


# In[90]:


p.minor_axis


# In[95]:


p.minor_xs("MSFT")
p.minor_xs("GOOG").head(3)


# In[96]:


p


# In[102]:


p.items
p.major_axis
p.minor_axis


# In[99]:


p["Open"]
p.major_xs("2016-09-16")
p.minor_xs("YHOO")


# ## Transpose a `Panel` with the `.transpose()` Method

# In[12]:


companies = ["MSFT", "GOOG", "AAPL", "YHOO", "AMZN"]

p = data.DataReader(name = companies, data_source = "google", start = "2010-01-01", end = "2016-12-31")

p


# In[13]:


p.axes


# In[15]:


p2 = p.transpose(2, 1, 0)


# In[16]:


p


# In[19]:


p2["GOOG"]


# In[20]:


p2.major_xs("2010-01-04")


# In[21]:


p2.minor_xs("Volume")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## The `.swapaxes()` Method

# In[115]:


companies = ["MSFT", "GOOG", "AAPL", "YHOO", "AMZN"]

p = data.DataReader(name = companies, data_source = "google", start = "2010-01-01", end = "2016-12-31")

p


# In[117]:


p2 = p.swapaxes("items", "minor")


# In[118]:


p2.axes


# In[121]:


p2["MSFT"]
p2.major_xs("2016-09-02")
p2.minor_xs("Close")


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





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




