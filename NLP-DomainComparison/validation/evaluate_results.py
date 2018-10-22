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

from _collections import defaultdict
import csv
from pprint import pprint
from random import sample
import operator

import numpy as np
from boto.sdb.db.sequence import double


evaluation_dictionary_AMT = {'exactly the same':1,
                         'almost the same':2, 
                         'somewhat different':3,
                         'extremely different':4}

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

def evaluate_results_top_bottom_optimistic(ground_truth_dictionary, auto_sets):
    ambiguous_set = auto_sets[0]
    non_ambiguous_set = auto_sets[1]
    
    #create tuples that are ordered based on the score
    sorted_elems = []
    ground_truth_rank = sorted(ground_truth_dictionary, key=ground_truth_dictionary.get, reverse=True)
    
    for item in ground_truth_rank:
        if item in ambiguous_set:
            sorted_elems.append([item, ground_truth_dictionary[item], 0])
        else:
            sorted_elems.append([item, ground_truth_dictionary[item], 1])
            
                
    dict_ties = defaultdict(list)
    for [term, value, amb] in sorted_elems:
        dict_ties[value].append([term, value, amb])
    
    
    for key in dict_ties.keys():
        dict_ties[key].sort(key=lambda x: x[2])
    
    sorted_dict = sorted(dict_ties.items(), key=operator.itemgetter(0), reverse=True)
    sorted_list = [item for (val, item) in sorted_dict]       
    ranked_list = [word for item_list in sorted_list for [word, _, _] in item_list]                 

    return evaluate_results_top_bottom_rank(ranked_list, auto_sets) 
    
def evaluate_results_top_bottom_skip_ties(ground_truth_dictionary, auto_sets):
    ambiguous_set = auto_sets[0]
    non_ambiguous_set = auto_sets[1]
               
    c_amb = 0
    c_pairs = 0
    
    for ambiguous_term in ambiguous_set:
        ambiguous_term_score = ground_truth_dictionary[ambiguous_term]
        for non_ambiguous_term in non_ambiguous_set:
            non_ambiguous_term_score = ground_truth_dictionary[non_ambiguous_term]
            if ambiguous_term_score>non_ambiguous_term_score:
                c_amb += 1
                c_pairs += 1
            elif ambiguous_term_score < non_ambiguous_term_score:
                c_pairs += 1
        
    tau_value = c_amb / c_pairs 
        
    return tau_value

'''
This function evaluates precision and recall, treating the problem as a classification problem
'''
def evaluate_results_top_bottom_classification(ground_truth_sets, auto_sets):
    
    if len(auto_sets[0]) != 0:
        precision = len(auto_sets[0].intersection(ground_truth_sets[0])) / len(auto_sets[0])
    else:
        precision = float(1)
    
    if len(ground_truth_sets[0]) != 0:
        recall = len(auto_sets[0].intersection(ground_truth_sets[0])) / len(ground_truth_sets[0])
    else:
        recall = float(1)
    
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


def convert_score(string_value):
    return evaluation_dictionary_AMT[string_value.lower()]

def get_term_value_dictionary_AMT(file_scoring, score_column_idx, term_column_idx):
    
    with open(file_scoring, mode='r', encoding='utf-8') as infile:
        reader = list(csv.reader(infile))[1:]
        terms = set([rows[term_column_idx] for rows in reader])
        
        annotation_dictionary = dict()
        for term in terms:
            annotation_dictionary[term] = np.mean([convert_score(rows[score_column_idx]) for rows in reader if rows[term_column_idx] == term])
            
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
Returns the list of scores from a .csv file from AMT,
which includes a header
'''
def get_term_value_list_AMT(file_scoring, score_column_idx):
    
    with open(file_scoring, mode='r', encoding='utf-8') as infile:
        reader = list(csv.reader(infile))[1:]
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

'''
Reduce the scores to two values
'''
def reduce_score(score_value):
    if score_value == 1 or score_value == 2:
        return 1
    else: 
        return 2

'''
Compute overlap between scores of two lists
'''    
def compute_score_overlap(list_a, list_b):
    
    count = 0
    for n, item in enumerate(list_a):
        if list_b[n] == item:
            count += 1
    
    return count/len(list_a)
    









