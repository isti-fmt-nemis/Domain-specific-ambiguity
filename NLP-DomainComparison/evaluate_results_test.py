'''
Created on Oct 3, 2018

@author: alessioferrari
'''
from random import shuffle

from sklearn.metrics.classification import cohen_kappa_score

import numpy as np
from validation.evaluate_results import build_automated_sets, \
    get_term_value_dictionary, evaluate_results_top_bottom_rank, \
    get_term_value_list


def compute_results(auto_list, set_separator_index, file_annotation_a, file_annotation_b, in_score_column_idx, in_term_column_idx):
    auto_s = build_automated_sets(auto_list, set_separator_index)
    dictionary_a = get_term_value_dictionary(file_annotation_a, in_score_column_idx, in_term_column_idx)
    dictionary_b = get_term_value_dictionary(file_annotation_b, in_score_column_idx, in_term_column_idx)
      
    dictionary_merge = {}
    for k in dictionary_a.keys():
        dictionary_merge[k] = np.mean([dictionary_a[k],dictionary_b[k]]) 
    ground_truth_rank = sorted(dictionary_merge, key=dictionary_merge.get, reverse=True)
    tau_result = evaluate_results_top_bottom_rank(ground_truth_ranked_list=ground_truth_rank, auto_sets=auto_s)
    
    scores_a = get_term_value_list(file_annotation_a, score_column_idx = in_score_column_idx)
    scores_b = get_term_value_list(file_annotation_b, score_column_idx = in_score_column_idx)
    k_result = (cohen_kappa_score(scores_a, scores_b))

    return [k_result, tau_result] 



auto_list_1 = ['institute', 'theory', 'environment', 'distance', 'matrix', 'length', 'release', 'tool', 'law', 'frequency', 'business', 'distribution', 'output', 'issue', 'component', 'team', 'machine', 'concept', 'performance', 'approach']
print(compute_results(auto_list=auto_list_1, set_separator_index=10, file_annotation_a='./validation/1_a.csv', file_annotation_b='./validation/1_b.csv', in_score_column_idx=3, in_term_column_idx=0))
auto_list_7 = ['environment', 'board', 'table', 'law', 'institute', 'value', 'pattern', 'surface', 'tool', 'chemical', 'area', 'server', 'heat', 'rule', 'solution', 'range', 'condition', 'issue', 'user', 'report']
print(compute_results(auto_list=auto_list_7, set_separator_index=10, file_annotation_a='./validation/7_a.csv', file_annotation_b='./validation/7_b.csv', in_score_column_idx=5, in_term_column_idx=0))

