import requests
import streamlit as st
import yfinance as yf
import streamlit.components.v1 as components
from requests_html import HTMLSession




st.set_page_config('Crypto',":moneybag:","wide",menu_items={'About': "This is an *extremely* cool app!"})



menu=['Chart']
ch=st.sidebar.selectbox('Menu',menu)

if ch== 'Chart':
    with st.container():
        list_asset = ['BTC-USD', 'ETH-USD', 'DOGE-USD']
        ms = st.multiselect('choose asset', list_asset)
        dates1 = st.date_input('from')
        dates2 = st.date_input('to')
        st.write('---')

    if len(ms) > 0:
        with st.container():
            df = yf.download(ms, dates1, dates2)
            st.write(df)
            df2 = yf.download(ms, dates1, dates2)['Close']
            st.line_chart(df2)