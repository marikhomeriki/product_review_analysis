import requests
import streamlit as st
 # from streamlit_lottie import st_lottie
import pandas as pd
import time
import datetime
import requests
from PIL import Image
import base64

st.set_page_config(page_title="My Webpage", page_icon= "tada", layout= "wide")

st.markdown("<h1 style='text-align: center;'>Product Review Analysis</h1>",unsafe_allow_html= True)

with st.container():
    left_col,mid_col,right_col = st.columns(3)
    with left_col:
        st.header("By Mariami Khomeriki, Ankur Kaushal, Mathias Freisleben, Arun Appulingam")

    with right_col:
        file = open("/Users/arun._.appulingam/code/ezgif-4-21e05539a6.gif", 'rb')
        contents = file.read()
        data_url = base64.b64encode(contents).decode('utf-8-sig')
        file.close()
        st.markdown(f'<img src="data:image/gif;base64,{data_url}">',unsafe_allow_html = True)

st.write("---")
st.markdown("# Introduction 📈")
st.sidebar.markdown("# Page 1: 📈")
st.header("Main Tasks")

st.write("This project is based around..........")

st.write("We divided the task in this were split within the group:")
st.write ("Mari:")
st.write ("Ankur:")
st.write ("Mathias:")
st.write ("Arun: Making a sexy ass website :)")

st.write("---")
st.markdown("# Inputting the Data 📊")
st.sidebar.markdown("# Page 2: 📊")

data_url=('/Users/arun._.appulingam/code/marikhomeriki/product_review_analysis/raw_data/train.csv')
@st.cache(persist=True)

def load_data():
    data=pd.read_csv(data_url)
    return data

review_data=load_data()
st.markdown("#### Step 1:")
url = st.text_input("** `Give the URL link :` **", None)

st.write("Or")
company_name = st.text_input("** `Give the CompanyID :` **", None)

st.markdown("#### Step 2:")
st.write("** `Get Review From :` **")
form = st.form("form", clear_on_submit=True)
with form:
    st.markdown("<h2 style='text-align: center;'>Choose One:</h2>",unsafe_allow_html= True)
    column1,column2,column3 = form.columns(3)
    with column1:
        st.image('/Users/arun._.appulingam/code/rsz_1googleimage.png')
        google = column1.checkbox('Google')

    with column2:
        st.image('/Users/arun._.appulingam/code/rsz_1yelp-image.png')
     #     column2.write(f"`Yelp`")
        yelp = column2.checkbox('Yelp')

    with column3:
        st.image('/Users/arun._.appulingam/code/rsz_602e2fe1d9ced200045a5771.png')
     #     column3.write('')
        trust_pilot = column3.checkbox('TrustPilot')

    flag = True
    if (url is None and form is not None) or (url is not None and form is None):
        flag = True
    else:
        flag=False

    submit = form.form_submit_button("Submit Now", disabled=flag)
    st.info("**Choose an option using the boxes.**")

c1,c2,c3 = st.columns(3)
with c2:
    st.button("GIVE ME ANALYSIS")
    button_style = """
    <style>
    .stButton > button {
        color:black;
        text-align:center;
        width:200px;
        height:55px;
    }
    </style>
    """
    st.markdown(button_style,unsafe_allow_html=True)

 # if url is None:
 #     "You missed out information"
 # elif form is None:
 #     return "You missed out information"
 # else:
 #     return x

 # if submit:
 #     list_values = [int(i) for i in values]
 #     if sum(list_values) == 0:
 #         st.error("**Choose an option!**")
 #         time.sleep(1)
 #         st.experimental_rerun()


 # def get_total_dataframe(dataset):
 #     total_dataframe = pd.DataFrame({
