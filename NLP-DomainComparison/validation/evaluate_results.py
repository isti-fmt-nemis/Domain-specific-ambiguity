'''
Created on Sep 21, 2018

@author: alessioferrari

This module includes all the methods to evaluate the results of with
respect to the ranked lists of terms.
'''
from __future__ import division

from _collections import defaultdict
import csv
import operator
from pprint import pprint
from random import sample
from numpy.ma.core import fabs

import scipy.stats

import numpy as np


evaluation_dictionary_AMT = {'exactly the same':1,
                         'almost the same':2, 
                         'somewhat different':3,
                         'extremely different':4}

    
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





