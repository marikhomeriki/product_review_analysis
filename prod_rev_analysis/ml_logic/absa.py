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
from prod_rev_analysis.ml_logic.data import load_data_absa
from pyabsa import ATEPCCheckpointManager



import pandas as pd
import os
import numpy as np
from wordcloud import WordCloud
from nltk.corpus import stopwords
import matplotlib.pyplot as plt


df = load_data_absa()

aspect_extractor = ATEPCCheckpointManager.get_aspect_extractor(checkpoint='multilingual-256-2')


def perform_inference(text):
    result = aspect_extractor.extract_aspect(inference_source=[text],
                                             pred_sentiment=True)

    result = pd.DataFrame({
        'aspect': result[0]['aspect'],
        'sentiment': result[0]['sentiment'],
        # 'probability': result[0]['probs'],
        'confidence': [round(x, 4) for x in result[0]['confidence']],
        'position': result[0]['position']
    })
    return result, '{}'.format(text)


def get_aspect_dfs(data):
    dfs = []
    for row in data.iterrows():
        text = row[1][0]
        df = perform_inference(text)
        dfs.append(df)
    return dfs


def get_aspect_distribution(dataframes):
    aspects = {}
    sents = []
    for df in dataframes:
        for a, s in df[0].iterrows():
            word_all = s[0].split()
            word = word_all[0].lower()
            if aspects.get(word) is None:
                sents = []
                sents.append(s[1])
                aspects[word] = sents
            else:
                sents = aspects.get(word)
                sents.append(s[1])
                aspects[word] = sents
    return aspects



def get_dfs():

    dfs = get_aspect_dfs(df)
    aspects = get_aspect_distribution(dfs)
    lss = list(aspects.keys())
    frequent_aspects = sorted(lss, key = lambda x: -len(aspects[x]))[:5]
    return frequent_aspects



def get_sent_asps():
    sent_asps = {}
    sent_counts = []
    dfs = get_aspect_dfs(df)
    aspects = get_aspect_distribution(dfs)
    frequent_aspects = get_dfs()
    for aspect in frequent_aspects:
        sent_counts.append(aspects[aspect].count('Positive'))
        sent_counts.append(aspects[aspect].count('Negative'))
        sent_counts.append(aspects[aspect].count('Neutral'))
        sent_asps[aspect] = sent_counts
        sent_counts = []
    sent_asps = pd.DataFrame(sent_asps)
    sent_asps_tr = sent_asps.T
    sent_asps_tr.rename({0: 'Positive', 1: 'Negative', 2: 'Neutral'}, axis=1, inplace = True)
    return sent_asps_tr
