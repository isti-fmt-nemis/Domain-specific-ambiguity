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


def evaluate_results_top_bottom():
    return 0

def compute_AMT_scores():
    return 0