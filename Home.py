import requests
import streamlit as st
import yfinance as yf
import streamlit.components.v1 as components
from requests_html import HTMLSession
from streamlit_lottie import st_lottie

st.set_page_config('Home',":shark:","wide",menu_items={'About': "This is an *extremely* cool app!"})



x=requests.get('https://assets3.lottiefiles.com/packages/lf20_jtbfg2nb.json')
r=x.json()




with st.container():
    st.subheader('Hi, I am Daniel  :wave:')
    st.title('A Data Analyst From Denmark')
    st.write('This is a homepage to run and test different python scripts!')


with st.container():
    st.write('---')
    lc , rc =st.columns(2)
    with lc:
        st.header('What i do')
        st.write('##')
        st.write('''
                 - 1111111111111111111
                 - 2222222222222222222
                 - 3333333333333333333
                 ''')
    with rc:
        st_lottie(r,height=300)




