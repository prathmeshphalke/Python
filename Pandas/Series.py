#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# ## Create A `Series` Object from A Python List

# In[5]:


ice_cream = ["Chocolate", "Vanilla", "Strawberry", "Rum Raisin"]

pd.Series(ice_cream)


# In[6]:


lottery = [4, 8, 15, 16, 23, 42]

pd.Series(lottery)


# In[7]:


registrations = [True, False, False, False, True]

pd.Series(registrations)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## Create A `Series` Object from a Dictionary

# In[5]:


webster = {"Aardvark" : "An animal",
           "Banana" : "A delicious fruit",
           "Cyan" : "A color"}

pd.Series(webster)


# ## Intro to Attributes

# In[8]:


about_me = ["Smart", "Handsome", "Charming", "Brilliant", "Humble"]
s = pd.Series(about_me)
s


# In[9]:


s.values


# In[10]:


s.index


# In[11]:


s.dtype


# ## Intro to Methods

# In[13]:


prices = [2.99, 4.45, 1.36]
s = pd.Series(prices)
s


# In[14]:


s.sum()


# In[15]:


s.product()


# In[16]:


s.mean()


# ## Parameters and Arguments

# In[ ]:


# Difficulty - Easy, Medium, Hard
# Volume - 1 through 10
# Subtitles - True / False


# In[21]:


fruits = ["Apple", "Orange", "Plum", "Grape", "Blueberry"]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

pd.Series(fruits, weekdays)
pd.Series(data = fruits, index = weekdays)
pd.Series(fruits, index = weekdays)


# In[22]:


fruits = ["Apple", "Orange", "Plum", "Grape", "Blueberry", "Watermelon"]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Monday"]

pd.Series(data = fruits, index = weekdays)


# ## Import `Series` with the `read_csv` Method

# In[27]:


pokemon = pd.read_csv("pokemon.csv", usecols = ["Pokemon"], squeeze = True)
pokemon


# In[30]:


google = pd.read_csv("google_stock_price.csv", squeeze = True)
google


# ## The `.head()` and `.tail()` Methods

# In[31]:


pokemon = pd.read_csv("pokemon.csv", usecols = ["Pokemon"], squeeze = True)
google = pd.read_csv("google_stock_price.csv", squeeze = True)


# In[36]:


pokemon.head(1)


# In[40]:


google.tail(1)


# ## Python Built-In Functions

# In[54]:


pokemon = pd.read_csv("pokemon.csv", usecols = ["Pokemon"], squeeze = True)
google = pd.read_csv("google_stock_price.csv", squeeze = True)


# In[56]:


len(pokemon)
len(google)


# In[57]:


type(pokemon)


# In[58]:


dir(pokemon)


# In[60]:


sorted(pokemon)
sorted(google)


# In[61]:


list(pokemon)


# In[62]:


dict(google)


# In[64]:


max(pokemon)
min(pokemon)


# In[65]:


max(google)


# In[66]:


min(google)


# ## More `Series` Attributes

# In[75]:


pokemon = pd.read_csv("pokemon.csv", usecols = ["Pokemon"], squeeze = True)
google = pd.read_csv("google_stock_price.csv", squeeze = True)


# In[77]:


pokemon.values
google.values


# In[79]:


pokemon.index
google.index


# In[81]:


pokemon.dtype
google.dtype


# In[83]:


pokemon.is_unique
google.is_unique


# In[85]:


pokemon.ndim
google.ndim


# In[87]:


pokemon.shape
google.shape


# In[89]:


pokemon.size
google.size


# In[93]:


pokemon.name = "Pocket Monsters"


# In[94]:


pokemon.head()


# ## The `.sort_values()` Method

# In[95]:


pokemon = pd.read_csv("pokemon.csv", usecols = ["Pokemon"], squeeze = True)
google = pd.read_csv("google_stock_price.csv", squeeze = True)


# In[97]:


pokemon.sort_values().head()


# In[100]:


pokemon.sort_values(ascending = False).tail()


# In[104]:


google.sort_values(ascending = False).head(1)


# In[106]:


google


# ## The `inplace` Parameter

# In[112]:


pokemon = pd.read_csv("pokemon.csv", usecols = ["Pokemon"], squeeze = True)
google = pd.read_csv("google_stock_price.csv", squeeze = True)


# In[113]:


google.head(3)


# In[115]:


google = google.sort_values()


# In[118]:


google.head(3)


# In[119]:


google.sort_values(ascending = False, inplace = True)


# In[120]:


google.head(3)


# ## The `.sort_index()` Method

# In[129]:


pokemon = pd.read_csv("pokemon.csv", usecols = ["Pokemon"], squeeze = True)
google = pd.read_csv("google_stock_price.csv", squeeze = True)


# In[133]:


pokemon.sort_values(ascending = False, inplace = True)


# In[139]:


pokemon.head(3)


# In[138]:


pokemon.sort_index(ascending = True, inplace = True)


# ## Python's `in` Keyword

# In[149]:


pokemon = pd.read_csv("pokemon.csv", usecols = ["Pokemon"], squeeze = True)
google = pd.read_csv("google_stock_price.csv", squeeze = True)


# In[151]:


100 in [1, 2, 3, 4, 5]


# In[152]:


pokemon.head(3)


# In[155]:


100 in pokemon
100 in pokemon.index


# In[156]:


pokemon.index


# In[161]:


"Digimon" in pokemon.values


# ## Extract Values by Index Position

# In[162]:


pokemon = pd.read_csv("pokemon.csv", usecols = ["Pokemon"], squeeze = True)
google = pd.read_csv("google_stock_price.csv", squeeze = True)


# In[163]:


pokemon.head(3)


# In[172]:


pokemon[1]

pokemon[[100, 200, 300]]

pokemon[50:101]

pokemon[:50]

pokemon[-30:]

pokemon[-30 : -10]


# ## Extract Values by Index Label

# In[176]:


pokemon = pd.read_csv("pokemon.csv", index_col = "Pokemon", squeeze = True)
pokemon.head(3)


# In[178]:


pokemon[[100, 134]]


# In[185]:


pokemon["Bulbasaur"]
pokemon["Ditto"]
pokemon[["Charizard", "Jolteon"]]
pokemon[["Blastoise", "Venusaur", "Meowth"]]

pokemon[["Pikachu", "Digimon"]]

pokemon["Bulbasaur" : "Pikachu"]


# ## The `.get()` Method on a `Series`

# In[192]:


pokemon = pd.read_csv("pokemon.csv", index_col = "Pokemon", squeeze = True)
pokemon.sort_index(inplace = True)
pokemon.head(3)


# In[195]:


pokemon.get(key = ["Moltres", "Meowth"])


# In[199]:


pokemon.get(key = "Charizard", default = "This is not a Pokemon")


# In[202]:


pokemon.get(key = "jksajk", default = "This is not a Pokemon")


# ## Math Methods on `Series` Objects

# In[219]:


google = pd.read_csv("google_stock_price.csv", squeeze = True)
google.head(3)


# In[220]:


google.count()


# In[221]:


len(google)


# In[222]:


google.sum()


# In[223]:


google.mean()


# In[224]:


google.sum() / google.count()


# In[225]:


google.std()


# In[226]:


google.min()


# In[227]:


google.max()


# In[228]:


google.median()


# In[229]:


google.mode()


# In[230]:


google.describe()


# ## The `.idxmax()` and `.idxmin()` Methods

# In[232]:


google = pd.read_csv("google_stock_price.csv", squeeze = True)


# In[233]:


google.max()


# In[234]:


google.min()


# In[235]:


google.idxmax()


# In[236]:


google[3011]


# In[237]:


google.idxmin()


# In[238]:


google[11]


# In[239]:


google[google.idxmin()]


# ## The `.value_counts()` Method

# In[240]:


pokemon = pd.read_csv("pokemon.csv", index_col = "Pokemon", squeeze = True)
pokemon.head(3)


# In[242]:


pokemon.value_counts().sum()


# In[243]:


pokemon.count()


# In[246]:


pokemon.value_counts(ascending = True)


# ## The `.apply()` Method

# In[255]:


google = pd.read_csv("google_stock_price.csv", squeeze = True)
google.head(6)


# In[256]:


def classify_performance(number):
    if number < 300:
        return "OK"
    elif number >= 300 and number < 650:
        return "Satisfactory"
    else:
        return "Incredible!"


# In[258]:


google.apply(classify_performance).tail()


# In[259]:


google.head(6)


# In[260]:


google.apply(lambda stock_price : stock_price + 1)


# ## The `.map()` Method

# In[261]:


pokemon_names = pd.read_csv("pokemon.csv", usecols = ["Pokemon"], squeeze = True)
pokemon_names.head(3)


# In[262]:


pokemon_types = pd.read_csv("pokemon.csv", index_col = "Pokemon", squeeze = True)
pokemon_types.head(3)


# In[263]:


pokemon_names.map(pokemon_types)


# In[264]:


pokemon_names = pd.read_csv("pokemon.csv", usecols = ["Pokemon"], squeeze = True)
pokemon_types = pd.read_csv("pokemon.csv", index_col = "Pokemon", squeeze = True).to_dict()


# In[265]:


pokemon_names.head()


# In[266]:


pokemon_types


# In[267]:


pokemon_names.map(pokemon_types)


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




