'''
Created on May 19, 2017

@author: alessioferrari
'''
import nltk
from nltk.probability import FreqDist

from domainanalysismain import get_all_text, get_clean_text_tokens


INPUT_PATH_CS = "../DATASETS/Computer science_D_2"
INPUT_PATH_EE = "../DATASETS/Electronic_Engineering_D2"
INPUT_PATH_ME = "../DATASETS/Mechanical engineering_D_2"
INPUT_PATH_MED = "../DATASETS/Medicine_D_2"
INPUT_PATH_LIT = "../DATASETS/Literature_D2"
INPUT_PATH_AUT = "../DATASETS/Automobiles_D2"
INPUT_PATH_SPO = "../DATASETS/Sports_D_2"

FREQ_LIST = [
"system", 
"computer",
"software",
"data",
"time",
"user",
"application", 
"model", 
"information", 
"problem", 
"function", 
"language", 
"algorithm", 
"science", 
"university", 
"program", 
"set", 
"use", 
"method", 
"research"  
    ]


def print_tokens_freq(input_path):
    print(input_path)
    tokens = get_clean_text_tokens(get_all_text(input_path))
    freq = FreqDist(tokens)
    string =  str(len(tokens)) + " & " + str(len(freq.keys())) 
    print(string)
    

    
def print_k_tokens_freq(input_path_list, tok_list):
    
    freq = dict()
    
    for input_path in input_path_list:
        tokens = get_clean_text_tokens(get_all_text(input_path))
        freq[input_path] = FreqDist(tokens)
        
    for tok in tok_list:
        string_to_print = []
        for in_path in freq.keys():
            print(in_path)
            string_to_print.append(str(freq[in_path][tok]))
        print(tok)
        
        print(' & '.join(string_to_print))

if __name__ == '__main__':
    
    print_tokens_freq(INPUT_PATH_CS)
#     print_tokens_freq(INPUT_PATH_EE)
#     print_tokens_freq(INPUT_PATH_ME)    
#     print_tokens_freq(INPUT_PATH_MED) 
#     print_tokens_freq(INPUT_PATH_LIT) 
#     print_tokens_freq(INPUT_PATH_AUT) 
#     print_tokens_freq(INPUT_PATH_SPO) 
        
    print_k_tokens_freq([INPUT_PATH_CS, INPUT_PATH_EE, INPUT_PATH_ME, INPUT_PATH_MED, INPUT_PATH_LIT, INPUT_PATH_AUT, INPUT_PATH_SPO], FREQ_LIST)
    pass