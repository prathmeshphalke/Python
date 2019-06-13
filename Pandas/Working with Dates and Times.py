#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import datetime as dt


# ## Review of Python's `datetime` Module

# In[2]:


someday = dt.date(2010, 1, 20)


# In[3]:


someday.year
someday.month
someday.day


# In[4]:


str(someday)


# In[5]:


str(dt.datetime(2010, 1, 10, 17, 13, 57))


# In[6]:


sometime = dt.datetime(2010, 1, 10, 17, 13, 57)


# In[7]:


sometime.year
sometime.month
sometime.day
sometime.hour
sometime.minute
sometime.second


# ## The `pandas Timestamp` Object

# In[8]:


pd.Timestamp("2015-03-31")
pd.Timestamp("2015/03/31")
pd.Timestamp("2013, 11, 04")
pd.Timestamp("1/1/2015")
pd.Timestamp("19/12/2015")
pd.Timestamp("12/19/2015")
pd.Timestamp("4/3/2000")
pd.Timestamp("2021-03-08 08:35:15")
pd.Timestamp("2021-03-08 6:13:29 PM")


# In[9]:


pd.Timestamp(dt.date(2015, 1, 1))


# In[10]:


pd.Timestamp(dt.datetime(2000, 2, 3, 21, 35, 22))


# ## The `pandas DateTimeIndex` Object

# In[11]:


dates = ["2016/01/02", "2016/04/12", "2009/09/07"]
pd.DatetimeIndex(dates)


# In[12]:


dates = [dt.date(2016, 1, 10), dt.date(1994, 6, 13), dt.date(2003, 12, 29)]
dtIndex = pd.DatetimeIndex(dates)


# In[13]:


values = [100, 200, 300]
pd.Series(data = values, index = dtIndex)


# ## The `pd.to_datetime()` Method

# In[14]:


pd.to_datetime("2001-04-19")
pd.to_datetime(dt.date(2015, 1, 1))
pd.to_datetime(dt.datetime(2015, 1, 1, 14, 35, 20))
pd.to_datetime(["2015-01-03", "2014/02/08", "2016", "July 4th, 1996"])


# In[15]:


times = pd.Series(["2015-01-03", "2014/02/08", "2016", "July 4th, 1996"])
times


# In[16]:


pd.to_datetime(times)


# In[17]:


dates = pd.Series(["July 4th, 1996", "10/04/1991", "Hello", "2015-02-31"])
dates


# In[18]:


pd.to_datetime(dates, errors = "coerce")


# In[19]:


pd.to_datetime([1349720105, 1349806505, 1349892905, 1349979305, 1350065705], unit = "s")


# In[20]:


pd.Period("2016-01-08", freq = "10D")


# In[21]:


dates = ["2016-01-01", "2016-02-01", "2016-03-01"]
pd.Series([1, 2, 3], index = pd.PeriodIndex(dates, freq = "2M"))


# In[22]:


pd.Period("2016-01-08", freq = "W")
pd.Period("2016-01-08", freq = "W-SUN")
pd.Period("2016-01-08", freq = "W-WED")
pd.Period("2015-12-10", freq = "10D")

dates = ["2016-01-01", "2016-02-01", "2016-02-01"]
pd.PeriodIndex(dates, freq = "W-MON")
weeks = pd.PeriodIndex(dates, freq = "W-MON")

pd.Series([999, 500, 325], index = weeks, name = "Weekly Revenue")


# ## Create Range of Dates with the `pd.date_range()` Method, Part 1

# In[5]:


times = pd.date_range(start = "2016-01-01", end = "2016-01-10", freq = "D")


# In[6]:


type(times)


# In[9]:


type(times[0])


# In[22]:


pd.date_range(start = "2016-01-01", end = "2050-01-01", freq = "A")


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





# ## Create Range of Dates with the `pd.date_range()` Method, Part 2

# In[27]:


pd.date_range(start = "2012-09-09", periods = 50, freq = "6H")


# ## Create Range of Dates with the `pd.date_range()` Method, Part 3

# In[28]:


pd.date_range(end = "1999-12-31", periods = 100, freq = "7H")


# ## The `.dt` Accessor

# In[29]:


bunch_of_dates = pd.date_range(start = "2000-01-01", end = "2010-12-31", freq = "24D")


# In[30]:


s = pd.Series(bunch_of_dates)
s.head(3)


# In[31]:


mask = s.dt.is_month_end
s[mask]


# ## Import Financial Data Set with `pandas_datareader` Library

# In[33]:


import pandas as pd
import datetime as dt
from pandas_datareader import data


# In[35]:


company = "MSFT"
start = "2010-01-01"
end = "2017-12-31"

stocks = data.DataReader(name = company, data_source = "google", start = start, end = end)
stocks.head(3)


# In[40]:


stocks.values
stocks.columns
stocks.index[0]
stocks.axes


# ## Selecting from a `DataFrame` with a `DateTimeIndex`

# In[57]:


stocks = data.DataReader(name = company, data_source = "google", start = start, end = end)
stocks.head(3)


# In[61]:


stocks.loc["2014-03-04"]
stocks.iloc[300]
stocks.ix["2014-03-04"]
stocks.ix[300]


# In[62]:


stocks.ix["2016-01-01"]


# In[64]:


stocks.loc["2013-10-01" : "2013-10-07"]
stocks.ix["2013-10-01" : "2013-10-07"]


# In[66]:


birthdays = pd.date_range(start = "1991-04-12", end = "2017-12-31", freq = pd.DateOffset(years = 1))


# In[70]:


mask = stocks.index.isin(birthdays)


# In[72]:


stocks[mask]


# ## `Timestamp` Object Attributes

# In[73]:


stocks = data.DataReader(name = company, data_source = "google", start = start, end = end)
stocks.head(3)


# In[76]:


someday = stocks.index[500]
someday


# In[82]:


someday.day
someday.month
someday.year
someday.weekday_name
someday.is_month_end
someday.is_month_start


# In[83]:


stocks.insert(0, "Day of Week", stocks.index.weekday_name)


# In[85]:


stocks.insert(1, "Is Start of Month", stocks.index.is_month_start)


# In[88]:


stocks[stocks["Is Start of Month"]]


# ## The `.truncate()` Method

# In[89]:


stocks = data.DataReader(name = company, data_source = "google", start = start, end = end)
stocks.head(3)


# In[92]:


stocks.truncate(before = "2012-06-07", after = "2013-02-28")


# ## `pd.DateOffset` Objects

# In[94]:


stocks = data.DataReader(name = "GOOG", data_source = "google",
                start = dt.date(2000, 1, 1), end = dt.datetime.now())
stocks.head(3)


# In[105]:


stocks.index + pd.DateOffset(months = 8, years = 5, days = 12, hours = 3, minutes = 42)


# ## More Fun with `pd.DateOffset` Objects

# In[141]:


import pandas as pd
import datetime as dt
from pandas_datareader import data
from pandas.tseries.offsets import *


# In[135]:


stocks = data.DataReader(name = "GOOG", data_source = "google",
                start = dt.date(2000, 1, 1), end = dt.datetime.now())

stocks.head(3)


# In[151]:


stocks.index - MonthEnd()
stocks.index - BMonthEnd()
stocks.index - QuarterEnd()
stocks.index - QuarterBegin()


# In[157]:


stocks.index - YearBegin()


# ## The `Timedelta` Object

# In[215]:


timeA = pd.Timestamp("2016-03-31 04:35:16 PM")
timeB = pd.Timestamp("2016-03-20 02:16:49 AM")


# In[219]:


timeB - timeA


# In[217]:


type(timeA - timeB)


# In[218]:


type(timeA)


# In[227]:


pd.Timedelta(weeks = 8, days = 3, hours = 12, minutes = 45)


# In[226]:


pd.Timedelta("14 days 6 hours 12 minutes 49 seconds")


# ## `Timedeltas` in a Dataset

# In[240]:


shipping = pd.read_csv("ecommerce.csv", index_col = "ID", parse_dates = ["order_date", "delivery_date"])
shipping.head(3)


# In[243]:


shipping["Delivery Time"] = shipping["delivery_date"] - shipping["order_date"]


# In[244]:


shipping.head(3)


# In[249]:


shipping["Twice As Long"] = shipping["delivery_date"] + shipping["Delivery Time"]


# In[250]:


shipping.head(3)


# In[251]:


shipping.dtypes


# In[257]:


mask = shipping["Delivery Time"] == "3423 days"
shipping[mask]


# In[260]:


shipping["Delivery Time"].min()


# In[ ]:





# In[ ]:




