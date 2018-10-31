'''
Created on Oct 3, 2018

@author: alessioferrari
'''

import csv

from numpy import random
from numpy.ma.core import fabs
from sklearn.metrics.classification import cohen_kappa_score

import numpy as np
from validation.evaluate_results import build_automated_sets, \
    get_term_value_dictionary, evaluate_results_top_bottom_rank, \
    get_term_value_list, get_term_value_dictionary_AMT, convert_score, \
    get_term_value_list_AMT, compute_score_overlap, reduce_score, \
    evaluate_results_top_bottom_optimistic, \
    evaluate_results_top_bottom_skip_ties, build_ground_truth_sets, \
    evaluate_results_top_bottom_classification


def compute_results(auto_list, set_separator_index, file_annotation_a, file_annotation_b, in_score_column_idx, in_term_column_idx):
    auto_s = build_automated_sets(auto_list, set_separator_index)
    dictionary_a = get_term_value_dictionary(file_annotation_a, in_score_column_idx, in_term_column_idx)
    dictionary_b = get_term_value_dictionary(file_annotation_b, in_score_column_idx, in_term_column_idx)
      
    dictionary_merge = {}
    for k in dictionary_a.keys():
        dictionary_merge[k] = np.mean([dictionary_a[k],dictionary_b[k]]) 
    ground_truth_rank = sorted(dictionary_merge, key=dictionary_merge.get, reverse=True)
    
    tau_result = evaluate_results_top_bottom_rank(ground_truth_ranked_list=ground_truth_rank, auto_sets=auto_s)
    tau_result_ties = evaluate_results_top_bottom_optimistic(dictionary_merge, auto_s)
    tau_result_skip_ties = evaluate_results_top_bottom_skip_ties(dictionary_merge, auto_s)
    
    scores_a = get_term_value_list(file_annotation_a, score_column_idx = in_score_column_idx)
    scores_b = get_term_value_list(file_annotation_b, score_column_idx = in_score_column_idx)

    k_result = (cohen_kappa_score(scores_a, scores_b))
    
    return [k_result, tau_result_ties, tau_result_skip_ties] 


'''
For each couple in the list if the elements of the couple differ by a value
that is <= unit, the elements are considered equal. 
'''
def rebase_scores(list_a, list_b, unit=1):
    out_list_a = [0] * len(list_a)
    out_list_b = [0] * len(list_b)
    
    len_agree = 0
    for i,s in enumerate(list_a):
        if fabs(s - list_b[i]) <= 1:
            out_list_a[i] = 'a'
            out_list_b[i] = 'a'
            len_agree += 1 
        else:
            out_list_a[i] = 'b'
            out_list_b[i] = 'c'
    
    
    out_list_final_a = []
    out_list_final_b = []
    
    half_agree_counter = 0         
    for a,b in zip(out_list_a, out_list_b):
        if a == 'a':
            if half_agree_counter < len_agree/2: 
                out_list_final_a.append('b')
                out_list_final_b.append('b')
            else:
                out_list_final_a.append('c')
                out_list_final_b.append('c')
            half_agree_counter +=1    
        else:
            out_list_final_a.append(a)
            out_list_final_b.append(b)
                    
            
    return out_list_final_a, out_list_final_b


def compute_agreement(file_annotation_a, file_annotation_b, in_score_column_idx):
    
    scores_a = get_term_value_list(file_annotation_a, score_column_idx = in_score_column_idx)
    scores_b = get_term_value_list(file_annotation_b, score_column_idx = in_score_column_idx)

    k_result = cohen_kappa_score(scores_a, scores_b)
    k_percent = len([(x,y) for x, y in zip(scores_a, scores_b) if x == y]) / len(scores_a)
    
    scores_a_rebased, scores_b_rebased = rebase_scores([int(a) for a in scores_a], [int(b) for b in scores_b])
    
    if scores_a_rebased != scores_b_rebased:
        k_permissive = cohen_kappa_score(scores_a_rebased, scores_b_rebased)
    else:
        k_permissive = 1.0
        
    k_permissive_percent = len([(x,y) for x, y in zip(scores_a_rebased, scores_b_rebased) if x == y]) / len(scores_a_rebased)    
    
    return k_result, k_percent, k_permissive, k_permissive_percent

'''
This function computes the agreement in various forms: it computes the classical cohen's kappa, 
considering each answer as different, and then computes the cohen's kappa considering as 
different solely those answers that differ by more than 1 unit. 
'''
def compute_agreement_AMT(file_annotations, in_score_a_column_idx=5, in_score_b_column_idx=7):
    scores_literal_a = get_term_value_list_AMT(file_annotations, score_column_idx = in_score_a_column_idx)
    scores_literal_b = get_term_value_list_AMT(file_annotations, score_column_idx = in_score_b_column_idx)
    
    scores_a = [convert_score(s) for s in scores_literal_a]
    scores_b = [convert_score(s) for s in scores_literal_b]
    
    
    k_result = cohen_kappa_score(scores_a, scores_b)
    k_percent = len([(x,y) for x, y in zip(scores_a, scores_b) if x == y]) / len(scores_a) 

    scores_a_rebased, scores_b_rebased = rebase_scores(scores_a, scores_b)
    
    k_permissive = cohen_kappa_score(scores_a_rebased, scores_b_rebased)
    k_permissive_percent = len([(x,y) for x, y in zip(scores_a_rebased, scores_b_rebased) if x == y]) / len(scores_a_rebased)
    
    return k_result, k_percent, k_permissive, k_permissive_percent


print('\nAndrea\'s \& Alessio\'s Evaluation\n')
   
print('Embedded Light Controller ' + str(compute_agreement(file_annotation_a='./Results-Andrea-10.10.18/10a.csv', file_annotation_b='./Results-Alessio-10.10.18/10.csv',in_score_column_idx=3)))
print('CAD for Mechanical Components ' + str(compute_agreement(file_annotation_a='./Results-Andrea-10.10.18/9a.csv', file_annotation_b='./Results-Alessio-10.10.18/9.csv',in_score_column_idx=3)))
print('Medical Software ' + str(compute_agreement(file_annotation_a='./Results-Andrea-10.10.18/11a.csv', file_annotation_b='./Results-Alessio-10.10.18/11.csv',in_score_column_idx=3)))
print('Athletes Network ' + str(compute_agreement(file_annotation_a='./Results-Andrea-10.10.18/8a.csv', file_annotation_b='./Results-Alessio-10.10.18/8.csv',in_score_column_idx=3)))
 
print('Medical device ' + str(compute_agreement(file_annotation_a='./Results-Andrea-10.10.18/12a.csv', file_annotation_b='./Results-Alessio-10.10.18/12.csv',in_score_column_idx=4)))
print('Medical robot ' + str(compute_agreement(file_annotation_a='./Results-Andrea-10.10.18/14a.csv', file_annotation_b='./Results-Alessio-10.10.18/14.csv',in_score_column_idx=5)))
print('Sport rehab machine ' + str(compute_agreement(file_annotation_a='./Results-Andrea-10.10.18/13a.csv', file_annotation_b='./Results-Alessio-10.10.18/13.csv',in_score_column_idx=6)))

print('\nMechanical Turks\' Evaluation\n')

print('Embedded Light Controller ' + str(compute_agreement_AMT(file_annotations='./Results-AMT-9.10.18/res-10.csv')))
print('CAD for Mechanical Components ' + str(compute_agreement_AMT(file_annotations='./Results-AMT-11.10.18/res-9.csv')))
print('Medical Software ' + str(compute_agreement_AMT(file_annotations='./Results-AMT-9.10.18/res-11.csv')))
print('Athletes Network ' + str(compute_agreement_AMT(file_annotations='./Results-AMT-9.10.18/res-8.csv')))
 
print('Medical device ' + str(compute_agreement_AMT(file_annotations='./Results-AMT-11.10.18/res-12.csv', in_score_a_column_idx=6, in_score_b_column_idx=8)))
print('Medical robot ' + str(compute_agreement_AMT(file_annotations='./Results-AMT-11.10.18/res-14.csv', in_score_a_column_idx=7, in_score_b_column_idx=9)))
print('Sport rehab machine ' + str(compute_agreement_AMT(file_annotations='./Results-AMT-11.10.18/res-13.csv', in_score_a_column_idx=8, in_score_b_column_idx=10)))
   


