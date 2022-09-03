import requests
import streamlit as st
import yfinance as yf
import streamlit.components.v1 as components
from requests_html import HTMLSession



st.set_page_config('Home',":shark:","wide",menu_items={'About': "This is an *extremely* cool app!"})


menu=['Game']
ch=st.sidebar.selectbox('Menu',menu)

if ch == 'Game':
    st.title('Good deals from stores below:')
    url = requests.get('https://www.cheapshark.com/api/1.0/stores')
    x = url.json()


    with st.container():
        for i in x:
            st.write(i['storeName'] )
    st.write('---')

    url2 = requests.get('https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=15')
    y = url2.json()

    for j in y:
        with st.container():
            st.write('Game name:   '+j['title'])
            st.write('ID:  '+j['gameID'])
            st.write('New price:  '+j['salePrice'])
            st.write('Old price:  '+j['normalPrice'])
            st.write(j['thumb'])
            st.write('---')
