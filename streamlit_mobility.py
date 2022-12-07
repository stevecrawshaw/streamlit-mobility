import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

mob_data = pd.read_csv("applemobilitytrends-2020-04-19.csv" )

st.title("Mobility in the Time of the Plague")

city = st.sidebar.selectbox("Select a City", ["London", "Paris"])

mode = st.sidebar.selectbox("Select mode", ["driving", "walking"])

city_data = mob_data[mob_data["region"] == city] \
.drop(columns = ["geo_type", "region"]) \
.melt(id_vars = "transportation_type", var_name = "date", value_name = "flow")

city_data['date'] = pd.to_datetime(city_data['date'])

# mode = "driving"

mode_filtered_df = city_data[city_data["transportation_type"] == mode]

plot_df = mode_filtered_df.set_index("date") \
.drop(columns = "transportation_type")

plt.style.use("fivethirtyeight")

fig, ax = plt.subplots()
ax = plt.plot(plot_df)
plt.xticks([])
st.pyplot(fig)
