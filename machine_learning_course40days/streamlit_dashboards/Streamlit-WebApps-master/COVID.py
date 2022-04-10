import requests
import pandas as pd
import streamlit as st 
from bokeh.plotting import figure, save, show
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral3
from bokeh.models.tools import HoverTool

st.title("COVID-19 Cases in India  \n")
result = requests.get("https://api.covid19india.org/data.json")

result = result.json()

states = []

for i in result['statewise']:
    states.append(i['state'])

a = []

for i in range(1, len(result['statewise'])):
    a.append(result['statewise'])

statewise = result['statewise'][1:] 
states = states[1:] # Total tag is discarded.
# print(states[0])
# print(statewise[0])

statewise_active = []
statewise_confirmed = []
statewise_deaths = []
statewise_recovered = []
states_short = []

for i in range(0, len(statewise)):
    statewise_active.append(int(statewise[i]['active']))
    statewise_confirmed.append(int(statewise[i]['confirmed']))
    statewise_deaths.append(int(statewise[i]['deaths']))
    statewise_recovered.append(int(statewise[i]['recovered']))
    states_short.append(statewise[i]['statecode'])

state_dict = {'States' : states,
                'Confirmed Cases' : statewise_confirmed,
                'Total Deaths' : statewise_deaths,
                'Active Cases' : statewise_active,
                'Recovered' : statewise_recovered,
                'State Code' : states_short}

df = pd.DataFrame(state_dict)
df['Confirmed to Death Ratio'] = df['Confirmed Cases'] / df['Total Deaths']
for i in range(0, len(df['Total Deaths'])):
    if df['Total Deaths'][i] ==0 :
        df['Confirmed to Death Ratio'][i] = 0
print(df.head())

## Total:
total_active_cases = result['statewise'][0]['active']
total_confirmed_cases = result['statewise'][0]['confirmed']
total_deaths = result['statewise'][0]['deaths']

# print("Total Active cases are:", total_active_cases)
# print("Total Confirmed cases are:", total_confirmed_cases)
# print("Total Deaths are:", total_deaths)

daily_confirmed = []
daily_deceased = []
dates = []
daily_recovered = []

for i in range(0,len(result['cases_time_series'])):
    daily_confirmed.append(result['cases_time_series'][i]['dailyconfirmed'])
    daily_deceased.append(result['cases_time_series'][i]['dailydeceased'])
    dates.append(result['cases_time_series'][i]['date'])
    daily_recovered.append(result['cases_time_series'][i]['dailyrecovered'])

df1 = df[['State Code', 'Confirmed Cases']]
# print("States are", states)
# print("Daliy Confirmed ", daily_confirmed)
# print("Daily Deceased ", daily_deceased)
# print("Dates: ", dates)

case_type = st.sidebar.selectbox("Select One of the Options", ("Total", "Statewise"))

if case_type == "Total":

    st.write("Total Confirmed cases are:", total_confirmed_cases)
    st.write("Total Deaths are:", total_deaths)
    st.write("Total Active cases are:", total_active_cases)

    labels = ["Total Confirmed Cases", "Active Cases", "Deaths"]
    tops = [total_confirmed_cases, total_active_cases, total_deaths]
    source = ColumnDataSource(data=dict(labels = labels, tops = tops, color = Spectral3))
    source1 = ColumnDataSource(df1)

    p = figure(
        x_range = labels,
        plot_width = 500,
        plot_height = 500,
        title = "Cases in India"
    )

    p.vbar(
        x = 'labels',
        top = 'tops',
        bottom = 0,
        width = 0.9,
        color = 'color',
        source = source
    )

    p2 = figure(
        x_range = df1['State Code'],
        plot_width = 800,
        plot_height = 500,
        title = "Cases in Different States"
    )

    p2.vbar(
        x = 'State Code',
        top = 'Confirmed Cases',
        bottom = 0,
        width = 0.1,
        color = 'green',
        source = source1
    )
    st.bokeh_chart(p, use_container_width=True)
    """
    ## StateWise Comparision
    """
    st.bokeh_chart(p2, use_container_width = True)
    """
    ## Cases Tally since Day 1
    """

    p1 = figure(
        x_range = (0,len(daily_confirmed)),
        y_range = (0, 25000),
        plot_width = 500,
        plot_height = 500,
        title = "Cases in India",
    )

    p1.line(
        range(len(daily_confirmed)),
        y = daily_confirmed,
        color = 'red',
        line_width = 2,
        legend_label = "Total Cases",
    )

    p1.line(
        range(len(daily_confirmed)),
        y = daily_deceased,
        color = '#0000cd',
        line_width = 2,
        legend_label = "Total Deceased",
    )

    p1.line(
        range(len(daily_confirmed)),
        y = daily_recovered,
        color = 'green',
        line_width = 2,
        legend_label = "Total Recovered",
    )

    p1.legend.location = 'top_left'
    st.bokeh_chart(p1, use_container_width=True)

if case_type == "Statewise":
    if st.checkbox('DataFrame with Information for Top Five States'):
        "Dataset",df.head(5)
    state_selected = st.sidebar.selectbox("Select any of the following States", states)

    x = df.loc[df['States'] == state_selected]
    
    x = x.to_numpy()
    x = x[0]
    labels1 = ['Confirmed Cases', 'Death Cases', 'Active Cases', 'Recovered Cases']
    tops1 = [x[1], x[2], x[3], x[4]]
    color = ['#ADD8E6', 'red', 'green', 'yellow']

    st.write("## Data for {} is: ".format(state_selected))
    st.write("The Total Number of Confirmed Cases in {} are: {}".format(x[0], x[1]))
    st.write("The Total Number of Deaths Cases in {} are: {}".format(x[0], x[2]))
    st.write("The Total Number of Active Cases in {} are: {}".format(x[0], x[3]))
    st.write("The Total Number of Recovered Cases in {} are: {}".format(x[0], x[4]))
    st.write("The Confirmed to Death ratio in {} are: {}".format(x[0],round(x[-1],2)))

    p3 = figure(
        x_range = labels1,
        plot_width = 500,
        plot_height = 500,
        title = "Cases in State"
    )

    p3.vbar(
        x = labels1,
        top = tops1,
        bottom = 0,
        width = 0.5,
        color = color
    )

    st.bokeh_chart(p3, use_container_width=True)