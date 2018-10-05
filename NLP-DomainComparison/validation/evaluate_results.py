'''
Created on Sep 21, 2018

@author: alessioferrari

This module includes all the methods to evaluate the results of the AMT task with
respect to the ranked lists of terms. Different types of evaluation can be performed.

- precision/recall: we evaluate whether words that are ranked top by the algorithm
(i.e., highly ambiguous) are also ranked top by the raters, and whether words that
are ranked bottom by the algorithm (i.e., low degree of ambiguity) are also ranked
bottom by the raters.
 
- pearson's correlation coefficient: we evaluate the correlation between the position
of the top ambiguous words and their ambiguity evaluation score. This somehow suggests
the validation of the ambiguity score, rather than the list.

- tau-b: enables the comparison between the human vs machine ranking.  
'''
from __future__ import division

import csv
import numpy as np
from pprint import pprint
from random import sample


''''
This function evaluates the results as a ranking with ties. Given the auto_sets,
and the ground_truth_ranked_list coming from the annotation, for each element in the ambiguous set 
in the auto_sets, it computes how many elements of the non-ambiguous set follows 
the specific element of the ambiguous set. Then, it sums-up the contribution
for each element of the ambiguous set, and computes the final evaluation value 
by dividing for the product of the sizes of the non-ambiguous set and ambiguous set. 
'''

def evaluate_results_top_bottom_rank(ground_truth_ranked_list, auto_sets):
    ambiguous_set = auto_sets[0]
    non_ambiguous_set = auto_sets[1]
    
    c_amb = 0
    
    for ambiguous_term in ambiguous_set:
        followers = ground_truth_ranked_list[ground_truth_ranked_list.index(ambiguous_term):]
        c_amb = c_amb + len(set(followers).intersection(set(non_ambiguous_set)))
        
    tau_value = c_amb / (len(ambiguous_set)*len(non_ambiguous_set)) 
        
    return tau_value

'''
This function evaluates precision and recall, treating the problem as a classification problem
'''
def evaluate_results_top_bottom_classification(ground_truth_sets, auto_sets):
    
    precision = len(auto_sets[0].intersection(ground_truth_sets[0])) / len(auto_sets[0])
    recall = len(auto_sets[0].intersection(ground_truth_sets[0])) / len(auto_sets[0])
    
    return [precision, recall]

'''
Given the ordered list of terms to consider, builds the automated sets to be used
for evaluation. The index_separator is the index that divides the two classes.
'''

def build_automated_sets(automated_list, index_separator):
    
    ambiguous_terms = set(automated_list[:index_separator])
    non_ambiguous_terms = set(automated_list[index_separator:])
    
    return [ambiguous_terms, non_ambiguous_terms]  
    
'''
Given a dictionary of couples term:ambiguity_value, creates
the ground truth made of terms that are considered ambiguous,
based on the ambiguity_threshold given as input
'''
def build_ground_truth_sets(term_value_dictionary, ambiguity_threshold):
    
    ambiguous_terms_annotated = set([t for t, v in term_value_dictionary.items() if v >= ambiguity_threshold])
    non_ambiguous_terms_annotated = set([t for t, v in term_value_dictionary.items() if v < ambiguity_threshold])
    
    return [ambiguous_terms_annotated, non_ambiguous_terms_annotated]

'''
Given a .csv file with several terms and their evaluation score, creates
a dictionary to be used for evaluation. Each key of the dictionary
is a term, and the value is the average of the scores obtained.
@param file_scoring: csv file cointaining the scores
@param score_column_idx: index of the column of the csv file in which the score is placed
@param term_colum_ids: index of the column of the csv file in which the term is placed 
'''
def get_term_value_dictionary(file_scoring, score_column_idx, term_column_idx):
    
    with open(file_scoring, mode='r', encoding='utf-8') as infile:
        reader = list(csv.reader(infile))
        terms = set([rows[term_column_idx] for rows in reader])
        
        annotation_dictionary = dict()
        for term in terms:
            annotation_dictionary[term] = np.mean([int(rows[score_column_idx]) for rows in reader if rows[term_column_idx] == term])
            
    return annotation_dictionary    

'''
Returns the list of scores from a .csv file
'''
def get_term_value_list(file_scoring, score_column_idx):
    
    with open(file_scoring, mode='r', encoding='utf-8') as infile:
        reader = list(csv.reader(infile))
        scores = [rows[score_column_idx] for rows in reader]
            
    return scores    
    

'''
Given a list of terms, the function returns a sample of the list that
is constructed as follows: it takes a sample with size = in_sample_size
from the N-top words of the list, where N = in_top_words_num; it takes
another sample with size = in_sample_size, from the remaining words of the list.
The final sample will be 2 * in_sample_size
'''
def generate_ranked_sample_top(in_top_words_num, in_sample_size, in_w_list):
    top_sample = sample(in_w_list[:in_top_words_num], in_sample_size)
    bottom_sample = sample(in_w_list[in_top_words_num:], in_sample_size)
    
    return (top_sample + bottom_sample)


'''
Given a list of terms, generates a sample of the terms that preserves the 
order in the input list. The terms are taken at fixed steps.
'''
def generate_ranked_sample_step(in_sample_size, in_w_list):
    step = len(in_w_list)//in_sample_size
    step_list = in_w_list[0::step]
    return step_list[:in_sample_size]
    
    
##Usage: 
#dictionary_1_a = get_term_value_dictionary('1_a.csv', score_column_idx = 3, term_column_idx = 0)
#ground_1 = build_ground_truth_sets(dictionary_1_a, 3)
#auto_1 = build_automated_sets(['institute', 'theory', 'environment', 'distance', 'matrix', 'length', 'release', 'tool', 'law', 'frequency', 'business', 'distribution', 'output', 'issue', 'component', 'team', 'machine', 'concept', 'performance', 'approach'], 10)
#pprint(evaluate_results_top_bottom_classification(ground_1, auto_1))
 
#dictionary_7 = get_term_value_dictionary('7_a.csv', score_column_idx = 5, term_column_idx = 0)
#ground_7 = build_ground_truth_sets(dictionary_7, 3)
#auto_7 = build_automated_sets(['environment', 'board', 'table', 'law', 'institute', 'value', 'pattern', 'surface', 'tool', 'chemical', 'area', 'server', 'heat', 'rule', 'solution', 'range', 'condition', 'issue', 'user', 'report'], 10)
#pprint(evaluate_results_top_bottom_classification(ground_7, auto_7))
 
 
# ground_truth_rank_7 = sorted(dictionary_7, key=dictionary_7.get, reverse=True)
# tau_result_7 = evaluate_results_top_bottom_rank(ground_truth_ranked_list=ground_truth_rank_7, auto_sets=auto_7)
# print(tau_result_7)
 
# ground_truth_rank_1 = sorted(dictionary_1_a, key=dictionary_1_a.get, reverse=True)
# tau_result_1 = evaluate_results_top_bottom_rank(ground_truth_ranked_list=ground_truth_rank_1, auto_sets=auto_1)
# print(tau_result_1)








