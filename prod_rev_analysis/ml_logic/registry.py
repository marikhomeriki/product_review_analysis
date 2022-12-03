
import glob
import os
import time
import pickle
import mlflow


from colorama import Fore, Style

from tensorflow.keras import Model, models


def load_model() -> Model:
    """
    load the latest saved model, return None if no model found
    """
    model = models.load_model(os.path.join(os.getcwd(), "CNN_model"))
    print(Fore.BLUE + "\nLoad model from local disk..." + Style.RESET_ALL)

    return model

if __name__ == "__main__":
    load_model()
