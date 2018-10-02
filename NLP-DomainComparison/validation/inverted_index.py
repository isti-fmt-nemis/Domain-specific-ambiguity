'''
Created on Oct 1, 2018

@author: alessioferrari

This module includes the methods to create an inverted index from 
the different domain documents, given a domain folder with .txt documents.
'''

'''
Given an input folder with .txt files produces an inverted index and stores it in a csv file
'''

from _collections import defaultdict
from glob import glob
import os
import pickle
from random import sample

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize


stop_words = set(stopwords.words('english'))

def get_dictionary(in_folder):

    inverted_index = defaultdict(list)
 
    file_list = glob(in_folder+"/*.txt")
 
    for count, f in enumerate(file_list):
        print(count)
        with open(f,  mode = 'r', encoding='utf-8') as infile:
            raw_file = infile.read()
            raw_file_tokens = [w.lower() for w in word_tokenize(raw_file) if w.lower() not in stop_words and w.isalpha()]
            raw_file_token_set = set(raw_file_tokens)
            for w in raw_file_token_set:
                inverted_index[w].append(os.path.basename(f))                    

    return inverted_index
             

def create_index(in_folder, out_index_file):
    dictionary = get_dictionary(in_folder)
    f = open(out_index_file,"wb")
    pickle.dump(dictionary,f)
    f.close()
    
def load_index(index_file):
    inv_index = pickle.load(open(index_file, "rb" ))
    return inv_index
    
def get_sentence_from_file(file_path, term, sent_max_len = 200, sent_min_len = 50):
    with open(file_path, mode="r", encoding="utf-8") as f:
        raw = f.read()
        sentences = sent_tokenize(raw)
        s = ""
        for sent in sentences: 
            if term in [t.lower() for t in word_tokenize(sent)]:
                if len(sent) < sent_max_len and len(sent) > sent_min_len and not sent.startswith(u'='):
                    s = sent
                    break
        return s
    
def get_random_sentence_index(term, in_folder, in_inv_index):   
    inv_index = in_inv_index
    files = inv_index[term]
    
    s = ""
    
    while True:
        selected = sample(files, 1)[0]
        file_path = in_folder + os.sep + selected
        s = get_sentence_from_file(file_path, term)
        if s != "":
            break
    
    return s 

    
    
#create_index("../DATASETS/Computer_Science_D_2", "CS_dictionary.pkl")
#load_index("CS_dictionary.pkl")
#s = get_random_sentence_index("hash", "../DATASETS/Computer_Science_D_2", "CS_dictionary.pkl")


    
            