import pandas as pd
from datetime import date
import matplotlib.pyplot as plt
import seaborn as sns

import yfinance as yf
import numpy as np
import cufflinks as cf
cf.go_offline()
from cufflinks import tools
import plotly.graph_objs as go
import streamlit as st

st.title('Selected Market Prices.')


tab1, tab2 = st.tabs(["Currencies", "Oil & Gas"])


with tab1:
    st.header("Currencies")
    tickers =['GBPNZD=X', 'USDNZD=X', 'AUDNZD=X']
    currency=tickers
    start='2020-01-01'
    end=date.today()

    df =  yf.download(tickers, start, end)['Adj Close']

    fig = df.iplot(asFigure=True, xTitle="Time",
            yTitle="Prices", title="Currency Prices")
    st.plotly_chart(fig)


with tab2:
    st.header("Oil & Gas")
    tickers = ['NG=F', 'CL=F']
    currency=tickers
    start='2020-01-01'
    end=date.today()

    df =  yf.download(tickers, start, end)['Adj Close']

    fig2 = df.iplot(asFigure=True, xTitle="Time",
            yTitle="Prices", title="Currency Prices")
    st.plotly_chart(fig2)
