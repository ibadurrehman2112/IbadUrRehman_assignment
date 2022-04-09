from doctest import Example
import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# web app title

st.markdown('''
# **Exploratory Data Analysis web application**
This app is develop by Ibad Ur Rehman called EDA APP. 
''')

# How to upload file from PC

with st.sidebar.header("Upload your dataset (.csv)"):
    uploaded_file = st.sidebar.file_uploader("Upload your file", type=['.csv'])
    df = sns.load_dataset('titanic')
    st.sidebar.markdown("[Example CSV file](https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv)")

# profiling report for pandas 

if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative = True)
    st.header('**Input DF**')
    st.write(df)
    st.write('---')
    st.header('**Profiling report with pandas**')
    st_profile_report(pr)
else:
    st.info("Awaiting for CSV file")
    if st.button("Press to use example data"):
    # dataset

        def load_data():
            a = pd.DataFrame(np.random.rand(100, 5),
                            columns=['01-Column', '02-Column','03-Column','04-Column','05-Column'])
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input Dataframe**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)
