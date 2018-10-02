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
from random import sample



def evaluate_results_top_bottom():
    return 0

def compute_AMT_scores():
    return 0

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
    
    