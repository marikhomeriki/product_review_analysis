import requests
import streamlit as st
# from streamlit_lottie import st_lottie
import time
import datetime
import requests
from PIL import Image
import base64
import pandas as pd



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
url = st.text_input("**`Give the URL link:`**", None)

st.write("Or")
company_name = st.text_input("**`Give the CompanyID:`**", None)

st.markdown("#### Step 2:")
st.write("**`Get Review From :`**")
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
#     'Status':['Confirmed', 'Recovered', 'Deaths','Active'],
#     'Number of cases':(dataset.iloc[0]['confirmed'],
#     dataset.iloc[0]['recovered'],
#     dataset.iloc[0]['deaths'],dataset.iloc[0]['active'])})
#     return total_dataframe

# state_total = get_total_dataframe(state_data)

# if st.sidebar.checkbox("Show Analysis by State", True, key=2):
#     st.markdown("## **State level analysis**")
#     st.markdown("### Overall Confirmed, Active, Recovered and " +
#     "Deceased cases in %s yet" % (select))
#     if not st.checkbox('Hide Graph', False, key=1):
#         state_total_graph = px.bar(
#         state_total,
#         x='Status',
#         y='Number of cases',
#         labels={'Number of cases':'Number of cases in %s' % (select)},
#         color='Status')
#         st.plotly_chart(state_total_graph)




# with st.form(key='params_for_api'):

#     pickup_date = st.date_input('pickup datetime', value=datetime.datetime(2012, 10, 6, 12, 10, 20))
#     pickup_time = st.time_input('pickup datetime', value=datetime.datetime(2012, 10, 6, 12, 10, 20))
#     pickup_datetime = f'{pickup_date} {pickup_time}'
#     pickup_longitude = st.number_input('pickup longitude', value=40.7614327)
#     pickup_latitude = st.number_input('pickup latitude', value=-73.9798156)
#     dropoff_longitude = st.number_input('dropoff longitude', value=40.6413111)
#     dropoff_latitude = st.number_input('dropoff latitude', value=-73.7803331)
#     passenger_count = st.number_input('passenger_count', min_value=1, max_value=8, step=1, value=1)

#     st.form_submit_button('Make prediction')

# params = dict(
#     pickup_datetime=pickup_datetime,
#     pickup_longitude=pickup_longitude,
#     pickup_latitude=pickup_latitude,
#     dropoff_longitude=dropoff_longitude,
#     dropoff_latitude=dropoff_latitude,
#     passenger_count=passenger_count)

# wagon_cab_api_url = 'https://taxifare.lewagon.ai/predict'
# response = requests.get(wagon_cab_api_url, params=params)

# prediction = response.json()

# pred = prediction['fare']

# st.header(f'Fare amount: ${round(pred, 2)}')
