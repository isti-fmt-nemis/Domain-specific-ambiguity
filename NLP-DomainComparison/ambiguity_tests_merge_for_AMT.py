'''
This module generates the lists of terms, ranked by their ambiguity score 
'''


from __future__ import division

from os.path import os
from pprint import pprint

from gensim.models.word2vec import Word2Vec

import domain_analysis.ambiguity as ambiguity



MODEL_PATH = "./MODELS"

models = dict()

models['cs'] = Word2Vec.load(os.path.join(MODEL_PATH, "Computer_Science_D_2.bin"))
models['med'] = Word2Vec.load(os.path.join(MODEL_PATH, "Medicine_D_2.bin"))
models['sport'] = Word2Vec.load(os.path.join(MODEL_PATH, "Sports_D_2.bin"))
models['ele'] = Word2Vec.load(os.path.join(MODEL_PATH, "Electronic_Engineering_D_2.bin"))
models['mec'] = Word2Vec.load(os.path.join(MODEL_PATH, "Mechanical_Engineering_D_2.bin"))

min_freq_ratios = [0.3]
w2v_topn_values = [100]
shared_word_counts = [200]

top_words_num = 10
sample_size = 10

scenarios = {'CS_EEN': [('cs', models['cs']), ('ele', models['ele'])],
             'CS_MEN': [('cs', models['cs']), ('mec', models['mec'])],
             'CS_MED': [('cs', models['cs']), ('med', models['med'])],
             'CS_SPO': [('cs', models['cs']), ('sport', models['sport'])],
             'medical_software': [('cs', models['cs']), ('med', models['med'])],
             'medical_device': [('cs', models['cs']), ('ele', models['ele']), ('med', models['med'])],
             'medical_robot': [('cs', models['cs']), ('ele', models['ele']), ('mec', models['mec']),
                               ('med', models['med'])],
             'sport_rehab_machine': [('cs', models['cs']), ('ele', models['ele']), ('mec', models['mec']),
                                     ('med', models['med']), ('sport', models['sport'])], }

for scenario_name in scenarios:
    for min_freq_ratio in min_freq_ratios:
        for w2v_topn_value in w2v_topn_values:
            for shared_word_count in shared_word_counts:
    
                ambiguous = ambiguity.ambiguity_mse_rank_merge(scenarios[scenario_name], min_freq_ratio, shared_word_count, w2v_topn_value)
                print(scenario_name + '\n')
                pprint([(term, mse, count) for (_, term, _, mse, count) in ambiguous], width=200)
    

