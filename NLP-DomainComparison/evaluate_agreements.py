'''
Created on Oct 3, 2018

@author: alessioferrari
'''

import csv

from numpy import random
from numpy.ma.core import fabs
from sklearn.metrics.classification import cohen_kappa_score

import numpy as np
from validation import evaluate_results


def compute_agreement(file_annotation_a, file_annotation_b, in_score_column_idx):
    
    scores_a = evaluate_results.get_term_value_list(file_annotation_a, score_column_idx = in_score_column_idx)
    scores_b = evaluate_results.get_term_value_list(file_annotation_b, score_column_idx = in_score_column_idx)

    k_result = cohen_kappa_score(scores_a, scores_b)
    k_percent = len([(x,y) for x, y in zip(scores_a, scores_b) if x == y]) / len(scores_a)
    
    scores_a_rebased, scores_b_rebased = evaluate_results.rebase_scores([int(a) for a in scores_a], [int(b) for b in scores_b])
    
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
    scores_literal_a = evaluate_results.get_term_value_list_AMT(file_annotations, score_column_idx = in_score_a_column_idx)
    scores_literal_b = evaluate_results.get_term_value_list_AMT(file_annotations, score_column_idx = in_score_b_column_idx)
    
    scores_a = [evaluate_results.convert_score(s) for s in scores_literal_a]
    scores_b = [evaluate_results.convert_score(s) for s in scores_literal_b]
    
    
    k_result = cohen_kappa_score(scores_a, scores_b)
    k_percent = len([(x,y) for x, y in zip(scores_a, scores_b) if x == y]) / len(scores_a) 

    scores_a_rebased, scores_b_rebased = evaluate_results.rebase_scores(scores_a, scores_b)
    
    k_permissive = cohen_kappa_score(scores_a_rebased, scores_b_rebased)
    k_permissive_percent = len([(x,y) for x, y in zip(scores_a_rebased, scores_b_rebased) if x == y]) / len(scores_a_rebased)
    
    return k_result, k_percent, k_permissive, k_permissive_percent


print('\nAndrea\'s \& Alessio\'s Evaluation\n')
   
print('Embedded Light Controller ' + str(compute_agreement(file_annotation_a='./GROUND-TRUTH/Results-Andrea/10.csv', file_annotation_b='./GROUND-TRUTH/Results-Alessio/10.csv',in_score_column_idx=3)))
print('CAD for Mechanical Components ' + str(compute_agreement(file_annotation_a='./GROUND-TRUTH/Results-Andrea/9.csv', file_annotation_b='./GROUND-TRUTH/Results-Alessio/9.csv',in_score_column_idx=3)))
print('Medical Software ' + str(compute_agreement(file_annotation_a='./GROUND-TRUTH/Results-Andrea/11.csv', file_annotation_b='./GROUND-TRUTH/Results-Alessio/11.csv',in_score_column_idx=3)))
print('Athletes Network ' + str(compute_agreement(file_annotation_a='./GROUND-TRUTH/Results-Andrea/8.csv', file_annotation_b='./GROUND-TRUTH/Results-Alessio/8.csv',in_score_column_idx=3)))
 
print('Medical device ' + str(compute_agreement(file_annotation_a='./GROUND-TRUTH/Results-Andrea/12.csv', file_annotation_b='./GROUND-TRUTH/Results-Alessio/12.csv',in_score_column_idx=4)))
print('Medical robot ' + str(compute_agreement(file_annotation_a='./GROUND-TRUTH/Results-Andrea/14.csv', file_annotation_b='./GROUND-TRUTH/Results-Alessio/14.csv',in_score_column_idx=5)))
print('Sport rehab machine ' + str(compute_agreement(file_annotation_a='./GROUND-TRUTH/Results-Andrea/13.csv', file_annotation_b='./GROUND-TRUTH/Results-Alessio/13.csv',in_score_column_idx=6)))

print('\nMechanical Turks\' Evaluation\n')

print('Embedded Light Controller ' + str(compute_agreement_AMT(file_annotations='./GROUND-TRUTH/Results-MTurks/10.csv')))
print('CAD for Mechanical Components ' + str(compute_agreement_AMT(file_annotations='./GROUND-TRUTH/Results-MTurks/9.csv')))
print('Medical Software ' + str(compute_agreement_AMT(file_annotations='./GROUND-TRUTH/Results-MTurks/11.csv')))
print('Athletes Network ' + str(compute_agreement_AMT(file_annotations='./GROUND-TRUTH/Results-MTurks/8.csv')))
 
print('Medical device ' + str(compute_agreement_AMT(file_annotations='./GROUND-TRUTH/Results-MTurks/12.csv', in_score_a_column_idx=6, in_score_b_column_idx=8)))
print('Medical robot ' + str(compute_agreement_AMT(file_annotations='./GROUND-TRUTH/Results-MTurks/14.csv', in_score_a_column_idx=7, in_score_b_column_idx=9)))
print('Sport rehab machine ' + str(compute_agreement_AMT(file_annotations='./GROUND-TRUTH/Results-MTurks/13.csv', in_score_a_column_idx=8, in_score_b_column_idx=10)))
   


