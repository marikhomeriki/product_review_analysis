from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing.text import text_to_word_sequence
import pickle
import os
import string
from nltk.tokenize import word_tokenize

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from tensorflow.keras.preprocessing.text import Tokenizer
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle


def load_data():
    csv_path = os.getcwd() + "/temp_data/data_mc.csv"
    df = pd.read_csv(csv_path, header=None)
    # df = pd.read_csv('../review.csv', header=None)
    df = df.rename({0: 'text'}, axis = 1)
    df = df.dropna()
    df = pd.DataFrame(df.text)

    train_sentences = df['text']


    X = [text_to_word_sequence(_) for _ in train_sentences]

    return X

def load_data_w2v():
    csv_path = os.getcwd() + "/temp_data/data_dishoom.csv"
    df = pd.read_csv(csv_path, header=None)
    # df = pd.read_csv('../review.csv', header=None)
    df= df.rename({1: 'text', 2: 'score'}, axis = 1)
    df = df.dropna()
    df['score'] = df['score'].astype(int)

    return df

def load_data_wordcloud():
    csv_path = os.getcwd() + "/temp_data/data_mc.csv"
    df = pd.read_csv(csv_path, header=None)
    # df = pd.read_csv('../review.csv', header=None)
    df = df.rename({0: 'text'}, axis = 1)
    df = df.dropna()
    df = pd.DataFrame(df.text)

    return df

def clean_data(list) -> np.ndarray:
    """
    clean raw data by tokenizing and padding the reviews
    """
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    df_token = tokenizer.texts_to_sequences(list)

    df_token_pad = pad_sequences(df_token, maxlen=50, dtype='float32', padding="post")

    return df_token_pad


def cleaning_w2v(sentence):

    # Basic cleaning
    sentence = sentence.strip() ## remove whitespaces
    sentence = sentence.lower() ## lowercase
    sentence = ''.join(char for char in sentence if not char.isdigit()) ## remove numbers

    # Advanced cleaning
    for punctuation in string.punctuation:
        sentence = sentence.replace(punctuation, '') ## remove punctuation

    tokenized_sentence = word_tokenize(sentence) ## tokenize
    stop_words = set(stopwords.words('english')) ## define stopwords

    tokenized_sentence_cleaned = [ ## remove stopwords
        w for w in tokenized_sentence if not w in stop_words
    ]

    lemmatized = [
        WordNetLemmatizer().lemmatize(word, pos = "v")
        for word in tokenized_sentence_cleaned
    ]

    cleaned_sentence = ' '.join(word for word in lemmatized)

    return cleaned_sentence
