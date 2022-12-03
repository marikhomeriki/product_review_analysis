
# from taxifare.ml_logic.params import (COLUMN_NAMES_RAW,
#                                             DTYPES_RAW_OPTIMIZED,
#                                             DTYPES_RAW_OPTIMIZED_HEADLESS,
#                                             DTYPES_PROCESSED_OPTIMIZED
#                                             )

# from taxifare.data_sources.local_disk import (get_pandas_chunk, save_local_chunk)

# from taxifare.data_sources.big_query import (get_bq_chunk, save_bq_chunk)

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing.text import text_to_word_sequence
import pickle


import os


def load_data():
    df = pd.read_csv('/Users/marikhomeriki/code/marikhomeriki/raw_data/data_dishoom.csv', header=None)
    # df = pd.read_csv('../review.csv', header=None)
    df = df.rename({1: 'text'}, axis = 1)
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
