'''
Created on Oct 17, 2018

@author: alessioferrari

This module provides support to perform qualitative analysis of the results, 
by comparing automated rankings with manual ones, 1st and 2nd iteration. 
'''

import numpy as np
from validation.evaluate_results import get_term_value_dictionary_AMT, get_term_value_dictionary

#Ground-truth
CS_EEN_f03_w2vlen_100_dlen_200_top = ['interpretation', 'formula', 'flash', 'relation', 'motor', 'bell', 'studio', 'contact', 'surface', 'news', 'capacity', 'solution', 'law', 'period', 'transfer', 'force', 'cycle', 'mapping', 'layer', 'output']
CS_MEN_f03_w2vlen_100_dlen_200_top = ['hull', 'bar', 'room', 'option', 'argument', 'reduction', 'disk', 'interpretation', 'expression', 'house', 'year', 'link', 'phase', 'film', 'block', 'customer', 'transfer', 'order', 'report', 'distance']
CS_MED_f03_w2vlen_100_dlen_200_top = ['strength', 'editor', 'client', 'mouse', 'relation', 'matrix', 'pair', 'arm', 'argument', 'house', 'government', 'speech', 'word', 'germany', 'matter', 'success', 'community', 'transfer', 'location', 'class']
CS_SPO_f03_w2vlen_100_dlen_200_top = ['formula', 'loop', 'reduction', 'michael', 'founder', 'effect', 'string', 'washington', 'protein', 'statement', 'corporation', 'procedure', 'government', 'education', 'party', 'opportunity', 'selection', 'steve', 'interest', 'practice']

medical_device_f03_w2vlen_100_dlen_200_top = ['interpretation', 'arm', 'expression', 'formula', 'argument', 'relation', 'consequence', 'client', 'house', 'surface', 'supply', 'desktop', 'authority', 'software', 'society', 'presence', 'byte', 'science', 'combination', 'provider']
medical_robot_f03_w2vlen_100_dlen_200_top = ['argument', 'expression', 'consequence', 'relation', 'institution', 'formula', 'respect', 'statement', 'father', 'ion', 'glass', 'partner', 'structure', 'laboratory', 'part', 'author', 'detector', 'message', 'sin', 'concept']
sport_rehab_machine_f03_w2vlen_100_dlen_200_top = ['founder', 'argument', 'brother', 'end', 'michael', 'consequence', 'story', 'ray', 'respect', 'statement', 'lack', 'context', 'complexity', 'practice', 'opening', 'panel', 'bike', 'experience', 'stage', 'rail']


def get_gt_rank(dict_a, dict_b):
    
    dict_merge = {}
    for k in dict_a.keys():
        dict_merge[k] = np.mean([dict_a[k],dict_b[k]]) 
    gt_rank = sorted(dict_merge, key=dict_merge.get, reverse=True)
    
    return gt_rank


#Iteration 1
def generate_ranked_list_iteration_1(file_annotation_a, file_annotation_b, in_score_column_idx, in_term_column_idx):
    
    dictionary_a = get_term_value_dictionary(file_annotation_a, in_score_column_idx, in_term_column_idx)
    dictionary_b = get_term_value_dictionary(file_annotation_b, in_score_column_idx, in_term_column_idx)
      
    ground_truth_rank = get_gt_rank(dictionary_a, dictionary_b)
    return ground_truth_rank

#Iteration 2
def generate_ranked_list_iteration_2(file_annotations, in_score_a_column_idx=5, in_score_b_column_idx=7, in_term_column_idx=1):
    
    dictionary_a = get_term_value_dictionary_AMT(file_annotations, in_score_a_column_idx, in_term_column_idx)
    dictionary_b = get_term_value_dictionary_AMT(file_annotations, in_score_b_column_idx, in_term_column_idx)
    
    ground_truth_rank = get_gt_rank(dictionary_a, dictionary_b)
    
    return ground_truth_rank



ranks_dictionary = dict()
 
CS_EEN_1 = generate_ranked_list_iteration_1(file_annotation_a='./Results-Andrea-10.10.18/10a.csv', file_annotation_b='./Results-Alessio-10.10.18/10.csv',in_score_column_idx=3, in_term_column_idx=0)
CS_EEN_2 = generate_ranked_list_iteration_2(file_annotations='./Results-AMT-9.10.18/res-10.csv')
 
ranks_dictionary['CS EEN'] = [CS_EEN_f03_w2vlen_100_dlen_200_top, CS_EEN_1, CS_EEN_2]
 
CS_MEN_1 = generate_ranked_list_iteration_1(file_annotation_a='./Results-Andrea-10.10.18/9a.csv', file_annotation_b='./Results-Alessio-10.10.18/9.csv',in_score_column_idx=3, in_term_column_idx=0)
CS_MEN_2 = generate_ranked_list_iteration_2(file_annotations='./Results-AMT-11.10.18/res-9.csv')
 
ranks_dictionary['CS MEN'] = [CS_MEN_f03_w2vlen_100_dlen_200_top, CS_MEN_1, CS_MEN_2]
 
CS_MED_1 = generate_ranked_list_iteration_1(file_annotation_a='./Results-Andrea-10.10.18/11a.csv', file_annotation_b='./Results-Alessio-10.10.18/11.csv',in_score_column_idx=3, in_term_column_idx=0)
CS_MED_2 = generate_ranked_list_iteration_2(file_annotations='./Results-AMT-9.10.18/res-11.csv')
 
ranks_dictionary['CS MED'] = [CS_MED_f03_w2vlen_100_dlen_200_top, CS_MED_1, CS_MED_2]
 
CS_SPO_1 = generate_ranked_list_iteration_1(file_annotation_a='./Results-Andrea-10.10.18/8a.csv', file_annotation_b='./Results-Alessio-10.10.18/8.csv',in_score_column_idx=3, in_term_column_idx=0)
CS_SPO_2 = generate_ranked_list_iteration_2(file_annotations='./Results-AMT-9.10.18/res-8.csv')
 
ranks_dictionary['CS SPO'] = [CS_SPO_f03_w2vlen_100_dlen_200_top, CS_SPO_1, CS_SPO_2]

med_device_1 = generate_ranked_list_iteration_1(file_annotation_a='./Results-Andrea-10.10.18/12a.csv', file_annotation_b='./Results-Alessio-10.10.18/12.csv',in_score_column_idx=4, in_term_column_idx=0)
med_device_2 = generate_ranked_list_iteration_2(file_annotations='./Results-AMT-11.10.18/res-12.csv', in_score_a_column_idx=6, in_score_b_column_idx=8)

ranks_dictionary['Medical device'] = [medical_device_f03_w2vlen_100_dlen_200_top, med_device_1, med_device_2]

med_robot_1 = generate_ranked_list_iteration_1(file_annotation_a='./Results-Andrea-10.10.18/14a.csv', file_annotation_b='./Results-Alessio-10.10.18/14.csv',in_score_column_idx=5, in_term_column_idx=0)
med_robot_2 = generate_ranked_list_iteration_2(file_annotations='./Results-AMT-11.10.18/res-14.csv', in_score_a_column_idx=7, in_score_b_column_idx=9)

ranks_dictionary['Medical robot'] = [medical_robot_f03_w2vlen_100_dlen_200_top, med_robot_1, med_robot_2]

sport_rehab_1 = generate_ranked_list_iteration_1(file_annotation_a='./Results-Andrea-10.10.18/13a.csv', file_annotation_b='./Results-Alessio-10.10.18/13.csv',in_score_column_idx=6, in_term_column_idx=0)
sport_rehab_2 = generate_ranked_list_iteration_2(file_annotations='./Results-AMT-11.10.18/res-13.csv', in_score_a_column_idx=8, in_score_b_column_idx=10)

ranks_dictionary['Sport rehab machine'] = [sport_rehab_machine_f03_w2vlen_100_dlen_200_top, sport_rehab_1, sport_rehab_2]

for k in ranks_dictionary.keys():
    print(k)
    for term_list in ranks_dictionary[k]:
        print(term_list)




# print('\nAndrea\'s \& Alessio\'s Evaluation\n')
# 
# print('CS EEN ' + str(generate_ranked_list_iteration_1(file_annotation_a='./Results-Andrea-10.10.18/10a.csv', file_annotation_b='./Results-Alessio-10.10.18/10.csv',in_score_column_idx=3, in_term_column_idx=0)))
# print('CS MEN ' + str(generate_ranked_list_iteration_1(file_annotation_a='./Results-Andrea-10.10.18/9a.csv', file_annotation_b='./Results-Alessio-10.10.18/9.csv',in_score_column_idx=3, in_term_column_idx=0)))
# print('CS MED ' + str(generate_ranked_list_iteration_1(file_annotation_a='./Results-Andrea-10.10.18/11a.csv', file_annotation_b='./Results-Alessio-10.10.18/11.csv',in_score_column_idx=3, in_term_column_idx=0)))
# print('CS SPO ' + str(generate_ranked_list_iteration_1(file_annotation_a='./Results-Andrea-10.10.18/8a.csv', file_annotation_b='./Results-Alessio-10.10.18/8.csv',in_score_column_idx=3, in_term_column_idx=0)))
# 
# print('Medical device ' + str(generate_ranked_list_iteration_1(file_annotation_a='./Results-Andrea-10.10.18/12a.csv', file_annotation_b='./Results-Alessio-10.10.18/12.csv',in_score_column_idx=4, in_term_column_idx=0)))
# print('Medical robot ' + str(generate_ranked_list_iteration_1(file_annotation_a='./Results-Andrea-10.10.18/14a.csv', file_annotation_b='./Results-Alessio-10.10.18/14.csv',in_score_column_idx=5, in_term_column_idx=0)))
# print('Sport rehab machine ' + str(generate_ranked_list_iteration_1(file_annotation_a='./Results-Andrea-10.10.18/13a.csv', file_annotation_b='./Results-Alessio-10.10.18/13.csv',in_score_column_idx=6, in_term_column_idx=0)))
# 
# print('\nMechanical Turks\' Evaluation\n')
# 
# print('CS EEN ' + str(generate_ranked_list_iteration_2(file_annotations='./Results-AMT-9.10.18/res-10.csv')))
# print('CS MEN ' + str(generate_ranked_list_iteration_2(file_annotations='./Results-AMT-11.10.18/res-9.csv')))
# print('CS MED ' + str(generate_ranked_list_iteration_2(file_annotations='./Results-AMT-9.10.18/res-11.csv')))
# print('CS SPO ' + str(generate_ranked_list_iteration_2(file_annotations='./Results-AMT-9.10.18/res-8.csv')))
# 
# print('Medical device ' + str(generate_ranked_list_iteration_2(file_annotations='./Results-AMT-11.10.18/res-12.csv', in_score_a_column_idx=6, in_score_b_column_idx=8)))
# print('Medical robot ' + str(generate_ranked_list_iteration_2(file_annotations='./Results-AMT-11.10.18/res-14.csv', in_score_a_column_idx=7, in_score_b_column_idx=9)))
# print('Sport rehab machine ' + str(generate_ranked_list_iteration_2(file_annotations='./Results-AMT-11.10.18/res-13.csv', in_score_a_column_idx=8, in_score_b_column_idx=10)))
                                                                    
                                                                    
                                                                    