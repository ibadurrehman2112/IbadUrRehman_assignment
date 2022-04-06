from pyexpat import features
import streamlit as st 
import seaborn as sns
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# make containers 
header = st.container()
data_sets = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title("Ship App")
    st.text("In this project we will work on titanic data")

with data_sets:
    st.header("Ship is draining")
    st.text("Titanic datasets")
    #import data
    df = sns.load_dataset('titanic')
    df = df.dropna()
    st.write(df.head(10))

    st.subheader("How many peoples there?")
    st.bar_chart(df['sex'].value_counts())

    # Other plot
    st.subheader("Difference w.r.t class")
    st.bar_chart(df['class'].value_counts())

    # barpplot
    st.bar_chart(df["age"].sample(10)) # or .head()



with features:
    st.header("These are our app features")
    st.text("Many features")
    st.markdown('1. **Feature 1**: This is one')
    st.markdown('2. **Feature 2**: This is one')
    st.markdown('3. **Feature 3**: This is one')


with model_training:
    st.header("How about titanic pessengers?- Model training")
    st.text("Model traing here")

    #making columns
    input, display = st.columns(2)

    # Your selection point in first column?
    max_depth = input.slider("How many people do you know", min_value=10, max_value= 100, value=20, step=5)

# n_estimators
n_estimators = input.selectbox("How many tree should be there in a RF?", options =[50, 100, 200, 300, 'NO limit'])

# adding list of features

input.write(df.columns)
# input features from users

input_features = input.text_input('Which feature we should use?')

# Machine learning model

model = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)

# condition for No limits
if n_estimators == 'NO limit':
    model = RandomForestRegressor(max_depth=max_depth)
else:
    model = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)

# define  X and y

X = df[[input_features]]
y = df[['fare']]

# fit our model 
model.fit(X,y)
pred = model.predict(y)

# Display matrices

display.subheader("Mean absolute error of the model is :")
display.write(mean_absolute_error(y, pred))
display.subheader("Mean squared error of the model is :")
display.write(mean_squared_error(y, pred))
display.subheader("R squared score of the model is :")
display.write(r2_score(y, pred))




