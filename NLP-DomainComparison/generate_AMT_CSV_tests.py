'''
Created on Sep 20, 2018

@author: alessioferrari
'''
from validation.generate_AMT_CSV import generate_CSV, get_random_sentence_slow, \
    get_random_sentence
from validation.merge_documents import merge_domains


def test_random_sentence_slow():
    print(get_random_sentence_slow('Computer_Science_D_2.txt', 'cell'))
    
def test_random_sentence_fast():
    print(get_random_sentence('Computer_Science_D_2.txt', 'cell'))

def test_merge_domains():
    merge_domains('DATASETS', './')




term_list = dict()

term_list['CS_EEN'] = ['']
term_list['CS_MEN'] = ['']
term_list['CS_MED'] = ['']
term_list['CS_SPO'] = ['surface','distance','college','energy','length','result','condition','technique','table','goal','history','june','september','student','time','award','march','october','range','year']

file_list = dict()

file_list['CS_EEN'] = ['Computer_Science_D_2.txt', 'Electronic_Engineering_D_2.txt']
file_list['CS_MEN'] = ['Computer_Science_D_2.txt', 'Mechanical_Engineering_D_2.txt']
file_list['CS_MED'] = ['Computer_Science_D_2.txt', 'Medicine_D_2.txt']
file_list['CS_SPO'] = ['Computer_Science_D_2.txt', 'Sports_D_2.txt']

SENT_NUM = 3

if __name__ == '__main__':
    
#     generate_CSV(term_list['CS_EEN'], file_list['CS_EEN'], SENT_NUM, 'CS_EEN.csv')
#     generate_CSV(term_list['CS_MEN'], file_list['CS_MEN'], SENT_NUM, 'CS_EEN.csv')
#     generate_CSV(term_list['CS_MED'], file_list['CS_MED'], SENT_NUM, 'CS_EEN.csv')
    generate_CSV(term_list['CS_SPO'], file_list['CS_SPO'], SENT_NUM, 'CS_SPO.csv')
    
    pass