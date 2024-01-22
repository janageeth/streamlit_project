
import yfinance as yf
import streamlit as st
import pandas as pd


st.write("""
# Stock price on Website

Shown are the stock closing price and volume of Apple!



""")

tickerSymbol = 'AAPL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')


st.write("""

## Closing Pricegi

""")

st.line_chart(tickerDf.Close)

st.write("""

## Volume of stocks traded

""")

st.line_chart(tickerDf.Volume)

