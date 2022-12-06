from fastapi import FastAPI
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
from prod_rev_analysis.ml_logic.absa import get_sent_asps
from prod_rev_analysis.interface.main import pred
from prod_rev_analysis.ml_logic.data import load_data_wordcloud
from prod_rev_analysis.ml_logic.model_w2v import neg_word2v, pos_word2v
from prod_rev_analysis.ml_logic.data import load_data_w2v

app = FastAPI()

@app.get("/analyze")
async def root():
    data = load_data_wordcloud()
    data_w2v = load_data_w2v()

    cnn_model = dict(pred())
    # word_frequency = Counter(" ".join(data['text'].to_list()).split(' '))
    words2v_neg = neg_word2v(data_w2v).to_dict()
    words2v_pos = pos_word2v(data_w2v).to_dict()
    absa = get_sent_asps().to_dict()

    return {
        'cnn_model': cnn_model,
        # 'word_frequency': word_frequency,
        'words2v_neg': words2v_neg,
        'words2v_pos': words2v_pos,
        'absa': absa,
    }
