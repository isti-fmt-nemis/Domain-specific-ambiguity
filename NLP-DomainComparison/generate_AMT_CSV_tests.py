'''
Created on Sep 20, 2018

@author: alessioferrari
'''
from validation.generate_AMT_CSV import generate_CSV, get_random_sentence_slow, \
    get_random_sentence
from validation.merge_documents import merge_domains, sample_and_merge_domains


# def test_random_sentence_slow():
#     print(get_random_sentence_slow('Computer_Science_D_2.txt', 'cell'))
#     
# def test_random_sentence_fast():
#     print(get_random_sentence('Computer_Science_D_2.txt', 'cell'))
# 
# def test_merge_domains():
#     merge_domains('DATASETS', './DATASETS-Merge')
#     
# def test_sample_and_merge_domains():
#     sample_and_merge_domains('DATASETS', './DATASETS-Merge-Sampled/', s_size = 2000)


term_list_top_bottom = dict()

term_list_top_bottom['CS_EEN'] = ['cell', 'logic', 'format', 'interface', 'content', 'field', 'theory', 'signal', 'video', 'power',  'space', 'performance', 'term', 'conference', 'number', 'example', 'computer', 'system', 'point', 'science']
term_list_top_bottom['CS_MEN'] = ['tool', 'version', 'law', 'software', 'theory', 'matrix', 'frequency', 'path', 'engine', 'life',  'problem', 'state', 'cost', 'test', 'space', 'time', 'range', 'term', 'year', 'example']
term_list_top_bottom['CS_MED'] = ['cell', 'surface', 'result', 'theory', 'function', 'device', 'agent', 'image', 'solution', 'condition',  'report', 'article', 'issue', 'history', 'student', 'award', 'time', 'term', 'range', 'year']
term_list_top_bottom['CS_SPO'] = ['surface','distance','college','energy','length','result','condition','technique','table','goal','history','june','september','student','time','award','march','october','range','year']

file_list = dict()

DOCUMENTS_DIR = 'DATASETS-Merge-Sampled/'
#DOCUMENTS_DIR = 'DATASETS-Merge'

file_list['CS_EEN'] = [DOCUMENTS_DIR + 'Computer_Science_D_2.txt', DOCUMENTS_DIR + 'Electronic_Engineering_D_2.txt']
file_list['CS_MEN'] = [DOCUMENTS_DIR + 'Computer_Science_D_2.txt', DOCUMENTS_DIR + 'Mechanical_Engineering_D_2.txt']
file_list['CS_MED'] = [DOCUMENTS_DIR + 'Computer_Science_D_2.txt', DOCUMENTS_DIR + 'Medicine_D_2.txt']
file_list['CS_SPO'] = [DOCUMENTS_DIR + 'Computer_Science_D_2.txt', DOCUMENTS_DIR + 'Sports_D_2.txt']

SENT_NUM = 3

if __name__ == '__main__':
    
    term_list = term_list_top_bottom
     
    generate_CSV(term_list['CS_EEN'], file_list['CS_EEN'], SENT_NUM, 'CSV-AMT-Sample/CS_EEN.csv')
    generate_CSV(term_list['CS_MEN'], file_list['CS_MEN'], SENT_NUM, 'CSV-AMT-Sample/CS_MEN.csv')
    generate_CSV(term_list['CS_MED'], file_list['CS_MED'], SENT_NUM, 'CSV-AMT-Sample/CS_MED.csv')
    generate_CSV(term_list['CS_SPO'], file_list['CS_SPO'], SENT_NUM, 'CSV-AMT-Sample/CS_SPO.csv')
    
    pass