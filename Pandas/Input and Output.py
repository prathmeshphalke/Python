#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# ## Quick Object Conversions

# In[45]:


baby_names = pd.read_csv("https://data.illinois.gov/api/views/9ean-aer9/rows.csv")
baby_names.head(3)


# ## Export `DataFrame` to CSV File with the `.to_csv()` Method

# In[60]:


baby_names = pd.read_csv("https://data.illinois.gov/api/views/9ean-aer9/rows.csv")
baby_names.head(3)


# In[63]:


baby_names.to_csv("Baby Names.csv", index = False, columns = ["Name", "Frequency"], encoding = "utf-8")


# ## Import Excel File

# In[65]:


df = pd.read_excel("Data - Single Worksheet.xlsx")
df


# In[84]:


data = pd.read_excel("Data - Multiple Worksheets.xlsx", sheetname = None)


# In[85]:


type(data)


# In[86]:


data


# ## Export Excel File

# In[124]:


baby_names = pd.read_csv("https://data.illinois.gov/api/views/9ean-aer9/rows.csv")
baby_names.head(3)


# In[131]:


popular = baby_names[baby_names["Frequency"] >= 2000]
unpopular = baby_names[baby_names["Frequency"] < 2000]


# In[136]:


excel_file = pd.ExcelWriter("Baby Name Frequencies.xlsx")


# In[137]:


popular.to_excel(excel_file, sheet_name = "Popular Names", index = False)
unpopular.to_excel(excel_file, sheet_name = "Unpopular Names", index = False, columns = ["Name", "Frequency"])


# In[138]:


excel_file.save()


# ## Export Excel File

# In[5]:


URL = "https://data.cityofnewyork.us/api/views/25th-nujf/rows.csv"
baby_names = pd.read_csv(URL)
baby_names.head(3)


# In[9]:


girls = baby_names[baby_names["GNDR"] == "FEMALE"]
boys = baby_names[baby_names["GNDR"] == "MALE"]


# In[11]:


excel_file = pd.ExcelWriter("Baby Names.xlsx")


# In[12]:


girls.to_excel(excel_file, sheet_name = "Girls", index = False)
boys.to_excel(excel_file, sheet_name = "Boys", index = False, columns = ["GNDR", "NM", "CNT"])


# In[13]:


excel_file.save()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




