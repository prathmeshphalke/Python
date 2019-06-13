#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[21]:


df = pd.read_csv("employees.csv", parse_dates = ["Start Date", "Last Login Time"])
df["Senior Management"] = df["Senior Management"].astype("bool")
df["Gender"] = df["Gender"].astype("category")
df.head(3)


# ## Filter A `DataFrame` Based On A Condition

# In[25]:


df = pd.read_csv("employees.csv", parse_dates = ["Start Date", "Last Login Time"])
df["Senior Management"] = df["Senior Management"].astype("bool")
df["Gender"] = df["Gender"].astype("category")
df.head(3)


# ## Filter with More than One Condition (AND)

# In[50]:


df = pd.read_csv("employees.csv", parse_dates = ["Start Date", "Last Login Time"])
df["Senior Management"] = df["Senior Management"].astype("bool")
df["Gender"] = df["Gender"].astype("category")
df.head(3)


# In[55]:


mask1 = df["Gender"] == "Male"
mask2 = df["Team"] == "Marketing"

df[mask1 & mask2]


# ## Filter with More than One Condition (OR)

# In[82]:


df = pd.read_csv("employees.csv", parse_dates = ["Start Date", "Last Login Time"])
df["Senior Management"] = df["Senior Management"].astype("bool")
df["Gender"] = df["Gender"].astype("category")
df.head(3)


# In[86]:


mask1 = df["Senior Management"]
mask2 = df["Start Date"] < "1990-01-01"

df[mask1 | mask2]


# In[93]:


mask1 = df["First Name"] == "Robert"
mask2 = df["Team"] == "Client Services"
mask3 = df["Start Date"] > "2016-06-01"

df[(mask1 & mask2) | mask3]


# ## The `.isin()` Method

# In[9]:


df = pd.read_csv("employees.csv", parse_dates = ["Start Date", "Last Login Time"])
df["Senior Management"] = df["Senior Management"].astype("bool")
df["Gender"] = df["Gender"].astype("category")
df.head(3)


# In[12]:


mask1 = df["Team"] == "Legal"
mask2 = df["Team"] == "Sales"
mask3 = df["Team"] == "Product"

df[mask1 | mask2 | mask3]


# ## The `.isnull()` and `.notnull()` Methods

# In[19]:


df = pd.read_csv("employees.csv", parse_dates = ["Start Date", "Last Login Time"])
df["Senior Management"] = df["Senior Management"].astype("bool")
df["Gender"] = df["Gender"].astype("category")
df.head(3)


# In[22]:


mask = df["Team"].isnull()

df[mask]


# In[25]:


condition = df["Gender"].notnull()

df[condition]


# ## The `.between()` Method

# In[26]:


df = pd.read_csv("employees.csv", parse_dates = ["Start Date", "Last Login Time"])
df["Senior Management"] = df["Senior Management"].astype("bool")
df["Gender"] = df["Gender"].astype("category")
df.head(3)


# In[29]:


df[df["Salary"].between(60000, 70000)]


# In[32]:


df[df["Bonus %"].between(2.0, 5.0)]


# In[35]:


df[df["Start Date"].between("1991-01-01", "1992-01-01")]


# In[38]:


df[df["Last Login Time"].between("08:30AM", "12:00PM")]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## The `.duplicated()` Method

# In[15]:


df = pd.read_csv("employees.csv", parse_dates = ["Start Date", "Last Login Time"])
df["Senior Management"] = df["Senior Management"].astype("bool")
df["Gender"] = df["Gender"].astype("category")
df.sort_values("First Name", inplace = True)
df.head(3)


# In[27]:


mask = ~df["First Name"].duplicated(keep = False)
df[mask]


# ## The `.drop_duplicates()` Method

# In[53]:


df = pd.read_csv("employees.csv", parse_dates = ["Start Date", "Last Login Time"])
df["Senior Management"] = df["Senior Management"].astype("bool")
df["Gender"] = df["Gender"].astype("category")
df.sort_values("First Name", inplace = True)
df.head(3)


# In[54]:


len(df)


# In[56]:


len(df.drop_duplicates())


# In[59]:


df.drop_duplicates(subset = ["First Name"], keep = False)


# In[62]:


df.drop_duplicates(subset = ["First Name", "Team"], inplace = True)


# In[63]:


df.head(2)


# In[64]:


len(df)


# ## The `.unique()` and `.nunique()` Methods

# In[2]:


df = pd.read_csv("employees.csv", parse_dates = ["Start Date", "Last Login Time"])
df["Senior Management"] = df["Senior Management"].astype("bool")
df["Gender"] = df["Gender"].astype("category")
df.head(3)


# In[6]:


df["Gender"].unique()

df["Team"].unique()


# In[7]:


len(df["Team"].unique())


# In[11]:


df["Team"].nunique(dropna = False)


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




