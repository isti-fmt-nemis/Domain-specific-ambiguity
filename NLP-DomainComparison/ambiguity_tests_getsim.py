'''
Created on Jun 12, 2018

@author: alessioferrari
'''

from __future__ import division

from os.path import os
from pprint import pprint

import domain_analysis.ambiguity as ambiguity
from gensim.models.word2vec import Word2Vec

MODEL_PATH = "./MODELS"

TERM = 'term'


if __name__ == '__main__':
    models = dict()
    models['cs'] = Word2Vec.load(os.path.join(MODEL_PATH, "Computer_Science_D_2.bin"))
    models['med'] = Word2Vec.load(os.path.join(MODEL_PATH, "Medicine_D_2.bin"))
    models['sport'] = Word2Vec.load(os.path.join(MODEL_PATH, "Sports_D_2.bin"))
    models['ele'] = Word2Vec.load(os.path.join(MODEL_PATH, "Electronic_Engineering_D_2.bin"))
    models['mec'] = Word2Vec.load(os.path.join(MODEL_PATH, "Mechanical_Engineering_D_2.bin"))
    models['lit'] = Word2Vec.load(os.path.join(MODEL_PATH, "Literature_D_2.bin"))
    
    for model in models.keys():
        print(model)
        pprint(models[model].wv.most_similar(TERM, topn=20))
