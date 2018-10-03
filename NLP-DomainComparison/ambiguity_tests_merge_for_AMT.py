from __future__ import division

from os.path import os
from pprint import pprint

from gensim.models.word2vec import Word2Vec

import domain_analysis.ambiguity as ambiguity

from validation import evaluate_results


MODEL_PATH = "./MODELS"

models = dict()

models['cs'] = Word2Vec.load(os.path.join(MODEL_PATH, "Computer_Science_D_2.bin"))
models['med'] = Word2Vec.load(os.path.join(MODEL_PATH, "Medicine_D_2.bin"))
models['sport'] = Word2Vec.load(os.path.join(MODEL_PATH, "Sports_D_2.bin"))
models['ele'] = Word2Vec.load(os.path.join(MODEL_PATH, "Electronic_Engineering_D_2.bin"))
models['mec'] = Word2Vec.load(os.path.join(MODEL_PATH, "Mechanical_Engineering_D_2.bin"))
models['lit'] = Word2Vec.load(os.path.join(MODEL_PATH, "Literature_D_2.bin"))

min_freq_ratios = [0.3]#[0.1, 0.3, 0.5]
w2v_topn_values = [100]#[50, 100, 300, 500]
shared_word_counts = [200]#[100, 200, 500]

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
        
                ranked_sample_top = evaluate_results.generate_ranked_sample_top(top_words_num, sample_size, ambiguous)
#                ranked_sample_step = evaluate_results.generate_ranked_sample_step(sample_size*2, ambiguous)
            
                terms_sample_top = [term for (_, term, _, _, _) in ranked_sample_top]
#                terms_sample_step = [term for (_, term, _, _, _) in ranked_sample_step]
            
                print(scenario_name + '_f0' + str(min_freq_ratio).split('.')[-1] + '_w2vlen_' + str(w2v_topn_value) + '_dlen_' + str(shared_word_count) + '_top = ' + str(terms_sample_top))
#                print(scenario_name + '_f0' + str(min_freq_ratio).split('.')[-1] + '_w2vlen_' + str(w2v_topn_value) + '_dlen_'+ str(shared_word_count) + '_step = ' + str(terms_sample_step))
    

