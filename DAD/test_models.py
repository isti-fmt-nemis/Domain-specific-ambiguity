'''
Created on Apr 27, 2018

@author: alessioferrari
'''
from __future__ import division

from os.path import os

from gensim.models.word2vec import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity

from generate_domain_models import MODEL_PATH    

from gensim.models import KeyedVectors
import nltk

MODEL_LIST = ["Sports_D_2.bin", "Computer_Science_D_2.bin", "Medicine_D_2.bin", "Electronic_Engineering_D_2.bin", "Mechanical_Engineering_D_2.bin", "Literature_D_2.bin"]

req_1 = "The system shall support user authentication"
req_2 = "The student shall enter login and password"

if __name__ == '__main__':
    
    mdl = Word2Vec.load(os.path.join(MODEL_PATH, "Computer_Science_D_2.bin"))
    
    tok_req_1 = nltk.tokenize.word_tokenize(req_1)
    vect_req_1 = [mdl[t] for t in tok_req_1 if t in mdl.wv.vocab]
    v_req_1 = [sum(e)/len(e) for e in zip(*vect_req_1)]
    
    tok_req_2 = nltk.tokenize.word_tokenize(req_2)
    vect_req_2 = [mdl[t] for t in tok_req_2 if t in mdl.wv.vocab]
    v_req_2 = [sum(e)/len(e) for e in zip(*vect_req_2)]
        
    print cosine_similarity(v_req_1, v_req_2)
    
