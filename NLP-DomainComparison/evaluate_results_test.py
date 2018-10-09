'''
Created on Oct 3, 2018

@author: alessioferrari
'''

from sklearn.metrics.classification import cohen_kappa_score

import numpy as np
from validation.evaluate_results import build_automated_sets, \
    get_term_value_dictionary, evaluate_results_top_bottom_rank, \
    get_term_value_list, get_term_value_dictionary_AMT, convert_score, \
    get_term_value_list_AMT, compute_score_overlap, reduce_score, \
    evaluate_results_top_bottom_optimistic


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



def compute_results_from_AMT(auto_list, set_separator_index, file_annotations, in_score_a_column_idx=5, in_score_b_column_idx=7, in_term_column_idx=1):
    auto_s = build_automated_sets(auto_list, set_separator_index)
    dictionary_a = get_term_value_dictionary_AMT(file_annotations, in_score_a_column_idx, in_term_column_idx)
    dictionary_b = get_term_value_dictionary_AMT(file_annotations, in_score_b_column_idx, in_term_column_idx)
    
    dictionary_merge = {}
    for k in dictionary_a.keys():
        dictionary_merge[k] = np.mean([dictionary_a[k],dictionary_b[k]]) 
    ground_truth_rank = sorted(dictionary_merge, key=dictionary_merge.get, reverse=True)
    
    tau_result = evaluate_results_top_bottom_rank(ground_truth_ranked_list=ground_truth_rank, auto_sets=auto_s)
    
    tau_result_ties = evaluate_results_top_bottom_optimistic(dictionary_merge, auto_s)
    
    scores_literal_a = get_term_value_list_AMT(file_annotations, score_column_idx = in_score_a_column_idx)
    scores_literal_b = get_term_value_list_AMT(file_annotations, score_column_idx = in_score_b_column_idx)
    
    scores_a = [convert_score(s) for s in scores_literal_a]
    scores_b = [convert_score(s) for s in scores_literal_b]
    k_result = cohen_kappa_score(scores_a, scores_b)
    k_percent = compute_score_overlap(scores_a, scores_b)
    
    scores_a_permissive = [reduce_score(s_a) for s_a in scores_a] 
    scores_b_permissive = [reduce_score(s_b) for s_b in scores_b]
    k_result_permissive = cohen_kappa_score(scores_a_permissive, scores_b_permissive)
    k_permissive_percent = compute_score_overlap(scores_a_permissive, scores_b_permissive)
    
    return [k_result, k_percent, k_result_permissive, k_permissive_percent, tau_result, tau_result_ties]

        

# auto_list_1 = ['institute', 'theory', 'environment', 'distance', 'matrix', 'length', 'release', 'tool', 'law', 'frequency', 'business', 'distribution', 'output', 'issue', 'component', 'team', 'machine', 'concept', 'performance', 'approach']
# print(compute_results(auto_list=auto_list_1, set_separator_index=10, file_annotation_a='./validation/1_a.csv', file_annotation_b='./validation/1_b.csv', in_score_column_idx=3, in_term_column_idx=0))
# auto_list_7 = ['environment', 'board', 'table', 'law', 'institute', 'value', 'pattern', 'surface', 'tool', 'chemical', 'area', 'server', 'heat', 'rule', 'solution', 'range', 'condition', 'issue', 'user', 'report']
# print(compute_results(auto_list=auto_list_7, set_separator_index=10, file_annotation_a='./validation/7_a.csv', file_annotation_b='./validation/7_b.csv', in_score_column_idx=5, in_term_column_idx=0))
# 
# auto_list_1_trick = ['frequency', 'length', 'matrix', 'institute', 'release', 'tool', 'environment', 'law', 'theory', 'distance', 'problem', 'time', 'space', 'range', 'state', 'term', 'cost', 'year', 'example', 'test']
# print(compute_results(auto_list=auto_list_1_trick, set_separator_index=10, file_annotation_a='./validation/100_a.csv', file_annotation_b='./validation/100_b.csv', in_score_column_idx=3, in_term_column_idx=0))
# 
# auto_list_1_min_freq = ['hull', 'bar', 'room', 'option', 'argument', 'reduction', 'disk', 'interpretation', 'expression', 'house', 'year', 'link', 'phase', 'film', 'block', 'customer', 'transfer', 'order', 'report', 'distance']
# print(compute_results(auto_list=auto_list_1_min_freq, set_separator_index=10, file_annotation_a='./validation/101_a.csv', file_annotation_b='./validation/101_b.csv', in_score_column_idx=3, in_term_column_idx=0))
# print(compute_results_from_AMT(auto_list=auto_list_1_min_freq, set_separator_index=10, file_annotations='./validation/AMT_results.csv'))
#       
# auto_list_12 = ['interpretation', 'arm', 'expression', 'formula', 'argument', 'relation', 'consequence', 'client', 'house', 'surface', 'supply', 'desktop', 'authority', 'software', 'society', 'presence', 'byte', 'science', 'combination', 'provider']
# print(compute_results(auto_list=auto_list_12, set_separator_index=10, file_annotation_a='./validation/12.csv', file_annotation_b='./validation/12.csv', in_score_column_idx=4, in_term_column_idx=0))      
#       
# auto_list_13 = ['founder', 'argument', 'brother', 'end', 'michael', 'consequence', 'story', 'ray', 'respect', 'statement', 'lack', 'context', 'complexity', 'practice', 'opening', 'panel', 'bike', 'experience', 'stage', 'rail']
# print(compute_results(auto_list=auto_list_13, set_separator_index=10, file_annotation_a='./validation/13.csv', file_annotation_b='./validation/13.csv', in_score_column_idx=6, in_term_column_idx=0))      

CS_EEN_f03_w2vlen_100_dlen_200_top = ['interpretation', 'formula', 'flash', 'relation', 'motor', 'bell', 'studio', 'contact', 'surface', 'news', 'capacity', 'solution', 'law', 'period', 'transfer', 'force', 'cycle', 'mapping', 'layer', 'output']
CS_MEN_f03_w2vlen_100_dlen_200_top = ['disk', 'room', 'expression', 'hull', 'reduction', 'option', 'bar', 'house', 'interpretation', 'argument', 'track', 'family', 'action', 'molecule', 'law', 'theory', 'life', 'production', 'source', 'tool']
CS_MED_f03_w2vlen_100_dlen_200_top = ['strength', 'editor', 'client', 'mouse', 'relation', 'matrix', 'pair', 'arm', 'argument', 'house', 'government', 'speech', 'word', 'germany', 'matter', 'success', 'community', 'transfer', 'location', 'class']
CS_SPO_f03_w2vlen_100_dlen_200_top = ['formula', 'loop', 'reduction', 'michael', 'founder', 'effect', 'string', 'washington', 'protein', 'statement', 'corporation', 'procedure', 'government', 'education', 'party', 'opportunity', 'selection', 'steve', 'interest', 'practice']

print('CS SPO ' + str(compute_results_from_AMT(auto_list=CS_SPO_f03_w2vlen_100_dlen_200_top, set_separator_index=10, file_annotations='./Results-AMT-9.10.18/res-8.csv')))
print('CS MEN ' + str(compute_results_from_AMT(auto_list=CS_MEN_f03_w2vlen_100_dlen_200_top, set_separator_index=10, file_annotations='./Results-AMT-9.10.18/res-9.csv')))
print('CS EEN ' + str(compute_results_from_AMT(auto_list=CS_EEN_f03_w2vlen_100_dlen_200_top, set_separator_index=10, file_annotations='./Results-AMT-9.10.18/res-10.csv')))
print('CS MED ' + str(compute_results_from_AMT(auto_list=CS_MED_f03_w2vlen_100_dlen_200_top, set_separator_index=10, file_annotations='./Results-AMT-9.10.18/res-11.csv')))
