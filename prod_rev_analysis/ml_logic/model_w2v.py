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
from prod_rev_analysis.ml_logic.data import load_data_w2v, cleaning_w2v



# def initialize_model(vocab_size) -> Model:
#     model = Sequential()
#     model.add(layers.Embedding(input_dim=vocab_size + 1, output_dim=20, mask_zero=True, input_length=50))
#     model.add(layers.Conv1D(32, 3))
#     model.add(layers.Flatten())
#     model.add(layers.Dense(50, activation="relu"))
#     model.add(layers.Dense(1, activation='sigmoid'))

#     return model



# def compile_model(model: Model) -> Model:
#     model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
#     return model

# def train_model(model: Model,
#                 X: np.ndarray,
#                 y: np.ndarray,
#                 batch_size=64,
#                 patience=2,
#                 validation_split=0.3,
#                 validation_data=None) -> Tuple[Model, dict]:

#     y_adj = y -1
#     es = EarlyStopping(patience=5, restore_best_weights=True)

#     histoty = model.fit(X, y_adj,
#                         epochs=20,
#                         batch_size=32,
#                         validation_split=0.3,
#                         callbacks=[es]
#                         )
#     return model, histoty

# def evaluate_model(model: Model,
#                    X: np.ndarray,
#                    y: np.ndarray,
#                    batch_size=64) -> Tuple[Model, dict]:


#     if model is None:
#         print(f"\n❌ no model to evaluate")
#         return None

#     metrics = model.evaluate(X, y)


#     loss = metrics["loss"]
#     mae = metrics["mae"]

#     print(f"\n✅ model evaluated: loss {round(loss, 2)} mae {round(mae, 2)}")

#     return metrics


def neg_word2v(df):
    df_negative = df[df.score < 4]
    neg_reviews = df_negative.text
    neg_reviews = pd.DataFrame(neg_reviews)
    neg_reviews_cleaned = neg_reviews["text"].apply(cleaning_w2v)
    print("This is it", neg_reviews_cleaned)
    neg_reviews_cleaned = pd.DataFrame(neg_reviews_cleaned)

    vectorizer_neg = TfidfVectorizer(ngram_range = (1,2),
                             min_df=0.01,
                             max_df = 0.5).fit(neg_reviews_cleaned.text).fit(neg_reviews_cleaned.text)
    vectors_neg = pd.DataFrame(vectorizer_neg.transform(neg_reviews_cleaned.text).toarray(),
                       columns = vectorizer_neg.get_feature_names_out())
    sum_tfidf_neg = vectors_neg.sum(axis = 0)
    tfidf_list_neg = [(word, sum_tfidf_neg[word])
              for word, idx in vectorizer_neg.vocabulary_.items()
              if word in vectorizer_neg.vocabulary_.keys()]
    sorted_tfidf_list_neg =sorted(tfidf_list_neg, key = lambda x: x[1], reverse=True)
    sorted_tfidf_list_neg = sorted_tfidf_list_neg[:20]

    words = [tup[0] for tup in sorted_tfidf_list_neg]
    scores = [tup[1] for tup in sorted_tfidf_list_neg]

    df_neg =  {'Words':words,'Scores':scores}
    df_neg = pd.DataFrame(df_neg).set_index('Words')

    return df_neg



def pos_word2v(df):
    df_positive = df[df.score > 4]
    pos_reviews = df_positive.text
    pos_reviews = pd.DataFrame(pos_reviews)
    pos_reviews_cleaned = pos_reviews["text"].apply(cleaning_w2v)
    pos_reviews_cleaned = pd.DataFrame(pos_reviews_cleaned)

    vectorizer_pos = TfidfVectorizer(ngram_range = (1,2),
                             min_df=0.001,
                             max_df = 0.5).fit(pos_reviews_cleaned.text).fit(pos_reviews_cleaned.text)
    vectors_pos = pd.DataFrame(vectorizer_pos.transform(pos_reviews_cleaned.text).toarray(),
                       columns = vectorizer_pos.get_feature_names_out())
    sum_tfidf_pos = vectors_pos.sum(axis = 0)
    tfidf_list_pos = [(word, sum_tfidf_pos[word])
              for word, idx in vectorizer_pos.vocabulary_.items()
              if word in vectorizer_pos.vocabulary_.keys()]
    sorted_tfidf_list_pos =sorted(tfidf_list_pos, key = lambda x: x[1], reverse=True)
    sorted_tfidf_list_pos = sorted_tfidf_list_pos[:20]

    words = [tup[0] for tup in sorted_tfidf_list_pos]
    scores = [tup[1] for tup in sorted_tfidf_list_pos]

    df_pos =  {'Words':words,'Scores':scores}
    df_pos = pd.DataFrame(df_pos).set_index('Words')

    return df_pos
