import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)
st.balloons()

st.title(
'Stroke Statistics'
)

st.write('This dataset is used to predict whether a patient is likely to get stroke based on the input parameters like gender, age, various diseases, and smoking status. Each row in the data provides relavant information about the patient.')


df = pd.read_csv('stroke-data.csv')
st.write(df.head(10))

st.subheader("Distribution Plot")
dplot=sns.distplot(df['age'],kde=False)
st.pyplot()

st.subheader("Joint Plot")
sns.jointplot(x='heart_disease',y='age',data=df,kind='reg')
st.pyplot()

st.subheader("Bar Plot")
sns.barplot(x='ever_married',y='avg_glucose_level',data=df)
st.pyplot()