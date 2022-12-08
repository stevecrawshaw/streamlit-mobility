import streamlit as st
import pandas as pd
import altair as alt

mob_data = pd.read_csv("city_mobility.csv" )

cities = list(mob_data['city'].unique())
modes = list(mob_data['transportation_type'].unique())

st.title("Mobility in the UK during COVID-19")

city = st.sidebar.selectbox("Select a City", cities)

mode = st.sidebar.selectbox("Select mode", modes)

st.subheader(f'{mode} in {city}')

mob_data['date'] = pd.to_datetime(mob_data['date'])

mode_filtered_df = mob_data[(mob_data['transportation_type'] == mode) & (mob_data['city'] == city)]

lines = (
    alt.Chart(mode_filtered_df)
    .mark_line()
    .encode(x = "date", y="flow")
)

lines.encoding.x.title = 'Date'
lines.encoding.y.title = 'Normalised daily flow'

xrule = (
    alt.Chart()
    .mark_rule(color="cyan", strokeWidth=2)
    .encode(x=alt.datum(alt.DateTime(year=2020, month="March", date = 23)))
)

mob_chart = lines + xrule

mob_chart
