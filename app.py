import streamlit as st
import pandas as pd
from client import StockApi

st.set_page_config(page_title="Stock Market App", layout="wide")
st.title("Stock Market App")
st.subheader("By Varsha Mhetre")

company = st.text_input("Company Name")

@st.cache_resource(ttl=3600)
def fetch_data():
    return StockApi(api_key=st.secrets["API_KEY"])

Stockapi = fetch_data()

@st.cache_data(ttl=3600)
def get_symbol(company):
    return Stockapi.search_symbol(company)

@st.cache_data(ttl=3600)
def get_chart(get_):
    df = Stockapi.time_series_daily_data(symbol)
    return Stockapi.plot_graph(df)

if company:
    company_data = get_symbol(company)

    


