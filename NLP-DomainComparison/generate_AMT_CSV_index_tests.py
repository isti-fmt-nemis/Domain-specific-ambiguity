'''
Created on Sep 20, 2018

@author: alessioferrari
'''
from validation.generate_AMT_CSV_index import generate_CSV_from_index


term_list_top_bottom = dict()

term_list_top_bottom['CS_EEN'] = ['tv', 'broadcast', 'processor', 'engineering', 'type', 'electron', 'memory', 'user', 'development', 'hardware', 'version', 'time', 'language', 'window', 'file', 'material', 'display', 'color', 'series', 'video']
term_list_top_bottom['CS_MEN'] = ['input', 'engineering', 'field', 'memory', 'area', 'motor', 'processing', 'type', 'level', 'server', 'language', 'system', 'window', 'file', 'material', 'force', 'air', 'wave', 'water', 'engine']
term_list_top_bottom['CS_MED'] = ['result', 'procedure', 'level', 'day', 'year', 'analysis', 'memory', 'tool', 'engineering', 'input', 'test', 'infection', 'blood', 'disease', 'cell', 'syndrome', 'medicine', 'tumor', 'woman', 'health']
term_list_top_bottom['CS_SPO'] = [ 'conference', 'type', 'medal', 'level', 'award', 'score', 'training', 'year', 'input', 'memory', 'language', 'window', 'file', 'ball', 'cricket', 'sport', 'rule', 'series', 'horse', 'opponent']

term_list_top_bottom['sport_rehab'] = []

domain_list_CS_EEN = {"./DATASETS/Computer_Science_D_2": "./INDEXES/CS_dictionary.pkl", 
                      "./DATASETS/Electronic_Engineering_D_2": "./INDEXES/EEN_dictionary.pkl"}

domain_list_CS_MEN = {"./DATASETS/Computer_Science_D_2": "./INDEXES/CS_dictionary.pkl", 
                      "./DATASETS/Mechanical_Engineering_D_2": "./INDEXES/MEN_dictionary.pkl"}
    
domain_list_CS_MED = {"./DATASETS/Computer_Science_D_2": "./INDEXES/CS_dictionary.pkl", 
                      "./DATASETS/Medicine_D_2" : "./INDEXES/MED_dictionary.pkl"}    

domain_list_CS_SPO = {"./DATASETS/Computer_Science_D_2": "./INDEXES/CS_dictionary.pkl", 
                      "./DATASETS/Sports_D_2" : "./INDEXES/SPO_dictionary.pkl"} 

domain_list_medical_device = {"./DATASETS/Computer_Science_D_2": "./INDEXES/CS_dictionary.pkl", 
                      "./DATASETS/Electronic_Engineering_D_2": "./INDEXES/EEN_dictionary.pkl", 
                      "./DATASETS/Medicine_D_2" : "./INDEXES/MED_dictionary.pkl"}

domain_list_medical_robot = {"./DATASETS/Computer_Science_D_2": "./INDEXES/CS_dictionary.pkl", 
                      "./DATASETS/Electronic_Engineering_D_2": "./INDEXES/EEN_dictionary.pkl", 
                      "./DATASETS/Medicine_D_2" : "./INDEXES/MED_dictionary.pkl", 
                      "./DATASETS/Mechanical_Engineering_D_2": "./INDEXES/MEN_dictionary.pkl"}

domain_list_sport_rehab = {"./DATASETS/Computer_Science_D_2": "./INDEXES/CS_dictionary.pkl", 
                      "./DATASETS/Electronic_Engineering_D_2": "./INDEXES/EEN_dictionary.pkl", 
                      "./DATASETS/Medicine_D_2" : "./INDEXES/MED_dictionary.pkl", 
                      "./DATASETS/Mechanical_Engineering_D_2": "./INDEXES/MEN_dictionary.pkl",
                      "./DATASETS/Sports_D_2" : "./INDEXES/SPO_dictionary.pkl"}
  


    

SENT_NUM = 3

if __name__ == '__main__':
    
    term_list = term_list_top_bottom
     
    generate_CSV_from_index(term_list['sport_rehab'], domain_list_sport_rehab, SENT_NUM, './CSV-AMT-Index/sport_rehab.csv') 
     
#     generate_CSV_from_index(term_list['CS_EEN'], domain_list_CS_EEN, SENT_NUM, './CSV-AMT-Index/CS_EEN.csv')
#     generate_CSV_from_index(term_list['CS_MEN'], domain_list_CS_MEN, SENT_NUM, './CSV-AMT-Index/CS_MEN.csv')
#     generate_CSV_from_index(term_list['CS_MED'], domain_list_CS_MED, SENT_NUM, './CSV-AMT-Index/CS_MED.csv')
#     generate_CSV_from_index(term_list['CS_SPO'], domain_list_CS_SPO, SENT_NUM, './CSV-AMT-Index/CS_SPO.csv')
    
    
    pass