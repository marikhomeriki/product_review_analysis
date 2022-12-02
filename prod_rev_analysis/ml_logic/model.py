from tensorflow.keras import Model, Sequential, layers, regularizers, optimizers
from tensorflow.keras.callbacks import EarlyStopping
<<<<<<< HEAD
<<<<<<< HEAD
import pandas as pd
import os
import numpy as np



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
=======
=======
>>>>>>> master



def initialize_model(X: np.ndarray) -> Model:
    pass


def compile_model(model: Model, learning_rate: float) -> Model:
    pass
<<<<<<< HEAD
>>>>>>> master
=======
>>>>>>> master

def train_model(model: Model,
                X: np.ndarray,
                y: np.ndarray,
                batch_size=64,
                patience=2,
                validation_split=0.3,
                validation_data=None) -> Tuple[Model, dict]:
<<<<<<< HEAD
<<<<<<< HEAD


    y_adj = y -1
    es = EarlyStopping(patience=5, restore_best_weights=True)

    histoty = model.fit(X, y_adj,
                        epochs=20,
                        batch_size=32,
                        validation_split=0.3,
                        callbacks=[es]
                        )
    return model, histoty
=======
    pass
>>>>>>> master
=======
    pass
>>>>>>> master

def evaluate_model(model: Model,
                   X: np.ndarray,
                   y: np.ndarray,
                   batch_size=64) -> Tuple[Model, dict]:
<<<<<<< HEAD
<<<<<<< HEAD


    if model is None:
        print(f"\n❌ no model to evaluate")
        return None

    metrics = model.evaluate(X, y)


    loss = metrics["loss"]
    mae = metrics["mae"]

    print(f"\n✅ model evaluated: loss {round(loss, 2)} mae {round(mae, 2)}")

    return metrics
=======
    pass
>>>>>>> master
=======
    pass
>>>>>>> master
