import pandas as pd
from datetime import date

import yfinance as yf
import numpy as np
import cufflinks as cf
cf.go_offline()
from cufflinks import tools
import plotly.graph_objs as go
import streamlit as st

st.title('Selected Market Prices.')


tab1, tab2, tab3 = st.tabs(["Currency Pairs NZ", "Currency Pairs UK", "Oil & Gas"])


with tab1:
    st.header("Currency Pairs NZ")
    tickers =['GBPNZD=X', 'USDNZD=X', 'AUDNZD=X']
    currency=tickers
    start='2020-01-01'
    end=date.today()

    df =  yf.download(tickers, start, end)['Adj Close']
    fig = df.iplot(asFigure=True, xTitle="Time",
            yTitle="Prices", title="Currency Prices")
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.header("Currency Pairs UK")
    tickers = ['EURUSD=X', 'GBPEUR=X',  'GBPUSD=X']
    currency=tickers
    start='2020-01-01'
    end=date.today()

    df =  yf.download(tickers, start, end)['Adj Close']
    fig2 = df.iplot(asFigure=True, xTitle="Time",
            yTitle="Prices", title="Currency Prices")
    st.plotly_chart(fig2, use_container_width=True)    


with tab3:
    st.header("Oil (CL=F) & Gas (NG=F)")
    tickers = ['NG=F', 'CL=F']
    currency=tickers
    start='2020-01-01'
    end=date.today()

    df =  yf.download(tickers, start, end)['Adj Close']
    fig3 = go.Figure(**tools.merge_figures([df.figure(columns=['NG=F']), df.figure(columns=['CL=F'], color='green')])).set_axis(['CL=F'], side='right')
    fig3['layout'].update(title='Oil and Gas Prices')
    st.plotly_chart(fig3, use_container_width=True)
