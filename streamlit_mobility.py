#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


mob_data = pd.read_csv("applemobilitytrends-2020-04-19.csv" )


# In[4]:


city = "London"
city_data = mob_data[mob_data["region"] == city] \
.drop(columns = ["geo_type", "region"]) \
.melt(id_vars = "transportation_type", var_name = "date", value_name = "flow")

city_data['date'] = pd.to_datetime(city_data['date'])


# In[5]:


mode = "driving"

mode_filtered_df = city_data[city_data["transportation_type"] == mode]


# In[7]:


plot_df = mode_filtered_df.set_index("date") \
.drop(columns = "transportation_type")


# In[8]:


plt.style.use("fivethirtyeight")


# In[9]:


plt.xticks([])
plt.plot(plot_df);

