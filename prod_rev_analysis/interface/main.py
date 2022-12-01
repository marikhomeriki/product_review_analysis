# package imports here
import numpy as np
import pandas as pd

from colorama import Fore, Style



# from taxifare.ml_logic.data import clean_data, get_chunk, save_chunk
# from taxifare.ml_logic.model import initialize_model, compile_model, train_model, evaluate_model
# from taxifare.ml_logic.params import CHUNK_SIZE, DATASET_SIZE, VALIDATION_DATASET_SIZE
# from taxifare.ml_logic.preprocessor import preprocess_features
# from taxifare.ml_logic.registry import load_model, save_model


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
