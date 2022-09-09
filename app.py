import pandas as pd
from datetime import date

import yfinance as yf
import numpy as np
import cufflinks as cf
from cufflinks import tools
cf.go_offline()
import plotly.graph_objs as go
import wbgapi as wb

import streamlit as st

st.title('Selected Market Prices.')


tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Currency Pairs NZ", "Currency Pairs UK", "Oil & Gas", 
    "Ruble", "Interest Rates", "GDP per Capita"])


with tab1:
    st.header("Currency Pairs NZ")
    tickers =['GBPNZD=X', 'USDNZD=X', 'AUDNZD=X', 'NZDJPY=X']
    currency=tickers
    start='2020-01-01'
    end=date.today()

    df =  yf.download(tickers, start, end)['Adj Close']
    # fig = df.iplot(asFigure=True, xTitle="Time",
    #         yTitle="Prices", title="Currency Prices")

    fig = go.Figure(**tools.merge_figures([df.figure(columns=['GBPNZD=X', 'USDNZD=X', 'AUDNZD=X']), df.figure(columns=['NZDJPY=X'], color='red')])).set_axis(['NZDJPY=X'], side='right')
    fig['layout'].update(title='Currency Prices')

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

with tab4:
    st.header("Russian Ruble vs USD")
    tickers = tickers = ['RUBUSD=X']
    currency=tickers
    start='2020-01-01'
    end=date.today()

    df =  yf.download(tickers, start, end)['Adj Close']
    fig4 = df.iplot(asFigure=True, xTitle="Time", yTitle="Prices", title="Currency Prices")
    st.plotly_chart(fig4, use_container_width=True)   

with tab5:
    st.header("Inflation Rates")
    data = pd.read_html('https://en.wikipedia.org/wiki/List_of_countries_by_inflation_rate')
    table = data[1].set_index('Country (or Territory)')['Inflation rate (consumer prices) (%)']
    array = ['Australia', 'New Zealand', 'Austria', 'Germany', 'France', 'United Kingdom', 'Spain', 'Portugal', 'United States', 'Russia', 'Italy', 'Netherlands', 'Sweden']
    df = table.reset_index().loc[table.reset_index()['Country (or Territory)'].isin(array)]
    df = df.set_index('Country (or Territory)')
    fig5 = df['Inflation rate (consumer prices) (%)'].iplot(asFigure=True, kind='bar', title='Inflation Rates  2021')
    st.plotly_chart(fig5, use_container_width=True)   

with tab6:
    st.header("GDP/Capita Europe")
    gdppercap=wb.data.DataFrame('NY.GDP.PCAP.CD', wb.region.members('EMU'))
    fig6 = gdppercap.iloc[:,-6:].iplot(asFigure=True, kind='bar', title='GDP per Capita in Europe')
    st.plotly_chart(fig6, use_container_width=True)   