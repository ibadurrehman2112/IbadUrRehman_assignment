import streamlit as st
import seaborn as sns
st.header('This is my first test application')

phool = sns.load_dataset('iris')
st.write(phool.head())
st.text("Thank you all")

#pip install -r requirement.txt
# conda activate
# conda create -n streamlit python=3.8
# conda activate streamlit
# pip install streamlit numpy pandas seaborn matplotlib scipy statsmodels
# streamlit run test.py
# pytorch
# keras


