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

min_freq_ratio = 0.1
shared_word_count = 100
top_words_to_show = 20

scenarios = {'medical_software': [('cs', models['cs']), ('med', models['med'])],
             'medical_device': [('cs', models['cs']), ('ele', models['ele']), ('med', models['med'])],
             'medical_robot': [('cs', models['cs']), ('ele', models['ele']), ('mec', models['mec']),
                               ('med', models['med'])],
             'sport_rehab_machine': [('cs', models['cs']), ('ele', models['ele']), ('mec', models['mec']),
                                     ('med', models['med']), ('sport', models['sport'])], }

for scenario_name in scenarios:
    pprint([scenario_name, shared_word_count],width=200)
    ambiguous = ambiguity.ambiguity_mse_rank_merge(scenarios[scenario_name], min_freq_ratio, shared_word_count)
    pprint(ambiguous[:top_words_to_show],width=200)
    pprint(ambiguous[-top_words_to_show:],width=200)
