"""
Developed by Aindriya Barua in November, 2021
"""

import os
import json
import numpy as np
import fasttext as ft

import sentence_normalizer


def parse_data(ft_model):
    with open("dataset.json") as file:
        data = json.load(file)

    for intent in data['intents']:
        embedded_patterns = []
        for pattern in intent['patterns']:
            pattern = sentence_normalizer.preprocess_main(pattern)
            embedded_sentence = embed_sentence(pattern, ft_model)

            embedded_patterns.append(embedded_sentence)
        intent['patterns'] = np.array(embedded_patterns).tolist()

    return data


def embed_sentence(sentence, ft_model):
    sentence_vec = ft_model.get_sentence_vector(sentence)
    return sentence_vec


def write_embedded_data(data):
    json_object = json.dumps(data, indent=4)

    with open("embedded_data.json", "w") as outfile:
        outfile.write(json_object)


def load_embedding_model(model_path='cc.en.300.bin'):
    if not os.path.exists(model_path):
        raise FileNotFoundError(
            f"FastText model '{model_path}' not found. "
            "Please download 'cc.en.300.bin.gz' from https://fasttext.cc/docs/en/crawl-vectors.html "
            "and extract it to the project root directory."
        )
    ft_model = ft.load_model(model_path)
    return ft_model


if __name__ == '__main__':
    ft_model = load_embedding_model()
    embedded_data = parse_data(ft_model)
    write_embedded_data(embedded_data)

