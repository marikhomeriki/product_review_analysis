from fastapi import FastAPI
import pandas as pd
import nltk
from prod_rev_analysis.ml_logic.absa import get_sent_asps
from prod_rev_analysis.interface.main import pred
from prod_rev_analysis.ml_logic.data import load_data_wordcloud, load_data
from prod_rev_analysis.ml_logic.model_w2v import neg_word2v, pos_word2v
from prod_rev_analysis.ml_logic.data import load_data_w2v
from prod_rev_analysis.data_sources.data_scarping import get_data_yelp, get_data_trustpilot

app = FastAPI()

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('corpus')
nltk.download('omw-1.4')

mock_data = {
    "cnn_model": {
        "Negative": 1218,
        "Positive": 307
    },
    'review_count': 5,
    'average_score': 3.4,
    "words": "A A A B B B C C C C C C C D D D D D",
    "words2v_neg": {
        "Scores": {
            "breakfast": 0.5056196295113908,
            "great food": 0.49979621245343886,
            "staff": 0.45015233280411826,
            "come back": 0.42710695466251225,
            "interior": 0.42311736617035406,
            "impressive": 0.42311736617035406,
            "place ok": 0.42066779513371866,
            "alright": 0.4139349890688776,
            "basic": 0.39377559042335186,
            "queue": 0.38419371103771877,
            "rude": 0.3623346150316884,
            "food alright": 0.3623346150316884,
            "alright wait": 0.3623346150316884,
            "wait staff": 0.3623346150316884,
            "staff rude": 0.3623346150316884,
            "rude better": 0.3623346150316884,
            "paneer tikka": 0.34797853734279205,
            "wish": 0.3468762521257027,
            "quality": 0.3314536309043429,
            "mediocre special": 0.3268726082918062
        }
    },
    "words2v_pos": {
        "Scores": {
            "life": 4.653466813615953,
            "great food": 4.5440070210520025,
            "amaze food": 4.476792128706007,
            "wow": 4.124781162635328,
            "roll": 4.109637340699904,
            "lovely": 4.07617377167323,
            "lamb chop": 4.010762882543427,
            "ambience": 3.984401679860918,
            "food ive": 3.778831739595504,
            "star": 3.674250585028675,
            "extremely": 3.6701131582352446,
            "fish": 3.59898167385988,
            "india": 3.494927079289294,
            "definitely recommend": 3.4923332269544596,
            "authentic": 3.4710140838269954,
            "decor": 3.414609984072969,
            "huge": 3.3393646713399945,
            "yelp": 3.3207868934628295,
            "accommodate": 3.2995818623668094,
            "top": 3.274168566918065
        }
    },

    "absa": {
        "Positive": {
            "service": 6,
            "food": 6,
            "meal": 2,
            "mash": 2,
            "chocolate": 2
        },
        "Negative": {
            "service": 1,
            "food": 0,
            "meal": 0,
            "mash": 0,
            "chocolate": 0
        },
        "Neutral": {
            "service": 0,
            "food": 0,
            "meal": 0,
            "mash": 0,
            "chocolate": 0
        }
    }
}


@app.get("/analyze")
async def analyze(source: str = '', url: str = '', pages: int = 1):
    if source == 'Yelp':
        df_reviews, review_count, average_score = get_data_yelp(url, pages)
    else:
        df_reviews, review_count, average_score = get_data_trustpilot(url, pages)

    cnn_data = load_data(df_reviews)

    cnn_model = pred(cnn_data)
    words = " ".join(df_reviews['text'].to_list())
    words2v_neg = neg_word2v(df_reviews).to_dict()
    words2v_pos = pos_word2v(df_reviews).to_dict()
    absa = get_sent_asps(pd.DataFrame(df_reviews['text'])).to_dict()

    return {
        'cnn_model': cnn_model,
        'words': words,
        'words2v_neg': words2v_neg,
        'words2v_pos': words2v_pos,
        'absa': absa,
        'review_count': review_count,
        'average_score': average_score

    }


@app.get("/mock-analyze")
async def mock_analyze(source: str = '', url: str = '', pages: int = 1):
    return mock_data
