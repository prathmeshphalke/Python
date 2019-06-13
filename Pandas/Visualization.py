#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from pandas_datareader import data

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# ## The `.plot() ` Method

# In[3]:


bb = data.DataReader(name = "BBRY", data_source = "google", start = "2007-07-01", end = "2008-12-31")
bb.head(3)


# In[11]:


bb[["High", "Low"]].plot()


# ## Modifying Aesthetics

# In[12]:


bb = data.DataReader(name = "BBRY", data_source = "google", start = "2007-07-01", end = "2008-12-31")
bb.head(3)


# In[13]:


plt.style.available


# In[15]:


plt.style.use("fivethirtyeight")
bb.plot(y = "Close")


# In[16]:


plt.style.use("dark_background")
bb.plot(y = "Close")


# In[17]:


plt.style.use("ggplot")
bb.plot(y = "Close")


# ## Bar Charts

# In[18]:


google = data.DataReader(name = "GOOG", data_source = "google", start = "2004-01-01", end = "2016-12-31")
google.head(3)


# In[19]:


def rank_performance(stock_price):
    if stock_price <= 200:
        return "Poor"
    elif stock_price > 200 and stock_price <= 500:
        return "Satisfactory"
    else:
        return "Stellar"


# In[27]:


plt.style.use("ggplot")
google["Close"].apply(rank_performance).value_counts().plot(kind = "barh")


# ## Pie Charts

# In[28]:


apple = data.DataReader(name = "AAPL", data_source = "google", start = "2012-01-01", end = "2016-12-31")
apple.head(3)


# In[30]:


apple["Close"].mean()


# In[31]:


def rank_performance(stock_price):
    if stock_price >= 92.63809405940599:
        return "Above Average"
    else:
        return "Below Average"


# In[36]:


plt.style.use("ggplot")
apple["Close"].apply(rank_performance).value_counts().plot(kind = "pie", legend = True)


# ## Histograms

# In[93]:


google = data.DataReader(name = "GOOG", data_source = "google", start = "2004-01-01", end = "2016-12-31")
google.head(3)


# In[94]:


def custom_round(stock_price):
    return int(stock_price / 100.0) * 100


# In[101]:


google["High"].apply(custom_round).value_counts().sort_index()


# In[103]:


google["High"].apply(custom_round).nunique()


# In[107]:


google["High"].apply(custom_round).plot(kind = "hist", bins = 9)


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




