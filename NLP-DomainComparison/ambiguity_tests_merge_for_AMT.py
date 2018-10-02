from __future__ import division

from os.path import os
from pprint import pprint

import domain_analysis.ambiguity as ambiguity
from gensim.models.word2vec import Word2Vec
from validation import evaluate_results

MODEL_PATH = "./MODELS"

models = dict()

models['cs'] = Word2Vec.load(os.path.join(MODEL_PATH, "Computer_Science_D_2.bin"))
models['med'] = Word2Vec.load(os.path.join(MODEL_PATH, "Medicine_D_2.bin"))
models['sport'] = Word2Vec.load(os.path.join(MODEL_PATH, "Sports_D_2.bin"))
models['ele'] = Word2Vec.load(os.path.join(MODEL_PATH, "Electronic_Engineering_D_2.bin"))
models['mec'] = Word2Vec.load(os.path.join(MODEL_PATH, "Mechanical_Engineering_D_2.bin"))
models['lit'] = Word2Vec.load(os.path.join(MODEL_PATH, "Literature_D_2.bin"))

min_freq_ratio = 0.3
w2v_topn_value = 100
shared_word_count = 100

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
    
    #pprint([scenario_name, shared_word_count, w2v_topn_value],width=200)
    ambiguous = ambiguity.ambiguity_mse_rank_merge(scenarios[scenario_name], min_freq_ratio, shared_word_count, w2v_topn_value)
    
    ranked_sample_top = evaluate_results.generate_ranked_sample_top(top_words_num, sample_size, ambiguous)
    ranked_sample_step = evaluate_results.generate_ranked_sample_step(sample_size*2, ambiguous)
    
    terms_sample_top = [term for (_, term, _, _, _) in ranked_sample_top]
    terms_sample_step = [term for (_, term, _, _, _) in ranked_sample_step]
    
    #pprint(['TOP', top_words_num, sample_size], width=200)
    print(scenario_name + '_top_f0' + str(min_freq_ratio).split('.')[-1] + ' = ' + str(terms_sample_top))
    
    #pprint(['STEP', sample_size*2], width=200)
    print(scenario_name + '_step_f0' + str(min_freq_ratio).split('.')[-1] + ' = ' + str(terms_sample_step))
    

