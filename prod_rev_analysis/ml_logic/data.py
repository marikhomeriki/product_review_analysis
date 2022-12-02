<<<<<<< HEAD
<<<<<<< HEAD
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
    # df = pd.read_csv('/Users/marikhomeriki/code/marikhomeriki/raw_data/data_dishoom.csv', header=None)
    df = pd.read_csv('../review.csv', header=None)
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
=======
=======
>>>>>>> master
from taxifare.ml_logic.params import (COLUMN_NAMES_RAW,
                                            DTYPES_RAW_OPTIMIZED,
                                            DTYPES_RAW_OPTIMIZED_HEADLESS,
                                            DTYPES_PROCESSED_OPTIMIZED
                                            )

from taxifare.data_sources.local_disk import (get_pandas_chunk, save_local_chunk)

from taxifare.data_sources.big_query import (get_bq_chunk, save_bq_chunk)

import os
import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    clean raw data by removing buggy or irrelevant transactions
    or columns for the training set
    """

    # remove useless/redundant columns
    df = df.drop(columns=['key'])

    # remove buggy transactions
    df = df.drop_duplicates()  # TODO: handle in the data source if the data is consumed by chunks
    df = df.dropna(how='any', axis=0)
    df = df[(df.dropoff_latitude != 0) | (df.dropoff_longitude != 0) |
            (df.pickup_latitude != 0) | (df.pickup_longitude != 0)]
    df = df[df.passenger_count > 0]
    df = df[df.fare_amount > 0]

    # remove irrelevant/non-representative transactions (rows) for a training set
    df = df[df.fare_amount < 400]
    df = df[df.passenger_count < 8]
    df = df[df["pickup_latitude"].between(left=40.5, right=40.9)]
    df = df[df["dropoff_latitude"].between(left=40.5, right=40.9)]
    df = df[df["pickup_longitude"].between(left=-74.3, right=-73.7)]
    df = df[df["dropoff_longitude"].between(left=-74.3, right=-73.7)]

    print("\n✅ data cleaned")

    return df

<<<<<<< HEAD
>>>>>>> master
=======
>>>>>>> master
