#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


nba = pd.read_csv("nba.csv")


# ## Shared Methods and Attributes

# In[4]:


nba = pd.read_csv("nba.csv")


# In[8]:


nba.head(1)


# In[9]:


nba.tail()


# In[10]:


nba.index


# In[11]:


nba.values


# In[12]:


nba.shape


# In[13]:


nba.dtypes


# In[14]:


nba.head()


# In[15]:


nba.columns


# In[16]:


nba.axes


# In[17]:


nba.info()


# In[18]:


nba.get_dtype_counts()


# In[20]:


rev = pd.read_csv("revenue.csv", index_col = "Date")
rev.head(3)


# In[22]:


s = pd.Series([1, 2, 3])
s.sum()


# In[27]:


rev.sum(axis = "columns")


# ## Select One Column from a `DataFrame`

# In[40]:


nba = pd.read_csv("nba.csv")
nba.head(3)


# ## Select Two or More Columns from A `DataFrame`

# In[64]:


nba = pd.read_csv("nba.csv")
nba.head(3)


# In[70]:


nba[["Team", "Name"]].head(3)
nba[["Number", "College"]]
nba[["Salary", "Team", "Name"]].tail()


# In[71]:


select = ["Salary", "Team", "Name"]
nba[select]


# ## Add New Column to `DataFrame`

# In[83]:


nba = pd.read_csv("nba.csv")
nba.head(3)

nba["Sport"] = "Basketball"
nba.head(3)

nba["League"] = "National Basketball Association"
nba.head(3)

nba = pd.read_csv("nba.csv")
nba.head(3)

nba.insert(3, column = "Sport", value = "Basketball")
nba.head(3)

nba.insert(7, column = "League", value = "National Basketball Association")
Output = None


# ## Broadcasting Operations

# In[103]:


nba = pd.read_csv("nba.csv")
nba.head(3)


# In[114]:


nba["Age"].add(5)
nba["Age"] + 5

nba["Salary"].sub(5000000)
nba["Salary"] - 5000000

nba["Weight"].mul(0.453592)
nba["Weight in Kilograms"] = nba["Weight"] * 0.453592


# In[115]:


nba.head(3)


# In[119]:


nba["Salary"].div(1000000)
nba["Salary in Millions"] = nba["Salary"] / 1000000


# In[120]:


nba.head(3)


# ## A Review of the `.value_counts()` Method

# In[122]:


nba = pd.read_csv("nba.csv")
nba.head(3)


# In[132]:


nba["Team"].value_counts()
nba["Position"].value_counts().head(1)
nba["Weight"].value_counts().tail()
nba["Salary"].value_counts()


# ## Drop Rows with Null Values

# In[133]:


nba = pd.read_csv("nba.csv")
nba.head(3)


# In[134]:


nba.tail(3)


# In[137]:


nba.dropna(how = "all", inplace = True)


# In[138]:


nba.tail(3)


# In[141]:


nba.head(3)


# In[143]:


nba.dropna(subset = ["Salary", "College"])


# ## Fill in Null Values with the `.fillna()` Method

# In[20]:


nba = pd.read_csv("nba.csv")
nba.head(3)


# In[21]:


nba.fillna(0)


# In[23]:


nba["Salary"].fillna(0, inplace = True)


# In[24]:


nba.head()


# In[27]:


nba["College"].fillna("No College", inplace = True)


# In[28]:


nba.head()


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





# ## The `.astype()` Method

# In[161]:


nba = pd.read_csv("nba.csv").dropna(how = "all")
nba["Salary"].fillna(0, inplace = True)
nba["College"].fillna("None", inplace = True)
nba.head(6)


# In[188]:


nba.dtypes
nba.info()


# In[166]:


nba["Salary"] = nba["Salary"].astype("int")


# In[167]:


nba.head(3)


# In[173]:


nba["Number"] = nba["Number"].astype("int")
nba["Age"] = nba["Age"].astype("int")
nba.head(3)


# In[175]:


nba["Age"].astype("float")


# In[178]:


nba["Position"].nunique()


# In[181]:


nba["Position"] = nba["Position"].astype("category")


# In[186]:


nba["Team"] = nba["Team"].astype("category")


# In[187]:


nba.head()


# ## Sort a `DataFrame` with the `.sort_values()` Method, Part I

# In[2]:


nba = pd.read_csv("nba.csv")
nba.head(3)


# In[9]:


nba.sort_values("Name", ascending = False)

nba.sort_values("Age", ascending = False)

nba.sort_values("Salary", ascending = False, inplace = True)
nba.head(3)


# In[15]:


nba.sort_values("Salary", ascending = False, na_position = "first").tail()


# ## Sort a `DataFrame` with the `.sort_values()` Method, Part II

# In[16]:


nba = pd.read_csv("nba.csv")
nba.head(3)


# In[20]:


nba.sort_values(["Team", "Name"], ascending = [True, False], inplace = True)
nba.head(3)


# ## Sort `DataFrame` with the `.sort_index()` Method

# In[21]:


nba = pd.read_csv("nba.csv")
nba.head(3)


# In[23]:


nba.sort_values(["Number", "Salary", "Name"], inplace = True)
nba.tail(3)


# In[26]:


nba.sort_index(ascending = False, inplace = True)


# In[27]:


nba.head(3)


# ## Rank Values with the `.rank()` Method

# In[28]:


nba = pd.read_csv("nba.csv").dropna(how = "all")
nba["Salary"] = nba["Salary"].fillna(0).astype("int")
nba.head(3)


# In[33]:


nba["Salary Rank"] = nba["Salary"].rank(ascending = False).astype("int")
nba.head(3)


# In[35]:


nba.sort_values(by = "Salary", ascending = False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




