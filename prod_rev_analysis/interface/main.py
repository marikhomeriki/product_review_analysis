from colorama import Fore, Style
from prod_rev_analysis.ml_logic.registry import load_model
from prod_rev_analysis.ml_logic.data import load_data, clean_data
from collections import Counter


def pred(data):
    """
    Make a prediction using the latest trained model
    """

    data_cleaned = clean_data(data)
    model = load_model()
    y_pred =  model.predict(data_cleaned)
    y_pred = [0 if pred <0.5 else 1 for pred in y_pred]
    y_pred = ['Negative' if sent == 0 else 'Positive' for sent in y_pred]

    return Counter(y_pred)


if __name__ == '__main__':

    result = pred()
    print(result)
