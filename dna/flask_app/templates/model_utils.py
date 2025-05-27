import torch
import torch.nn as nn
import pickle
import numpy as np


# DNA base encoding
DNA_DICT = {'A': 3, 'C': 4, 'G': 5, 'T': 0, 'N': 1}

def encode_sequence(seq):
    return [DNA_DICT.get(base.upper(), 4) for base in seq]

def pad_sequence(seq, max_len):
    return seq + [4] * (max_len - len(seq))


def load_model(model_path):
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    model.eval()
    return model

def predict(model, sequence, pad=False, max_len=20):
    classes= np.arange(12)
    input_encoded = encode_sequence(sequence)
    prediction_logic = model(torch.Tensor(input_encoded).unsqueeze(0))
    model(torch.Tensor(input_encoded = encode_sequence(sequence)).unsqueeze(0))
    prediction = torch.argmax(prediction_logic)
    if pad:
        input_encoded = pad_sequence(input_encoded, max_len)
    input_tensor = torch.tensor([input_encoded], dtype=torch.long)
    with torch.no_grad():
        prediction = model(input_tensor)
    return prediction 
