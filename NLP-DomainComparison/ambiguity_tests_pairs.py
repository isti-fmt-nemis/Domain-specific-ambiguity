from __future__ import division

from os.path import os
from pprint import pprint

import domain_analysis.ambiguity as ambiguity
from gensim.models.word2vec import Word2Vec

MODEL_PATH = "./MODELS"

models = dict()

models['cs'] = Word2Vec.load(os.path.join(MODEL_PATH, "Computer_Science_D_2.bin"))
models['med'] = Word2Vec.load(os.path.join(MODEL_PATH, "Medicine_D_2.bin"))
models['sport'] = Word2Vec.load(os.path.join(MODEL_PATH, "Sports_D_2.bin"))
models['ele'] = Word2Vec.load(os.path.join(MODEL_PATH, "Electronic_Engineering_D_2.bin"))
models['mec'] = Word2Vec.load(os.path.join(MODEL_PATH, "Mechanical_Engineering_D_2.bin"))
models['lit'] = Word2Vec.load(os.path.join(MODEL_PATH, "Literature_D_2.bin"))

shared_word_count = 100
top_words_to_show = 20

domains = sorted(list(models.keys()))

for domain_a in domains:
    for domain_b in domains:
        if domain_a < domain_b:
            pprint([domain_a, domain_b, shared_word_count])
            ambiguous = ambiguity.ambiguity_mse_rank([models[domain_a], models[domain_b]], shared_word_count)
            pprint(ambiguous[:top_words_to_show])
            pprint(ambiguous[-top_words_to_show:])
