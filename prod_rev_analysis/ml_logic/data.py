from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing.text import text_to_word_sequence
import pickle
import os

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

def clean_data(list) -> np.ndarray:
    """
    clean raw data by tokenizing and padding the reviews
    """
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    df_token = tokenizer.texts_to_sequences(list)

    df_token_pad = pad_sequences(df_token, maxlen=50, dtype='float32', padding="post")

    return df_token_pad
