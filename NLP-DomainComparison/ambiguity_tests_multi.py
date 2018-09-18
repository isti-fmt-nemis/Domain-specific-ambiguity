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

scenarios = {'med_device': [models['cs'], models['ele'], models['med']],
             'engineering': [models['cs'], models['ele'], models['mec']],
             'high_tech_sport_device': [models['cs'], models['ele'], models['sport']],
             'low_tech_sport_device': [models['mec'], models['ele'], models['sport']],
             'all': list(models.values())}

scenarios = {'medical_software': [models['cs'], models['med']],
             'medical_device': [models['cs'], models['ele'], models['med']],
             'medical_robot': [models['cs'], models['ele'], models['mec'], models['med']],
             'sport_rehab_machine': [models['cs'], models['ele'], models['mec'], models['med'], models['sport']],}

for scenario_name in scenarios:
    pprint([scenario_name, shared_word_count])
    ambiguous = ambiguity.ambiguity_mse_rank(scenarios[scenario_name], shared_word_count)
    pprint(ambiguous[:top_words_to_show])
    pprint(ambiguous[-top_words_to_show:])
