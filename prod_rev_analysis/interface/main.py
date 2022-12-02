# package imports here
import numpy as np
import pandas as pd

from colorama import Fore, Style
<<<<<<< HEAD
<<<<<<< HEAD
from prod_rev_analysis.ml_logic.registry import load_model

from prod_rev_analysis.ml_logic.data import load_data, clean_data
=======
>>>>>>> master
=======
>>>>>>> master



# from taxifare.ml_logic.data import clean_data, get_chunk, save_chunk
# from taxifare.ml_logic.model import initialize_model, compile_model, train_model, evaluate_model
# from taxifare.ml_logic.params import CHUNK_SIZE, DATASET_SIZE, VALIDATION_DATASET_SIZE
# from taxifare.ml_logic.preprocessor import preprocess_features
# from taxifare.ml_logic.registry import load_model, save_model
<<<<<<< HEAD
<<<<<<< HEAD
from collections import Counter


def pred():
    """
    Make a prediction using the latest trained model
    """
    data = load_data()
    data_cleaned = clean_data(data)
    model = load_model()
    y_pred =  model.predict(data_cleaned)
    y_pred = [0 if pred <0.5 else 1 for pred in y_pred]
    y_pred = ['Negative' if sent == 0 else 'Positive' for sent in y_pred]

    return Counter(y_pred)


if __name__ == '__main__':

    result = pred()
    print(result)
=======
=======
>>>>>>> master


def preprocess(source_type = 'train'):
    """
    Preprocess the dataset by chunks fitting in memory.
    parameters:
    - source_type: 'train' or 'val'
    """

    print("\n⭐️ Use case: preprocess")
    # CODE here


def train():
    """
    Train a new model on the full (already preprocessed) dataset ITERATIVELY, by loading it
    chunk-by-chunk, and updating the weight of the model after each chunks.
    Save final model once it has seen all data, and compute validation metrics on a holdout validation set
    common to all chunks.
    """
    print("\n⭐️ Use case: train")
     # CODE here


def evaluate():
    """
    Evaluate the performance of the latest production model on new data
    """
    print("\n⭐️ Use case: evaluate")
     # CODE here


def pred(X_pred: pd.DataFrame = None) ->np.ndarray:
    """
    Make a prediction using the latest trained model
    """

    print("\n⭐️ Use case: predict")
     # CODE here






if __name__ == '__main__':
    # preprocess()
    # preprocess(source_type='val')
    # train()
    # pred()
    # evaluate()
    pass
<<<<<<< HEAD
>>>>>>> master
=======
>>>>>>> master
