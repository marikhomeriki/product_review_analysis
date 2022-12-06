import requests
import streamlit as st
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from prod_rev_analysis.ml_logic.data import load_data_w2v, cleaning_w2v
from prod_rev_analysis.ml_logic.model_w2v import neg_word2v, pos_word2v
from prod_rev_analysis.ml_logic.absa import get_sent_asps
import nltk

# from streamlit_lottie import st_lottie
import time
import datetime
import requests
from PIL import Image
import base64
import pandas as pd
import altair as alt
import subprocess
from prod_rev_analysis.data_sources.data_scarping import hello_world,get_data_yelp

from prod_rev_analysis.ml_logic.data import load_data_wordcloud, clean_data


from prod_rev_analysis.interface.main import pred
from prod_rev_analysis.ml_logic import model_w2v


import webbrowser

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('corpus')
nltk.download('omw-1.4')


st.set_page_config(page_title="My Webpage", page_icon= "tada", layout= "wide")

st.markdown ("""
    <style>
    .title{
        font-size:1006px;
        }
    </style>
    """,unsafe_allow_html=True)

st.title("Product Review Analysis")
# st.markdown("<h1 style='text-align: center;'>Product Review Analysis</h1>",unsafe_allow_html= True)

with st.container():
    left_col,mid_col,right_col = st.columns(3)
    with left_col:
        st.header("By Mariami Khomeriki, Ankur Kaushal, Mathias Freisleben\
            , Arun Appulingam")


    # with right_col:
        # file = open("/Users/arun._.appulingam/code/ezgif-4-21e05539a6.gif", 'rb')
        # contents = file.read()
        # data_url = base64.b64encode(contents).decode('utf-8-sig')
        # file.close()
        # st.markdown(f'<img src="data:image/gif;base64,{data_url}">',unsafe_allow_html = True)

st.write("---")
st.markdown("# Introduction 📈")
st.sidebar.markdown("# Page 1: 📈")
st.header("Main Tasks")

st.write("This project is based around..........")

st.write("We divided the task in this were split within the group:")
st.write ("Mari:")
st.write ("Ankur:")
st.write ("Mathias:")
st.write ("Arun: Creating a Sequential and CNN base model, helped clean data, using Streamline to make this website :)")

st.write("---")
st.markdown("# Running the Data 😮")
st.sidebar.markdown("# Page 2: 😮")

# data_url=('/Users/arun._.appulingam/code/marikhomeriki/product_review_analysis/raw_data/train.csv')
# @st.cache(persist=True)

# def load_data():
#     data=pd.read_csv(data_url)
#     return data

# review_data=load_data()
st.markdown("#### Step 1:")

st.write("**`Get Review From :`**")

st.markdown("<h2 style='text-align: center;'>Choose One:</h2>",unsafe_allow_html= True)
column1,column2,column3 = st.columns(3)
with column1:
    # st.image('/Users/arun._.appulingam/code/rsz_1googleimage.png')
    google = column1.checkbox('Google')

with column2:
    # st.image('/Users/arun._.appulingam/code/rsz_1yelp-image.png')
#     column2.write(f"`Yelp`")
    yelp = column2.checkbox('Yelp')

with column3:
    # st.image('/Users/arun._.appulingam/code/rsz_602e2fe1d9ced200045a5771.png')
#     column3.write('')
    trust_pilot = column3.checkbox('TrustPilot')

number_of_pages = st.slider("**`Number of Pages:`**", 0, 40, 20, step=1)

form = st.form("form", clear_on_submit=True)
with form:
    url = st.text_input("**`Give the URL link:`**", None)


# path = ''
# outlet_df = pd.read_csv(path)

    number_of_pages = st.slider("**`Number of Pages:`**", 0, 40, 2, step=1)

    st.markdown("<h2 style='text-align: center;'>Choose One:</h2>",unsafe_allow_html= True)
    column1,column2,column3 = form.columns(3)
    with column1:
        # st.image('/Users/arun._.appulingam/code/rsz_1googleimage.png')
        google = column1.checkbox('Google')

    with column2:
        # st.image('/Users/arun._.appulingam/code/rsz_1yelp-image.png')
    #     column2.write(f"`Yelp`")
        yelp = column2.checkbox('Yelp')

    with column3:
        # st.image('/Users/arun._.appulingam/code/rsz_602e2fe1d9ced200045a5771.png')
    #     column3.write('')
        trust_pilot = column3.checkbox('TrustPilot')

    flag = True
    if (url is not None) and ((google and not yelp and not trust_pilot)\
        or (not google and yelp and not trust_pilot) or (not google and not yelp and trust_pilot)):
        flag = True
    else:
        flag = False

    submit = form.form_submit_button("Submit Now", disabled=False)
    st.info("**Choose an option using the boxes.**")

    if submit:

        # check if url value is empty / if box is empty (or the default values)
        if url == "None" or url == '':
                    st.write("missing information, please fill out")
        # return the st.write that contains the intended message (i.e. please fill in missing info )
        elif 'https://www.yelp.' not in url:
                    st.write("this is not a Yelp file, please try again")
        else:
            output = get_data_yelp(url, pages = number_of_pages)
            st.write(yelp, output)
            st.balloons()


# st.markdown("#### Step 2:")

        # check if url value is empty / if box is empty (or the default values)
        if url == "None" or url == '':
                    st.write("missing information, please fill out")
        # return the st.write that contains the intended message (i.e. please fill in missing info )
        elif 'https://www.yelp.' not in url:
                    st.write("this is not a Yelp file, please try again")
        else:
            output = get_data_yelp(url)
            st.write(yelp, output)
            st.balloons()


st.write('---')

st.markdown("#### Step 3:")

c1,c2,c3 = st.columns(3)
with c2:
        csv = st.file_uploader("If data does not input, upload the CSV file")

        if csv is not None and csv.type == 'text/csv':
            df = pd.read_csv(csv)
            st.write(df)
        elif csv is not None and csv.type != 'text/csv':
            st.write('Not a CSV file')

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

# if url is None:
#     "You missed out information"
# elif form is None:
#     return "You missed out information"
# else:
#     return x


# source = pd.DataFrame({
#         "Price ($)": [10, 15, 20],
#         "Month": ["January", "February", "March"]
#       })
# st.write("---")
# bar_chart = alt.Chart(source).mark_bar().encode(
#     x="sum(Price ($)):Q",
#     y=alt.Y("Month:N", sort="-x")
#     )

# st.altair_chart(bar_chart, use_container_width=True)


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



st.markdown("# Graphs and Review Data 📊")
st.sidebar.markdown("# Page 3: 📊")

counter = dict(pred())

counter = pd.DataFrame.from_dict(counter, orient ='index')
st.bar_chart(counter)

data = load_data_wordcloud()
full_text = ' '.join(data['text'])
wordcloud = WordCloud().generate(full_text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
st.pyplot()


# cloud_no_stopword = WordCloud(background_color='black', stopwords=my_stop_words).generate(full_text)
# plt.imshow(cloud_no_stopword, interpolation='bilinear')
# plt.axis('off')
# plt.show()

c1,c2= st.columns(2)
with c1:
    data_w2v = load_data_w2v()
    words2v = neg_word2v(data_w2v)
    st.write(words2v)
    st.bar_chart(words2v)
with c2:
    data_w2v = load_data_w2v()
    words2v_pos = pos_word2v(data_w2v)
    st.write(words2v_pos)
    st.bar_chart(words2v_pos)

sent_asp_distribution = get_sent_asps()
st.write(sent_asp_distribution)

st.bar_chart(sent_asp_distribution)
