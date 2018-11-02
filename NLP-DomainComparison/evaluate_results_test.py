'''
Created on Oct 3, 2018

@author: alessioferrari
'''

import numpy as np
from validation import evaluate_results

def compute_results(auto_list, set_separator_index, file_annotation_a, file_annotation_b, in_score_column_idx, in_term_column_idx):
    auto_s = evaluate_results.build_automated_sets(auto_list, set_separator_index)
    dictionary_a = evaluate_results.get_term_value_dictionary(file_annotation_a, in_score_column_idx, in_term_column_idx)
    dictionary_b = evaluate_results.get_term_value_dictionary(file_annotation_b, in_score_column_idx, in_term_column_idx)
      
    dictionary_merge = {}
    for k in dictionary_a.keys():
        dictionary_merge[k] = np.mean([dictionary_a[k],dictionary_b[k]]) 
    
    tau_result_skip_ties = evaluate_results.evaluate_results_top_bottom_skip_ties(dictionary_merge, auto_s)
    
    return tau_result_skip_ties 



def compute_results_from_AMT(auto_list, set_separator_index, file_annotations, in_score_a_column_idx=5, in_score_b_column_idx=7, in_term_column_idx=1):
    auto_s = evaluate_results.build_automated_sets(auto_list, set_separator_index)
    dictionary_a = evaluate_results.get_term_value_dictionary_AMT(file_annotations, in_score_a_column_idx, in_term_column_idx)
    dictionary_b = evaluate_results.get_term_value_dictionary_AMT(file_annotations, in_score_b_column_idx, in_term_column_idx)
    
    dictionary_merge = {}
    for k in dictionary_a.keys():
        dictionary_merge[k] = np.mean([dictionary_a[k],dictionary_b[k]]) 

    tau_result_skip_ties = evaluate_results.evaluate_results_top_bottom_skip_ties(dictionary_merge, auto_s)
    
    return tau_result_skip_ties


CS_EEN_f03_w2vlen_100_dlen_200_top = ['interpretation', 'formula', 'flash', 'relation', 'motor', 'bell', 'studio', 'contact', 'surface', 'news', 'capacity', 'solution', 'law', 'period', 'transfer', 'force', 'cycle', 'mapping', 'layer', 'output']
CS_MEN_f03_w2vlen_100_dlen_200_top = ['hull', 'bar', 'room', 'option', 'argument', 'reduction', 'disk', 'interpretation', 'expression', 'house', 'year', 'link', 'phase', 'film', 'block', 'customer', 'transfer', 'order', 'report', 'distance']
CS_MED_f03_w2vlen_100_dlen_200_top = ['strength', 'editor', 'client', 'mouse', 'relation', 'matrix', 'pair', 'arm', 'argument', 'house', 'government', 'speech', 'word', 'germany', 'matter', 'success', 'community', 'transfer', 'location', 'class']
CS_SPO_f03_w2vlen_100_dlen_200_top = ['formula', 'loop', 'reduction', 'michael', 'founder', 'effect', 'string', 'washington', 'protein', 'statement', 'corporation', 'procedure', 'government', 'education', 'party', 'opportunity', 'selection', 'steve', 'interest', 'practice']

medical_device_f03_w2vlen_100_dlen_200_top = ['interpretation', 'arm', 'expression', 'formula', 'argument', 'relation', 'consequence', 'client', 'house', 'surface', 'supply', 'desktop', 'authority', 'software', 'society', 'presence', 'byte', 'science', 'combination', 'provider']
medical_robot_f03_w2vlen_100_dlen_200_top = ['argument', 'expression', 'consequence', 'relation', 'institution', 'formula', 'respect', 'statement', 'father', 'ion', 'glass', 'partner', 'structure', 'laboratory', 'part', 'author', 'detector', 'message', 'sin', 'concept']
sport_rehab_machine_f03_w2vlen_100_dlen_200_top = ['founder', 'argument', 'brother', 'end', 'michael', 'consequence', 'story', 'ray', 'respect', 'statement', 'lack', 'context', 'complexity', 'practice', 'opening', 'panel', 'bike', 'experience', 'stage', 'rail']


print('\nAndrea\'s \& Alessio\'s Evaluation\n')

print('CS SPO ' + str(compute_results(auto_list=CS_SPO_f03_w2vlen_100_dlen_200_top, set_separator_index=10, file_annotation_a='./Results-Andrea-10.10.18/8a.csv', file_annotation_b='./Results-Alessio-10.10.18/8.csv',in_score_column_idx=3, in_term_column_idx=0)))
print('CS MEN ' + str(compute_results(auto_list=CS_MEN_f03_w2vlen_100_dlen_200_top, set_separator_index=10, file_annotation_a='./Results-Andrea-10.10.18/9a.csv', file_annotation_b='./Results-Alessio-10.10.18/9.csv',in_score_column_idx=3, in_term_column_idx=0)))
print('CS EEN ' + str(compute_results(auto_list=CS_EEN_f03_w2vlen_100_dlen_200_top, set_separator_index=10, file_annotation_a='./Results-Andrea-10.10.18/10a.csv', file_annotation_b='./Results-Alessio-10.10.18/10.csv',in_score_column_idx=3, in_term_column_idx=0)))
print('CS MED ' + str(compute_results(auto_list=CS_MED_f03_w2vlen_100_dlen_200_top, set_separator_index=10, file_annotation_a='./Results-Andrea-10.10.18/11a.csv', file_annotation_b='./Results-Alessio-10.10.18/11.csv',in_score_column_idx=3, in_term_column_idx=0)))

print('Medical device ' + str(compute_results(auto_list=medical_device_f03_w2vlen_100_dlen_200_top, set_separator_index=10, file_annotation_a='./Results-Andrea-10.10.18/12a.csv', file_annotation_b='./Results-Alessio-10.10.18/12.csv',in_score_column_idx=4, in_term_column_idx=0)))
print('Medical robot ' + str(compute_results(auto_list=medical_robot_f03_w2vlen_100_dlen_200_top, set_separator_index=10, file_annotation_a='./Results-Andrea-10.10.18/14a.csv', file_annotation_b='./Results-Alessio-10.10.18/14.csv',in_score_column_idx=5, in_term_column_idx=0)))
print('Sport rehab machine ' + str(compute_results(auto_list=sport_rehab_machine_f03_w2vlen_100_dlen_200_top, set_separator_index=10, file_annotation_a='./Results-Andrea-10.10.18/13a.csv', file_annotation_b='./Results-Alessio-10.10.18/13.csv',in_score_column_idx=6, in_term_column_idx=0)))

print('\nMechanical Turks\' Evaluation\n')

print('CS SPO ' + str(compute_results_from_AMT(auto_list=CS_SPO_f03_w2vlen_100_dlen_200_top, set_separator_index=10, file_annotations='./Results-AMT-9.10.18/res-8.csv')))
print('CS MEN ' + str(compute_results_from_AMT(auto_list=CS_MEN_f03_w2vlen_100_dlen_200_top, set_separator_index=10, file_annotations='./Results-AMT-11.10.18/res-9.csv')))
print('CS EEN ' + str(compute_results_from_AMT(auto_list=CS_EEN_f03_w2vlen_100_dlen_200_top, set_separator_index=10, file_annotations='./Results-AMT-9.10.18/res-10.csv')))
print('CS MED ' + str(compute_results_from_AMT(auto_list=CS_MED_f03_w2vlen_100_dlen_200_top, set_separator_index=10, file_annotations='./Results-AMT-9.10.18/res-11.csv')))

print('Medical device ' + str(compute_results_from_AMT(auto_list=medical_device_f03_w2vlen_100_dlen_200_top, set_separator_index=10, file_annotations='./Results-AMT-11.10.18/res-12.csv', in_score_a_column_idx=6, in_score_b_column_idx=8)))
print('Medical robot ' + str(compute_results_from_AMT(auto_list=medical_robot_f03_w2vlen_100_dlen_200_top, set_separator_index=10, file_annotations='./Results-AMT-11.10.18/res-14.csv', in_score_a_column_idx=7, in_score_b_column_idx=9)))
print('Sport rehab machine ' + str(compute_results_from_AMT(auto_list=sport_rehab_machine_f03_w2vlen_100_dlen_200_top, set_separator_index=10, file_annotations='./Results-AMT-11.10.18/res-13.csv', in_score_a_column_idx=8, in_score_b_column_idx=10)))

