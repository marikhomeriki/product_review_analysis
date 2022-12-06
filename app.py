import streamlit as st
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from prod_rev_analysis.ml_logic.data import load_data_w2v, cleaning_w2v
from prod_rev_analysis.ml_logic.model_w2v import neg_word2v, pos_word2v
import altair as alt
import os


# from streamlit_lottie import st_lottie
import time
import datetime
import requests
from PIL import Image
import base64
import pandas as pd
import altair as alt
import subprocess
from prod_rev_analysis.data_sources.data_scarping import get_data_yelp
from prod_rev_analysis.data_sources.data_scarping import get_data_trustpilot
from prod_rev_analysis.ml_logic.data import load_data_wordcloud, clean_data


from prod_rev_analysis.interface.main import pred
from prod_rev_analysis.ml_logic import model_w2v


import webbrowser

output = 0

st.set_page_config(page_title="My Webpage", page_icon= "tada", layout= "wide")

original_title = '<b style="font-family:serif; text-align:center; color:black; font-size: 70px;">Product Review Analysis</b>'
st.markdown(original_title, unsafe_allow_html=True)

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

st.write("This aim of this project is to ........")

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
st.markdown("### Step 1:")

st.write("**`Get Review From :`**")

st.markdown("<h3 style='text-align: center;'>Choose One:</h3>",unsafe_allow_html= True)
column1,column2 = st.columns(2)
# with column1:
#     st.image('/Users/arun._.appulingam/code/rsz_1googleimage.png')
#     google = column1.checkbox('Google')

with column1:
    st.image('/Users/arun._.appulingam/code/rsz_1yelp-image.png')
    yelp = column1.checkbox('Yelp')

with column2:
    st.image('/Users/arun._.appulingam/code/rsz_602e2fe1d9ced200045a5771.png')
#     column3.write('')
    trust_pilot = column2.checkbox('TrustPilot')

st.info("**Choose an option using the boxes.**")

st.write('---')

st.markdown("### Step 2:")

form = st.form("form", clear_on_submit=True)
with form:
    url = st.text_input("**`Give the URL link:`**", None)


# path = ''
# outlet_df = pd.read_csv(path)

    number_of_pages = st.slider("**`Number of Pages:`**", 0, 40, 2, step=1)

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
        # column2.write(f"`Yelp`")
        yelp = column2.checkbox('Yelp')

    with column3:
        # st.image('/Users/arun._.appulingam/code/rsz_602e2fe1d9ced200045a5771.png')
        # column3.write('')
        trust_pilot = column3.checkbox('TrustPilot')


    flag = True
    if (url is not None) and ((not yelp and not trust_pilot)\
        or (yelp and not trust_pilot) or (not yelp and trust_pilot)):
        flag = True
    else:
        flag = False

    submit = form.form_submit_button("Submit Now", disabled=False)

    if submit:

        # check if url value is empty / if box is empty (or the default values)
        if yelp:
            if url == "None" or url == '':
                        st.write("missing information, please fill out")
            # return the st.write that contains the intended message (i.e. please fill in missing info )
            elif 'https://www.yelp.' not in url:
                        st.write("this is not a Yelp file, please try again")
            else:
                output = get_data_yelp(url, pages = number_of_pages)
                st.balloons()
                st.write("Review count: ", output[1])
                st.write("Average score: ", output[2])

                st.markdown("# Graphs and Review Data 📊")
                st.sidebar.markdown("# Page 3: 📊")
                output[0].to_csv("temp.csv")
                counter = pred(output[0])
                st.markdown("#### Negative vs. Positive Reviews:")
                counter = pd.DataFrame.from_dict(counter, orient ='index')
                st.bar_chart(counter)


                data = load_data_wordcloud()
                full_text = ' '.join(data['text'])
                wordcloud = WordCloud().generate(full_text)

                # Display the generated image:
                st.markdown("#### Mariami's picture thingy:")
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
                    st.markdown("#### Negative words:")
                    words2v = neg_word2v(output[0])
                    words2v.reset_index(inplace = True)
                    words2v.columns = ["Words", "Scores"]
                    st.write(words2v)
                    st.altair_chart(alt.Chart(words2v).mark_bar(color='red',
                    ).encode(
                    x='Words',
                    y='Scores'
                ))
                    # st.bar_chart(words2v)

                with c2:
                    st.markdown("#### Positive words:")
                    # data_w2v = load_data_w2v()
                    words2v_pos = pos_word2v(output[0])
                    words2v_pos.reset_index(inplace = True)
                    words2v_pos.columns = ["Words", "Scores"]
                    st.write(words2v_pos)
                    st.altair_chart(alt.Chart(words2v_pos).mark_bar(color='green',
                    ).encode(
                    x='Words',
                    y='Scores'))



        if trust_pilot:
            if url == "None" or url == '':
                        st.write("missing information, please fill out")
            # return the st.write that contains the intended message (i.e. please fill in missing info )
            elif 'https://uk.trustpilot' not in url:
                        st.write("this is not a Trustpilot file, please try again")
            else:
                output = get_data_trustpilot(url, pages = number_of_pages)
                output[0].to_csv("temp.csv")
                st.balloons()
                st.write("Review count: ", output[1])
                st.write("Average score: ", output[2])

                st.markdown("# Graphs and Review Data 📊")
                st.sidebar.markdown("# Page 3: 📊")

                counter = pred(output[0])
                st.markdown("#### Negative vs. Positive Reviews:")
                counter_df = pd.DataFrame.from_dict(counter, orient ='index')
                print(counter_df)
                st.bar_chart(counter_df)


                # data = load_data_wordcloud(counter_df)
                full_text = ' '.join(output[0]['text'])
                wordcloud = WordCloud().generate(full_text)

                # Display the generated image:
                st.markdown("#### Mariami's picture thingy:")
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
                    st.markdown("#### Negative words:")
                    #data_w2v = load_data_w2v()
                    words2v = neg_word2v(output[0])
                    words2v.reset_index(inplace = True)
                    words2v.columns = ["Words", "Scores"]
                    st.write(words2v)
                    st.altair_chart(alt.Chart(words2v).mark_bar(color='red',
                    ).encode(
                    x='Words',
                    y='Scores'
                ))
                    # st.bar_chart(words2v)


                with c2:
                    st.markdown("#### Positive words:")
                    #data_w2v = load_data_w2v()
                    words2v_pos = pos_word2v(output[0])
                    words2v_pos.reset_index(inplace = True)
                    words2v_pos.columns = ["Words", "Scores"]
                    st.write(words2v_pos)
                    st.altair_chart(alt.Chart(words2v_pos).mark_bar(color='green',
                    ).encode(
                    x='Words',
                    y='Scores'))


st.write('---')

st.markdown("### Step 3 (Optional):")

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

# state_total = get_total_dataframe(state_data


# counter = dict(pred())


# if submit:

#     st.markdown("# Graphs and Review Data 📊")
#     st.sidebar.markdown("# Page 3: 📊")

# counter = dict(pred(df = output[0]))
output = pd.read_csv("temp.csv")
counter = pred(output)

st.markdown("#### Negative vs. Positive Reviews:")
counter = pd.DataFrame.from_dict(counter, orient ='index')
st.bar_chart(counter)


# data = load_data_wordcloud(df = output)
full_text = ' '.join(output['text'])
wordcloud = WordCloud().generate(full_text)

# Display the generated image:
st.markdown("#### Mariami's picture thingy:")
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
st.pyplot()

c1,c2= st.columns(2)
with c1:
    st.markdown("#### Negative words:")
    # data_w2v = load_data_w2v(df = output)
    words2v = neg_word2v(output)
    words2v.reset_index(inplace = True)
    words2v.columns = ["Words", "Scores"]
    st.write(words2v)
    st.altair_chart(alt.Chart(words2v).mark_bar(color='red',
    ).encode(
    x='Words',
    y='Scores'
))
    # st.bar_chart(words2v)


with c2:
    st.markdown("#### Positive words:")
    # data_w2v = load_data_w2v(df = output)
    words2v_pos = pos_word2v(output)
    words2v_pos.reset_index(inplace = True)
    words2v_pos.columns = ["Words", "Scores"]
    st.write(words2v_pos)
    st.altair_chart(alt.Chart(words2v_pos).mark_bar(color='green',
    ).encode(
    x='Words',
    y='Scores'))
os.remove("temp.csv")
