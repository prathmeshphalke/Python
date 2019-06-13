#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[5]:


week1 = pd.read_csv("Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("Restaurant - Customers.csv")
foods = pd.read_csv("Restaurant - Foods.csv")


# ## The `pd.concat()` Method, Part 1

# In[4]:


week1 = pd.read_csv("Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("Restaurant - Customers.csv")
foods = pd.read_csv("Restaurant - Foods.csv")


# In[7]:


len(week1)


# In[8]:


len(week2)


# In[10]:


len(pd.concat([week1, week2]))


# ## The `pd.concat()` Method, Part 2

# In[6]:


week1 = pd.read_csv("Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("Restaurant - Customers.csv")
foods = pd.read_csv("Restaurant - Foods.csv")


# In[10]:


sales = pd.concat([week1, week2], keys = ["A", "B"])


# In[14]:


sales.ix[("B", 240), "Customer ID"]


# ## The `.append()` Method

# In[15]:


week1 = pd.read_csv("Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("Restaurant - Customers.csv")
foods = pd.read_csv("Restaurant - Foods.csv")


# In[19]:


sales = week2.append(week1, ignore_index = True)


# ## Inner Joins, Part 1

# In[20]:


week1 = pd.read_csv("Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("Restaurant - Customers.csv")
foods = pd.read_csv("Restaurant - Foods.csv")


# In[21]:


week1.head(2)


# In[22]:


week2.head(2)


# In[28]:


week1.merge(week2, how = "inner", on = "Customer ID", suffixes = [" - A", " - B"])


# In[25]:


week1[week1["Customer ID"] == 155]


# In[26]:


week2[week2["Customer ID"] == 155]


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





# ## Inner Joins, Part 2

# In[65]:


week1 = pd.read_csv("Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("Restaurant - Customers.csv")
foods = pd.read_csv("Restaurant - Foods.csv")


# In[66]:


week1.head(2)


# In[67]:


week2.head(2)


# In[68]:


week1.merge(week2, how = "inner", on = ["Customer ID", "Food ID"])


# In[71]:


week1[week1["Customer ID"] == 578]


# In[72]:


week2[week2["Customer ID"] == 578]


# ## Outer Joins

# In[77]:


week1 = pd.read_csv("Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("Restaurant - Customers.csv")
foods = pd.read_csv("Restaurant - Foods.csv")


# In[78]:


week1.head(2)


# In[79]:


week2.head(2)


# In[85]:


merged = week1.merge(week2, how = "outer", on = "Customer ID", suffixes = [" - Week 1", " - Week 2"],
            indicator = True)


# In[88]:


merged["_merge"].value_counts()


# In[92]:


mask = merged["_merge"].isin(["left_only", "right_only"])
merged[mask]


# ## Left Joins

# In[98]:


week1 = pd.read_csv("Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("Restaurant - Customers.csv")
foods = pd.read_csv("Restaurant - Foods.csv")


# In[99]:


week1.head(3)


# In[100]:


foods.head(3)


# In[103]:


week1 = week1.merge(foods, how = "left", on = "Food ID", sort = True)


# In[104]:


week1.head()


# ## The `left_on` and `right_on` Parameters

# In[105]:


week1 = pd.read_csv("Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("Restaurant - Customers.csv")
foods = pd.read_csv("Restaurant - Foods.csv")


# In[106]:


week2.head(3)


# In[107]:


customers.head(3)


# In[111]:


week2 = week2.merge(customers, how = "left", left_on = "Customer ID", right_on = "ID", sort = True).drop("ID", axis = "columns")


# In[112]:


week2.head()


# ## Merging by Indexes with the `left_index` and `right_index` Parameters

# In[118]:


week1 = pd.read_csv("Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("Restaurant - Customers.csv", index_col = "ID")
foods = pd.read_csv("Restaurant - Foods.csv", index_col = "Food ID")


# In[119]:


foods.head(3)


# In[125]:


sales = week1.merge(customers, how = "left", left_on = "Customer ID", right_index = True)
sales = sales.merge(foods, how = "left", left_on = "Food ID", right_index = True)
sales.head(3)


# In[126]:


week1.head(3)


# In[127]:


week2.head(3)


# In[129]:


week1.merge(week2, how = "left", left_index = True, right_index = True, suffixes = [" - Week 1", " - Week 2"])


# ## The `.join()` Method

# In[3]:


week1 = pd.read_csv("Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("Restaurant - Customers.csv")
foods = pd.read_csv("Restaurant - Foods.csv")
satisfaction = pd.read_csv("Restaurant - Week 1 Satisfaction.csv")


# In[4]:


week1.head(3)


# In[5]:


satisfaction.head(3)


# In[9]:


week1.merge(satisfaction, how = "left", left_index = True, right_index = True).head()


# In[8]:


week1.join(satisfaction).head()


# ## The `pd.merge()` Method

# In[10]:


week1 = pd.read_csv("Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("Restaurant - Customers.csv")
foods = pd.read_csv("Restaurant - Foods.csv")
satisfaction = pd.read_csv("Restaurant - Week 1 Satisfaction.csv")


# In[11]:


week1.head(3)


# In[12]:


customers.head(3)


# In[13]:


pd.merge(week1, customers, how = "left", left_on = "Customer ID", right_on = "ID")


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




