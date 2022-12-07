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

original_title = '<b style="text-align:center; color:black; font-size: 70px;">Product Review Analysis</b>'
st.markdown(original_title, unsafe_allow_html=True)

st.sidebar.markdown("# What is a Review Analysis?")
st.sidebar.markdown("Review analysis is the act of going through customer\
        and product reviews from a number of different channels and uncovering \
        insights. These insights can then be used to improve products and \
        services, create new ones, or enhance the overall customer experience.")
st.sidebar.write("---")
x = st.sidebar.slider('Rate this website:',0,5)
if x==1:
    st.sidebar.markdown("⭐")
if x==2:
    st.sidebar.markdown("⭐⭐")
if x==3:
    st.sidebar.markdown("⭐⭐⭐")
if x==4:
    st.sidebar.markdown("⭐⭐⭐⭐")
if x==5:
    st.sidebar.markdown("⭐⭐⭐⭐⭐")

y = st.sidebar.text_area("Feedback:",max_chars=250)
st.sidebar.write("---")
z = st.sidebar.button("Submit")


with st.container():
    left_col,mid_col,right_col = st.columns(3)
    with left_col:
        st.header("By Mariami Khomeriki, Ankur Kaushal, Mathias Freisleben\
        , Arun Appulingam")

    with right_col:
        file = open("/Users/arun._.appulingam/code/ezgif-4-21e05539a6.gif", 'rb')
        contents = file.read()
        data_url = base64.b64encode(contents).decode('utf-8-sig')
        file.close()
        st.markdown(f'<img src="data:image/gif;base64,{data_url}">',unsafe_allow_html = True)


tab1,tab2,tab3,tab4 = st.tabs(["Introduction 📈","Running the Data 😮","Backup Data 🔙"\
    ,"Review on Website🌐"])

with tab1:
    st.markdown("# Introduction 📈")


    st.header("Main Tasks")

    st.write("This aim of this project is to ........")

    st.write("We divided the task in this were split within the group:")
    st.write ("Mari:")
    st.write ("Ankur:")
    st.write ("Mathias:")
    st.write ("Arun: Creating a Sequential and CNN base model, helped clean data, using Streamline to make this website :)")


with tab2:
    st.markdown("# Running the Data 😮")

    st.markdown("### Step 1:")
    # st.markdown("#### Get Review From:")
    st.write("#### **`Get Review From :`**")

    st.markdown("<h3 style='text-align: center;color:grey;'>Choose One:</h3>",unsafe_allow_html= True)
    column1,column2,column3,column4,column5 = st.columns(5)
    # with column1:
    #     st.image('/Users/arun._.appulingam/code/rsz_1googleimage.png')
    #     google = column1.checkbox('Google')

    with column2:
        st.image('/Users/arun._.appulingam/code/rsz_1yelp-image.png')
        yelp = column2.checkbox('Yelp')

    with column4:
        st.image('/Users/arun._.appulingam/code/rsz_602e2fe1d9ced200045a5771.png')
        trust_pilot = column4.checkbox('TrustPilot')

    st.info("**Choose an option using the boxes.**")

    st.write('---')

    st.markdown("### Step 2:")

    form = st.form("form", clear_on_submit=True)
    with form:
        url = st.text_input(" **`Give the URL link:`**", None)

        number_of_pages = st.slider(" **`Number of Pages:`**", 0, 40, 2, step=1)

        flag = True
        if (url is not None) and ((not yelp and not trust_pilot)\
            or (yelp and not trust_pilot) or (not yelp and trust_pilot)):
            flag = True
        else:
            flag = False

        submit = form.form_submit_button("Submit Now", disabled=False)

        if submit:

            if yelp:
                if url == "None" or url == '':
                            st.write("missing information, please fill out")

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

                elif 'https://uk.trustpilot' not in url:
                            st.write("this is not a Trustpilot file, please try again")

                else:
                    output = get_data_trustpilot(url, pages = number_of_pages)
                    output[0].to_csv("temp.csv")
                    st.balloons()
                    st.write("Review count: ", output[1])
                    st.write("Average score: ", output[2])

                    st.markdown("# Graphs and Review Data 📊")

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
    # if submit:

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
    st.markdown("#### Image of the most frequently used words:")
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

with tab3:
    st.markdown("# Backup Data🔙")

    st.markdown("### If either Yelp or TrustPilot link is unable to collect data,\
        upload the CSV file here:")

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
with tab4:

    st.markdown("# Reviews on Website🌐")

    if z:
        if x == 0 or y == '':
            st.sidebar.write("Missing a section of the feedback...")
        else:
            st.sidebar.write("Thanks for the feedback!")
            print(f"{x}:{y}")
