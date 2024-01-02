import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv("Supermarket Sales\supermarket_sales.csv", sep=";", decimal=",")
df["Date"] = pd.to_datetime(df["Date"])
df=df.sort_values("Date")

df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.moth))
month = st.sidebar.selectbox("Mês", df["Moth"].unique())

print(df)