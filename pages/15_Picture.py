import requests
import streamlit as st
import yfinance as yf
import streamlit.components.v1 as components
from requests_html import HTMLSession





st.set_page_config('Picture',":tent:",menu_items={'About': "This is an *extremely* cool app!"})


menu=['Find picture']
ch=st.sidebar.selectbox('Menu',menu)


if 'Find picture' in ch:
    with st.container():
        st.title('Search and download your picturs here!')
        ti=st.text_input('Search')
    if len(ti)>0:
        r=requests.get('https://unsplash.com/napi/search?query='+ti+'&per_page=100&xp=')
        x=r.json()
        for i in x['photos']['results']:
            with st.container():
                lc , rc = st.columns(2)
                with lc:
                    st.image(i['urls']['small'])
                with rc:
                    st.subheader('Download link')
                    st.write(i['links']['download'])
                st.write('---')
