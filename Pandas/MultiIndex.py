#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


bigmac = pd.read_csv("bigmac.csv", parse_dates = ["Date"])
bigmac.head(3)


# ## Create A MultiIndex with the `.set_index()` Method

# In[8]:


bigmac = pd.read_csv("bigmac.csv", parse_dates = ["Date"])
bigmac.head(3)


# In[14]:


bigmac.set_index(keys = ["Date", "Country"], inplace = True)
bigmac.head(3)


# In[16]:


bigmac.sort_index(inplace = True)


# In[17]:


bigmac.head(3)


# In[19]:


bigmac.index.names


# In[21]:


type(bigmac.index)


# In[23]:


bigmac.index[0]


# ## The `.get_level_values()` Method

# In[21]:


bigmac = pd.read_csv("bigmac.csv", parse_dates = ["Date"], index_col = ["Date", "Country"])
bigmac.sort_index(inplace = True)
bigmac.head(3)


# In[26]:


bigmac.index.get_level_values(0)
bigmac.index.get_level_values("Date")


# In[28]:


#bigmac.index.get_level_values(1)
bigmac.index.get_level_values("Country")


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





# ## The `.set_names()` Method on MultiIndex

# In[15]:


bigmac = pd.read_csv("bigmac.csv", parse_dates = ["Date"], index_col = ["Date", "Country"])
bigmac.sort_index(inplace = True)
bigmac.head(3)


# In[20]:


bigmac.index.set_names(["Date", "Location"], inplace = True)


# In[21]:


bigmac.head(3)


# ## Extract Rows from a `MultiIndex DataFrame`

# In[11]:


bigmac = pd.read_csv("bigmac.csv", parse_dates = ["Date"], index_col = ["Date", "Country"])
bigmac.sort_index(inplace = True)
bigmac.head(3)


# In[14]:


bigmac.loc[("2010-01-01", "Brazil"), "Price in US Dollars"]


# In[17]:


bigmac.loc[("2015-07-01", "Chile"), "Price in US Dollars"]


# In[26]:


bigmac.ix[("2016-01-01", "China"), 0]


# ## The `.transpose()` Method

# In[27]:


bigmac = pd.read_csv("bigmac.csv", parse_dates = ["Date"], index_col = ["Date", "Country"])
bigmac.sort_index(inplace = True)
bigmac.head(3)


# In[29]:


bigmac = bigmac.transpose()
bigmac.head(1)


# In[32]:


bigmac.ix["Price in US Dollars", ("2016-01-01", "Denmark")]


# ## The `.swaplevel()` Method

# In[33]:


bigmac = pd.read_csv("bigmac.csv", parse_dates = ["Date"], index_col = ["Date", "Country"])
bigmac.sort_index(inplace = True)
bigmac.head(3)


# In[35]:


bigmac = bigmac.swaplevel()
bigmac.head(3)


# ## The `.sort_index()` Method on a MultiIndex `DataFrame`

# In[24]:


bigmac = pd.read_csv("bigmac.csv", parse_dates = ["Date"], index_col = ["Date", "Country"])
bigmac.sort_index(inplace = True)
bigmac.head(3)


# In[28]:


bigmac.sort_index(ascending = [True, False], inplace = True)


# In[29]:


bigmac.head(3)


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





# ## The `pivot` Method

# In[8]:


sales = pd.read_csv("salesmen.csv", parse_dates = ["Date"])
sales["Salesman"] = sales["Salesman"].astype("category")
sales.head(3)


# ## The `.stack()` Method

# In[22]:


world = pd.read_csv("worldstats.csv", index_col = ["country", "year"])
world.head(3)


# In[26]:


world.stack().to_frame()


# ## The `.unstack()` Method, Part 3

# In[50]:


world = pd.read_csv("worldstats.csv", index_col = ["country", "year"])
s = world.stack()
s.head(3)


# In[54]:


s.unstack(level = ["year", "country"])


# In[57]:


s = s.unstack("year", fill_value = 0)


# In[58]:


s.head()


# ## The `pivot_table()` Method

# In[62]:


foods =pd.read_csv("foods.csv")
foods.head(3)


# In[75]:


foods.pivot_table(values = "Spend", index = ["Gender", "Item"], columns = "City", aggfunc = "min").head(3)


# In[76]:


pd.pivot_table(data = foods, values = "Spend", index = ["Gender", "Item"], columns = "City", aggfunc = "min").head(3)


# ## The `pd.melt()` Method

# In[79]:


sales = pd.read_csv("quarters.csv")
sales


# In[82]:


pd.melt(sales, id_vars = "Salesman", var_name = "Quarter", value_name = "Revenue")


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




