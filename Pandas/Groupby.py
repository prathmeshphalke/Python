#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[6]:


fortune = pd.read_csv("fortune1000.csv", index_col = "Rank")
sectors = fortune.groupby("Sector")
fortune.head(3)


# In[7]:


type(sectors)


# ## The `.groupby()` Method

# In[8]:


fortune = pd.read_csv("fortune1000.csv", index_col = "Rank")
sectors = fortune.groupby("Sector")
fortune.head(3)


# ## Retrieve A Group with the `.get_group()` Method

# In[39]:


fortune = pd.read_csv("fortune1000.csv", index_col = "Rank")
sectors = fortune.groupby("Sector")
fortune.head(3)


# ## Methods on the Groupby Object and `DataFrame` Columns

# In[51]:


fortune = pd.read_csv("fortune1000.csv", index_col = "Rank")
sectors = fortune.groupby("Sector")
fortune.head(3)


# In[58]:


sectors.get_group("Apparel")["Profits"].sum()


# In[59]:


sectors.max()
sectors.min()
sectors.sum()
sectors.mean()


# In[67]:


sectors["Revenue"].sum()
sectors["Employees"].sum()
sectors["Profits"].max()
sectors["Profits"].min()
sectors["Employees"].mean()

sectors[["Revenue", "Profits"]].sum()


# ## Grouping by Multiple Columns

# In[69]:


fortune = pd.read_csv("fortune1000.csv", index_col = "Rank")
sectors = fortune.groupby(["Sector", "Industry"])
fortune.head(3)


# In[73]:


sectors.size()
sectors.sum()
sectors["Revenue"].sum()
sectors["Employees"].mean()


# ## The `.agg()` Method

# In[78]:


fortune = pd.read_csv("fortune1000.csv", index_col = "Rank")
sectors = fortune.groupby("Sector")
fortune.head(3)


# In[80]:


sectors["Employees"].mean()


# In[83]:


sectors.agg({"Revenue" : ["sum", "mean"],
             "Profits" : "sum",
              "Employees" : "mean"})


# In[82]:


sectors.agg(["size", "sum", "mean"])


# ## Iterating through Groups

# In[84]:


fortune = pd.read_csv("fortune1000.csv", index_col = "Rank")
sectors = fortune.groupby("Sector")
fortune.head(3)


# In[86]:


df = pd.DataFrame(columns = fortune.columns)
df


# In[87]:


for sector, data in sectors:
    highest_revenue_company_in_group = data.nlargest(1, "Revenue")
    df = df.append(highest_revenue_company_in_group)


# In[88]:


df


# In[89]:


cities = fortune.groupby("Location")
df = pd.DataFrame(columns = fortune.columns)
df


# In[90]:


for city, data in cities:
    highest_revenue_in_city = data.nlargest(1, "Revenue")
    df = df.append(highest_revenue_in_city)


# In[91]:


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





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




