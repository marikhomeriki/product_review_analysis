from tensorflow.keras import Model, Sequential, layers, regularizers, optimizers
from tensorflow.keras.callbacks import EarlyStopping
import pandas as pd
import os
import numpy as np
from prod_rev_analysis.ml_logic.data import load_data_w2v, cleaning_w2v



def initialize_model(vocab_size) -> Model:
    model = Sequential()
    model.add(layers.Embedding(input_dim=vocab_size + 1, output_dim=20, mask_zero=True, input_length=50))
    model.add(layers.Conv1D(32, 3))
    model.add(layers.Flatten())
    model.add(layers.Dense(50, activation="relu"))
    model.add(layers.Dense(1, activation='sigmoid'))

    return model



def compile_model(model: Model) -> Model:
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

def train_model(model: Model,
                X: np.ndarray,
                y: np.ndarray,
                batch_size=64,
                patience=2,
                validation_split=0.3,
                validation_data=None) -> Tuple[Model, dict]:

    y_adj = y -1
    es = EarlyStopping(patience=5, restore_best_weights=True)

    histoty = model.fit(X, y_adj,
                        epochs=20,
                        batch_size=32,
                        validation_split=0.3,
                        callbacks=[es]
                        )
    return model, histoty

def evaluate_model(model: Model,
                   X: np.ndarray,
                   y: np.ndarray,
                   batch_size=64) -> Tuple[Model, dict]:


    if model is None:
        print(f"\n❌ no model to evaluate")
        return None

    metrics = model.evaluate(X, y)


    loss = metrics["loss"]
    mae = metrics["mae"]

    print(f"\n✅ model evaluated: loss {round(loss, 2)} mae {round(mae, 2)}")

    return metrics



def neg_word2v(df):
    df_negative = df[df.score < 4]
    neg_reviews = df_negative.text
    neg_reviews = pd.DataFrame(neg_reviews)
    neg_reviews_cleaned = neg_reviews["text"].apply(cleaning_w2v)
    neg_reviews_cleaned = pd.DataFrame(neg_reviews_cleaned)
