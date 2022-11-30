import requests
import streamlit as st
# from streamlit_lottie import st_lottie

import datetime
import requests
from PIL import Image
import base64
import pandas as pd



st.set_page_config(page_title="My Webpage", page_icon= "tada", layout= "wide")

st.markdown("# Page 1 🎈")
st.sidebar.markdown("# Page 1 🎈")

st.title("Product Review Analysis")


with st.container():
    left_col,mid_col,right_col = st.columns(3)
    with left_col:
        st.subheader("By Mariami Khomeriki, Ankur Kaushal, Mathias Freisleben, Arun Appulingam")

    with right_col:
        file = open("/Users/arun._.appulingam/code/ezgif-4-21e05539a6.gif", 'rb')
        contents = file.read()
        data_url = base64.b64encode(contents).decode('utf-8-sig')
        file.close()
        st.markdown(f'<img src="data:image/gif;base64,{data_url}">',unsafe_allow_html = True)

st.write("---")
st.header("Main Tasks")

st.write("This project is based around..........")

inp = """We divided the task in this were split within the group:
                Mari:
                Ankur:
                Mathias:
                Arun)"""
st.write(inp)

st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")

data_url=('/Users/arun._.appulingam/code/marikhomeriki/product_review_analysis/raw_data/train.csv')
@st.cache(persist=True)( If you have a different use case where the data does not change so very often, you can simply use this)

def load_data():
    data=pd.read_csv(data_url)
    return data

covid_data=load_data()

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
