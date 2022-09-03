import requests
import streamlit as st
import yfinance as yf
import streamlit.components.v1 as components
from requests_html import HTMLSession





st.set_page_config('Sport',":soccer:","wide",menu_items={'About': "This is an *extremely* cool app!"})


menu=['From varzesh3.ir']
ch=st.sidebar.selectbox('Menu',menu)


if 'From varzesh3.ir' in ch:
    st.title('Sport news')
    ti=st.text_input('Search')
    if len(ti)>0:
        r=requests.get('https://search-api.varzesh3.com/v1.0/query?q='+ti)
        x=r.json()
        for i in x['news']:
            with st.container():
                st.success(i['publishedOn'])
                st.subheader(i['title'])
                st.write(i['shortDescription'])
                st.image(i['picture'])
                st.write('---')
