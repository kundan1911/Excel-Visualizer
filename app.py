import pandas as pd
import plotly_express as px
import streamlit as st

st.set_page_config(
    page_title="Data Dashboard",
    page_icon=":bar_chart:",
    layout="wide"
)

df=pd.read_excel(
    io='data.xlsx',
    engine='openpyxl',
    skiprows=0,
    usecols='B:W',
    nrows=70
)
# st.dataframe(df)


st.sidebar.header('Use the following filters:')
age=st.sidebar.multiselect(
    "Select Age :",
    options=df['Age'].unique(),
    default=df['Age'].unique()
)
gender=st.sidebar.multiselect(
    "Select Gender :",
    options=df['Gender'].unique(),
    default=df['Gender'].unique()
)
marriage=st.sidebar.multiselect(
    "Select Marital Status :",
    options=df['Marital_Status'].unique(),
    default=df['Marital_Status'].unique()
)
religion=st.sidebar.multiselect(
    "Select Religion :",
    options=df['Religion'].unique(),
    default=df['Religion'].unique()
)
education=st.sidebar.multiselect(
    "Select Education :",
    options=df['Education'].unique(),
    default=df['Education'].unique()
)
occupation=st.sidebar.multiselect(
    "Select Occupation :",
    options=df['Occupation'].unique(),
    default=df['Occupation'].unique()
)
df_selection=df.query(
    'Age == @age & Gender == @gender & Marital_Status == @marriage & Religion == @religion & Education == @education & Occupation == @occupation'
)

st.dataframe(df_selection)