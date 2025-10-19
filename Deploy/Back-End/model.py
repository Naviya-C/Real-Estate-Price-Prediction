import pickle
import numpy as np

def load_model():
    with open("../Model/model.pickle", "rb") as f:
        model = pickle.load(f)
    return model

def predict(model, data):
    data_array = np.array(data)
    return model.predict(data_array).tolist()



