'''
Created on Oct 1, 2018

@author: alessioferrari
'''
from validation.inverted_index import create_index


def create_indexes():
    create_index("DATASETS/Computer_Science_D_2", "CS_dictionary.pkl")
    create_index("DATASETS/Electronic_Engineering_D_2", "EEN_dictionary.pkl")
    create_index("DATASETS/Mechanical_Engineering_D_2", "MEN_dictionary.pkl")
    create_index("DATASETS/Medicine_D_2", "MED_dictionary.pkl")
    create_index("DATASETS/Sports_D_2", "SPO_dictionary.pkl")
    


