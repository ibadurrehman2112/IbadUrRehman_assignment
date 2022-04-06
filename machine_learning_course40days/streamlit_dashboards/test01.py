import streamlit as st 
import seaborn as sns 

st.header("This is my second app")
st.text("Hi")

st.header("Hi this")

df = sns.load_dataset('iris')
st.write(df[['species', 'sepal_length', 'petal_length']].head(10))

st.bar_chart(df['sepal_length']) #bar chart is only for continuous value
st.line_chart(df['sepal_length'])