'''
Created on Sep 20, 2018

@author: alessioferrari
'''
from validation.generate_AMT_CSV_index import generate_CSV_from_index


term_list_top_bottom = dict()


'''
Terms generated with the approach that considers the terms that occur at least 800 times in each domain
'''
CS_EEN_f03_w2vlen_100_dlen_200_top = ['interpretation', 'formula', 'flash', 'relation', 'motor', 'bell', 'studio', 'contact', 'surface', 'news', 'capacity', 'solution', 'law', 'period', 'transfer', 'force', 'cycle', 'mapping', 'layer', 'output']
CS_MEN_f03_w2vlen_100_dlen_200_top = ['disk', 'room', 'expression', 'hull', 'reduction', 'option', 'bar', 'house', 'interpretation', 'argument', 'track', 'family', 'action', 'molecule', 'law', 'theory', 'life', 'production', 'source', 'tool']
CS_MED_f03_w2vlen_100_dlen_200_top = ['strength', 'editor', 'client', 'mouse', 'relation', 'matrix', 'pair', 'arm', 'argument', 'house', 'government', 'speech', 'word', 'germany', 'matter', 'success', 'community', 'transfer', 'location', 'class']
CS_SPO_f03_w2vlen_100_dlen_200_top = ['formula', 'loop', 'reduction', 'michael', 'founder', 'effect', 'string', 'washington', 'protein', 'statement', 'corporation', 'procedure', 'government', 'education', 'party', 'opportunity', 'selection', 'steve', 'interest', 'practice']
medical_software_f03_w2vlen_100_dlen_200_top = ['matrix', 'pair', 'house', 'arm', 'mouse', 'argument', 'editor', 'strength', 'relation', 'client', 'location', 'degree', 'university', 'science', 'principle', 'energy', 'production', 'fact', 'claim', 'statement']
medical_device_f03_w2vlen_100_dlen_200_top = ['interpretation', 'arm', 'expression', 'formula', 'argument', 'relation', 'consequence', 'client', 'house', 'surface', 'supply', 'desktop', 'authority', 'software', 'society', 'presence', 'byte', 'science', 'combination', 'provider']
medical_robot_f03_w2vlen_100_dlen_200_top = ['argument', 'expression', 'consequence', 'relation', 'institution', 'formula', 'respect', 'statement', 'father', 'ion', 'glass', 'partner', 'structure', 'laboratory', 'part', 'author', 'detector', 'message', 'sin', 'concept']
sport_rehab_machine_f03_w2vlen_100_dlen_200_top = ['founder', 'argument', 'brother', 'end', 'michael', 'consequence', 'story', 'ray', 'respect', 'statement', 'lack', 'context', 'complexity', 'practice', 'opening', 'panel', 'bike', 'experience', 'stage', 'rail']



'''
These dictionaries includes couples of "folder including the documents" : "inverted indexes stored in 
pkl files". Each dictionary is associated to a group of domains. 
'''

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
    
    generate_CSV_from_index(CS_EEN_f03_w2vlen_100_dlen_200_top, domain_list_CS_EEN, SENT_NUM, './CSV-AMT-Index/CS_EEN_f03_w2vlen_100_dlen_200_top.csv') 
    generate_CSV_from_index(CS_MEN_f03_w2vlen_100_dlen_200_top, domain_list_CS_MEN, SENT_NUM, './CSV-AMT-Index/CS_MEN_f03_w2vlen_100_dlen_200_top.csv') 
    generate_CSV_from_index(CS_MED_f03_w2vlen_100_dlen_200_top, domain_list_CS_MED, SENT_NUM, './CSV-AMT-Index/CS_MED_f03_w2vlen_100_dlen_200_top.csv') 
    generate_CSV_from_index(CS_SPO_f03_w2vlen_100_dlen_200_top, domain_list_CS_SPO, SENT_NUM, './CSV-AMT-Index/CS_SPO_f03_w2vlen_100_dlen_200_top.csv')
  
    generate_CSV_from_index(medical_device_f03_w2vlen_100_dlen_200_top, domain_list_medical_device, SENT_NUM, './CSV-AMT-Index/medical_device_f03_w2vlen_100_dlen_200_top.csv')
    generate_CSV_from_index(medical_robot_f03_w2vlen_100_dlen_200_top, domain_list_medical_robot, SENT_NUM, './CSV-AMT-Index/medical_robot_f03_w2vlen_100_dlen_200_top.csv')
    generate_CSV_from_index(sport_rehab_machine_f03_w2vlen_100_dlen_200_top, domain_list_sport_rehab, SENT_NUM, './CSV-AMT-Index/sport_rehab_machine_f03_w2vlen_100_dlen_200_top.csv')
     
    pass