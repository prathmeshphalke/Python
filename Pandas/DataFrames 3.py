#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[ ]:


bond = pd.read_csv("jamesbond.csv")
bond.head(3)


# ## The `.set_index()` and `.reset_index()` Methods

# In[ ]:


bond = pd.read_csv("jamesbond.csv")
bond.head(3)


# In[ ]:


bond.set_index("Film", inplace = True)
bond.head(3)


# In[ ]:


bond.reset_index(drop = False, inplace = True)
bond.head(3)


# In[ ]:


bond.set_index("Film", inplace = True)
bond.head(3)


# In[ ]:


bond.reset_index(inplace = True)
bond.set_index("Year", inplace = True)
bond.head(3)


# ## Retrieve Rows by Index Label with `.loc[]`

# In[ ]:


bond = pd.read_csv("jamesbond.csv", index_col = "Film")
bond.sort_index(inplace = True)
bond.head(3)


# In[ ]:


bond.loc["Goldfinger"]
bond.loc["GoldenEye"]
#bond.loc["Sacred Bond"]
bond.loc["Casino Royale"]


# In[ ]:


bond.loc["Diamonds Are Forever" : "Moonraker"]
bond.loc[: "On Her Majesty's Secret Service"]


# In[ ]:


bond.loc[["Octopussy", "Moonraker"]]


# In[ ]:


bond.loc[["For Your Eyes Only", "Live and Let Die", "Gold Bond"]]


# In[ ]:


"Gold Bond" in bond.index


# ## Retrieve Row(s) by Index Position with `iloc`

# In[ ]:


bond = pd.read_csv("jamesbond.csv")
bond.head(3)


# In[ ]:


bond.loc[15]
bond.iloc[15]

bond.iloc[[15, 20]]
bond.iloc[:4]
bond.iloc[4:8]
bond.iloc[20:]


# In[ ]:


bond = pd.read_csv("jamesbond.csv", index_col = "Film")
bond.sort_index(inplace = True)
bond.head(3)


# In[ ]:


bond.iloc[[5, 10, 15, 20]]


# ## The Catch-All `.ix[]` Method

# In[6]:


bond = pd.read_csv("jamesbond.csv", index_col = "Film")
bond.sort_index(inplace = True)
bond.head(3)


# In[14]:


bond.ix["GoldenEye"]
bond.ix[["Diamonds are Forever", "Moonraker", "Spectre"]]
bond.ix["A View to a Kill" : "The World Is Not Enough"]
# bond.ix["Sacred Bond"]
bond.ix[["Spectre", "Sacred Bond"]]

"Spectre" in bond.index
"Sacred Bond" in bond.index


# In[ ]:


bond = pd.read_csv("jamesbond.csv", index_col = "Film")
bond.sort_index(inplace = True)
bond.head(3)


# In[ ]:


bond.loc["Moonraker", ["Actor", "Budget", "Year"]]

bond.iloc[14, [5, 3, 2]]

bond.ix[20, "Budget"]
bond.ix["The Man with the Golden Gun", :4]
bond.ix[5, 3]


# ## Set New Values for a Specific Cell or Row

# In[ ]:


bond = pd.read_csv("jamesbond.csv", index_col = "Film")
bond.sort_index(inplace = True)
bond.head(3)


# In[ ]:


bond.ix["Dr. No"]


# In[ ]:


bond.ix["Dr. No", "Actor"] = "Sir Sean Connery"


# In[ ]:


bond.ix["Dr. No", ["Box Office", "Budget", "Bond Actor Salary"]] = [448800000, 7000000, 600000]


# In[ ]:


bond.ix["Dr. No", "Budget"]


# ## Set Multiple Values in `DataFrame`

# In[38]:


bond = pd.read_csv("jamesbond.csv", index_col = "Film")
bond.sort_index(inplace = True)
bond.head(3)


# In[42]:


mask = bond["Actor"] == "Sean Connery"


# In[57]:


bond.ix[mask, "Actor"] = "Sir Sean Connery"


# In[60]:


bond[bond["Actor"] == "Roger Moore"]

bond.ix[bond["Actor"] == "Roger Moore"]


# ## Rename Index Labels or Columns in a `DataFrame`

# In[ ]:


bond = pd.read_csv("jamesbond.csv", index_col = "Film")
bond.sort_index(inplace = True)
bond.head(3)


# In[ ]:


bond.rename(columns = {"Year" : "Release Date", "Box Office" : "Revenue"}, inplace = True)


# In[ ]:


bond.head(1)


# In[ ]:


bond.rename(index = {"Dr. No" : "Doctor No", 
                     "GoldenEye" : "Golden Eye",
                    "The World Is Not Enough" : "Best Bond Movie Ever"}, inplace = True)


# In[ ]:


bond.ix["Best Bond Movie Ever"]


# In[ ]:


bond.head(1)


# In[ ]:


bond.columns = ["Year of Release", "Actor", "Director", "Gross", "Cost", "Salary"]


# In[ ]:


bond.head(3)


# ## Delete Rows or Columns from a `DataFrame`

# In[ ]:


bond = pd.read_csv("jamesbond.csv", index_col = "Film")
bond.sort_index(inplace = True)
bond.head(3)


# In[ ]:


# bond.drop("Casino Royale", inplace = True)
bond.drop(labels = ["Box Office", "Bond Actor Salary", "Actor"], axis = "columns", inplace = True)


# In[ ]:


actor = bond.pop("Actor")


# In[ ]:


actor


# In[ ]:


del bond["Director"]


# In[ ]:


del bond["Year"]


# ## Create Random Sample

# In[ ]:


bond = pd.read_csv("jamesbond.csv", index_col = "Film")
bond.sort_index(inplace = True)
bond.head(3)


# In[ ]:


bond.sample(n = 3, axis = "columns")


# ## The `.nsmallest()` and `.nlargest()` Methods

# In[ ]:


bond = pd.read_csv("jamesbond.csv", index_col = "Film")
bond.sort_index(inplace = True)
bond.head(3)


# In[ ]:


bond.sort_values("Box Office", ascending = False).head(3)


# In[ ]:


bond.nlargest(3, columns = "Box Office")

bond.nsmallest(n = 2, columns = "Box Office")


# In[ ]:


bond.nlargest(3, columns = "Budget")

bond.nsmallest(n = 6, columns = "Bond Actor Salary")


# In[ ]:


bond["Box Office"].nlargest(8)

bond["Year"].nsmallest(2)


# ## Filtering with the `where` Method

# In[2]:


bond = pd.read_csv("jamesbond.csv", index_col = "Film")
bond.sort_index(inplace = True)
bond.head(3)


# In[3]:


mask = bond["Actor"] == "Sean Connery"
bond[mask]


# In[4]:


bond.where(mask)


# In[ ]:


bond.where(bond["Box Office"] > 800)


# In[ ]:


mask2 = bond["Box Office"] > 800


# In[ ]:


bond.where(mask & mask2)


# ## The `.query()` Method

# In[2]:


bond = pd.read_csv("jamesbond.csv", index_col = "Film")
bond.sort_index(inplace = True)
bond.head(3)


# In[5]:


bond.columns = [column_name.replace(" ", "_") for column_name in bond.columns]
bond.head(1)


# In[8]:


bond.query('Actor == "Sean Connery"')
bond.query("Director == 'Terence Young'")
bond.query("Actor != 'Roger Moore'")


# In[9]:


bond.query("Box_Office > 600")


# In[11]:


bond.query("Actor == 'Roger Moore' or Director == 'John Glen'")


# In[13]:


bond.query("Actor in ['Timothy Dalton', 'George Lazenby']")

bond.query("Actor not in ['Sean Connery', 'Roger Moore']")


# ## A Review of the `.apply()` Method on Single Columns

# In[9]:


bond = pd.read_csv("jamesbond.csv", index_col = "Film")
bond.sort_index(inplace = True)
bond.head(3)


# In[10]:


def convert_to_string_and_add_millions(number):
    return str(number) + " MILLIONS!"


# In[11]:


columns = ["Box Office", "Budget", "Bond Actor Salary"]
for col in columns:
    bond[col] = bond[col].apply(convert_to_string_and_add_millions)


# In[12]:


bond.head(3)


# ## The `.apply()` Method with Row Values

# In[13]:


bond = pd.read_csv("jamesbond.csv", index_col = "Film")
bond.sort_index(inplace = True)
bond.head(3)


# In[14]:


def good_movie(row):
    
    actor = row[1]
    budget = row[4]
    
    if actor == "Pierce Brosnan":
        return "The best"
    elif actor == "Roger Moore" and budget > 40:
        return "Enjoyable"
    else:
        return "I have no clue"
    
bond.apply(good_movie, axis = "columns")


# ## The `.copy()` Method

# In[30]:


bond = pd.read_csv("jamesbond.csv", index_col = "Film")
bond.sort_index(inplace = True)
bond.head(3)


# In[25]:


directors = bond["Director"]
directors.head(3)


# In[27]:


directors["A View to a Kill"] = "Mister John Glen"


# In[28]:


directors.head(3)


# In[29]:


bond.head(3)


# In[32]:


directors = bond["Director"].copy()
directors.head(3)


# In[34]:


directors["A View to a Kill"] = "Mister John Glen"


# In[35]:


directors.head(3)


# In[36]:


bond.head(3)


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




