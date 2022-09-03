import requests
import streamlit as st
import yfinance as yf
import streamlit.components.v1 as components
from requests_html import HTMLSession




st.set_page_config('Home',":shark:","wide",menu_items={'About': "This is an *extremely* cool app!"})



menu=['Registeration form by streamlit','Online register step by step','Registeration form by component,Html']
ch=st.sidebar.selectbox('Menu',menu)











if ch == 'Registeration form by streamlit':
    st.title('Registration form')


    st.subheader('Customer information')
    ct = ['Private','Business']
    ctype = st.selectbox('Customer type', ct)



    if ctype == 'Private' :

        cemail = st.text_input('Email')

        rcemail = st.text_input('Repeat Email')
        if cemail != rcemail :
            st.warning('Email does not match')
        else:
            st.success('Please note that it is very important that your email is correct, as all communication and invoices will be sent by email.')

        cname = st.text_input('Name and family name')

        caddress = st.text_input('Address')


        cpcode = st.text_input('Postal code')


        ccity = st.text_input('City')


        cphone = st.text_input('Phone')


    else:

        cemail = st.text_input('Email')

        rcemail = st.text_input('Repeat Email')
        if cemail != rcemail :
            st.warning('Email does not match')
        else:
            st.success('Please note that it is very important that your email is correct, as all communication and invoices will be sent by email.')

        ccvr = st.text_input('CVR number')


        company = st.text_input('Company name')


        caddress = st.text_input('Address')


        cpcode = st.text_input('Postal code')


        ccity = st.text_input('City')


        cphone = st.text_input('Phone')


    st.subheader('Subscription')
    pack=st.radio('package', ['Gold','silver','bronz'],horizontal=True)
    if 'Gold' in pack:
        st.success('Kr. 1185.00 årligt inkl. moms')
    if 'silver' in pack:
        st.success('885.00 årligt inkl. moms')
    if 'bronz' in pack:
        st.success('585.00 årligt inkl. moms')

    goog=st.radio('include google map', ['Yes','No'],horizontal=True)
    if 'Yes' in goog:
        st.success('Kr. 75.00 årligt inkl. moms')

    alarm=st.radio('include alarmcentral', ['Yes','No'],horizontal=True)
    if 'Yes' in alarm:
        st.success('Tilvælg alarmcentral + 400.00 årligt inkl. moms')
        ins=['Topdanmark Forsikring A/S','Tryg Forsikring A/S','ALG Europe','Alka Forsikring','Alm. Brand Forsikring A/S','Andet']    
        ins2=st.selectbox('Insurance company',ins)


    st.subheader('Vehicle')

    plate = st.text_input('Registration Plate')

    brand = st.text_input('Brand')

    model = st.text_input('Model')

    year = st.text_input('Year')


    submitted = st.button("Submit")












if ch == 'Online register step by step':
    st.title('Online Bestil forsikringstracker')

    st.subheader('Customer information')

    ct = ['--Select--','Private','Business']
    ctype = st.selectbox('Customer type', ct)
    if '--Select--' in ctype:
        st.stop()

    cemail = st.text_input('Email')
    if not cemail:
        st.stop()

    rcemail = st.text_input('Repeat Email')
    if not rcemail:
        st.stop()

    if cemail != rcemail :
        st.warning('Email does not match')
        st.stop()
    else:
        st.success('We will send login infomation to this email.')



    if ctype == 'Private' :

        cname = st.text_input('Name and family name')
        if not cname:
            st.stop()

        caddress = st.text_input('Address')
        if not caddress:
            st.stop()

        cpcode = st.text_input('Postal code')
        if not cpcode:
            st.stop()

        ccity = st.text_input('City')
        if not ccity:
            st.stop()

        cphone = st.text_input('Phone')
        if not cphone:
            st.stop()

    else:
        ccvr = st.text_input('CVR number')
        if not ccvr:
            st.stop()

        company = st.text_input('Company name')
        if not company:
            st.stop()

        caddress = st.text_input('Address')
        if not company:
            st.stop()

        cpcode = st.text_input('Postal code')
        if not cpcode:
            st.stop()

        ccity = st.text_input('City')
        if not ccity:
            st.stop()

        cphone = st.text_input('Phone')
        if not cphone:
            st.stop()


    st.subheader('Subscription')
    pack=st.radio('package', ['Gold','silver','bronz','<--- choose'],horizontal=True,index=3)
    if '<--- choose' in pack:
        st.stop()
    if 'Gold' in pack:
        st.success('Kr. 1185.00 årligt inkl. moms')
    if 'silver' in pack:
        st.success('885.00 årligt inkl. moms')
    if 'bronz' in pack:
        st.success('585.00 årligt inkl. moms')

    goog=st.radio('include google map', ['Yes','No','<--- choose'],horizontal=True,index=2)
    if '<--- choose' in goog:
        st.stop()
    if 'Yes' in goog:
        st.success('Kr. 75.00 årligt inkl. moms')

    alarm=st.radio('Include alarmcentral', ['Yes','No','<--- choose'],horizontal=True,index=2)
    if '<--- choose' in alarm:
        st.stop()
    if 'Yes' in alarm:
        st.success('Tilvælg alarmcentral + 400.00 årligt inkl. moms')
        ins=['--Select--','Topdanmark Forsikring A/S','Tryg Forsikring A/S','ALG Europe','Alka Forsikring','Alm. Brand Forsikring A/S','Andet']    

        ins2=st.selectbox('Your car insurance company',ins)
        if ins2 == '--Select--':
            st.stop()

    st.subheader('Vehicle')

    plate = st.text_input('Registration Plate')
    if not plate:
        st.stop()

    brand = st.text_input('Brand')
    if not brand:
        st.stop()

    model = st.text_input('Model')
    if not model:
        st.stop()


    year = st.text_input('Year')
    if not year:
        st.stop()


    subm=st.button('Send')
    if subm:
        st.write('Check your email to continue')










if ch == 'Registeration form by component,Html':

    #define css




    #define html
    components.html("""
    <!doctype html>

    <html>
    <head>

    </head>
    <script language="Javascript">
    function hideA(x) {
        if (x.checked) {
        document.getElementById("A").style.display = "none";
        document.getElementById("B").style.display = "initial";
        document.getElementById('option1').checked = true;
        }
    }

    function hideB(x) {
        if (x.checked) {
        document.getElementById("B").style.display = "none";
        document.getElementById("A").style.display = "initial";
        document.getElementById('option4').checked = true;
        }
    }

    </script>

    <body>
    <h1>Tilmeldingsformular</h1>




    <div id="A">

    <form method="post" >
    Status:
    <input type="radio" name="c"  id='option1' onchange="hideB(this)"  value="1"  checked="checked" >Ny kunde
    <input type="radio" name="c"  id='option2' onchange="hideA(this)" value="2"> Eksisterende kunde
    <br><br>
    <input type="text" placeholder="Fornavn og Efternavn*" name="name" required  minlength="4"/>
    <br><br>
    <input type="text" placeholder="Firmanavn" name="firma" />
    <br><br>
    <input type="email" placeholder="E-mail*" name="email" required/>
    <br><br>
    <input type="text" placeholder="Telefonnummer" name="tlf" />
    <br><br>
    <input type="text" placeholder="Post nr" name="post" />
    <br><br>
    <input type="text" placeholder="By" name="city" />
    <br><br>
    <input type="text" placeholder="Adresse" name="address" />
    <br><br>
    <input type="text" placeholder="Nummerplade*" name="plate" required  minlength="4"/>
    <br><br>
    <input type="text" placeholder="Mærke" name="mark" />
    <br><br>
    <input type="text" placeholder="Model" name="model" />
    <br><br>
    <input type="text" placeholder="Årgang" name="year" />
    <br><br>

    Abonnement:      <input type="radio" name="s" id="f"  value="1" checked="checked"> ULTIMATE
    <input type="radio" name="s" id="k"  value="2"> PREMIUM
    <input type="radio" name="s" id="p"  value="3"   > BASIC
    <br><br>

    <input type="text" placeholder="IMEI nr.*" name="imei" required/>
    <br><br>

    Enhed model:      <input type="radio" name="m"   value="1" checked="checked"> GT06E
    <!-- <input type="radio" name="m"   value="2"> GV20
    <input type="radio" name="m"   value="3"   > ET25
    <input type="radio" name="m"   value="9"  checked="checked" > Unknown-->
    <br><br>



    <input type=submit value=Opret>
    </form>
    </div>



    <div id="B" style="display:none">
    <form method="post">
    Status:
    <input type="radio" name="c"  id='option3' onchange="hideB(this)"  value="1"   >Ny kunde
    <input type="radio" name="c"  id='option4' onchange="hideA(this)" value="2" checked="checked" > Eksisterende kunde
    <br><br>
    <input type="email" placeholder="E-mail*" name="email" required/>
    <br><br>
    <input type="text" placeholder="Nummerplade*" name="plate" required  minlength="4"/>
    <br><br>
    <input type="text" placeholder="Mærke" name="mark" />
    <br><br>
    <input type="text" placeholder="Model" name="model" />
    <br><br>
    <input type="text" placeholder="Årgang" name="year" />
    <br><br>
    <input type="text" placeholder="IMEI nr.*" name="imei" required/>
    <br><br>

    Enhed model:      <input type="radio" name="m"   value="1" checked="checked"> GT06E
    <!--<input type="radio" name="m"   value="2"> GV20
    <input type="radio" name="m"   value="3"   > ET25
    <input type="radio" name="m"   value="9"   > Unknown-->
        <br><br>
    <input type=submit value=Opret>
    </form>
    </div>


    </body>
    </html>
    """, height=1000)
