'''
Created on May 4, 2017

@author: alessioferrari

'''
import io
import os
import sys

import nltk
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize.regexp import wordpunct_tokenize

from domainanalysismain import save_text, get_all_text, \
    INPUT_PATH_TR, INPUT_PATH_HC, OUTPUT_PATH


# REPLACE_TERM_LIST_CS_TR = [u'system', u'time', u'game', u'use', u'version', u'number', u'company', u'service', u'set', u'reference']
# REPLACE_TERM_LIST_CS_HC = [u'system', u'time', u'year', u'state', u'reference', u'university',u'use',u'game',u'company',u'number']
# REPLACE_TERM_LIST_CS = [u'system',u'computer',u'data',u'time',u'displaystyle',u'game',u'user',u'software',u'version',u'number',u'company',u'model',u'application',u'program']
CS_COMMON_TERM_PATH = "../DATASETS/names_file_computer_science.txt"

MODIFIED_FILE_TR = 'ALL_FREQ_output_modified_file_TR.txt'
MODIFIED_FILE_HC = 'ALL_FREQ_output_modified_file_HC.txt'
MODIFIED_FILE_AN = 'ALL_FREQ_output_modified_file_AN.txt'

INPUT_PATH_TEST = "../../DATASETS/Test"
INPUT_PATH_AN = "../../DATASETS/Animals"

LANGUAGE = 'english'
STEMMER = SnowballStemmer(LANGUAGE)
LEMMATIZER = WordNetLemmatizer()

def lemma_replace(in_lemma_list, term, lemmatizer):
    
    o_term = term
    o_lemma = lemmatizer.lemmatize(term)
    if o_lemma in in_lemma_list:
        o_term = '_' + o_lemma 
    
    return o_term

def inject_term_list(in_lemma_list, in_text, lemmatizer):
    "This function replace the term with its lemma, prefixed by an underscore, if the term is included in in_lemma_list"
    return ' '.join([lemma_replace(in_lemma_list, t, lemmatizer).encode("utf-8") for t in wordpunct_tokenize(in_text)])
 
def modify_and_save(in_path, out_path, out_file, t_list, lemmatizer):
    original_text = get_all_text(in_path)
    lemma_list = [lemmatizer.lemmatize(t) for t in t_list]
    modified_text = inject_term_list(lemma_list, original_text, lemmatizer)
    save_text(unicode(modified_text, "utf-8"), os.path.join(out_path, out_file))
    
def modify_and_save_single_terms(in_path, out_path, t_list, lemmatizer, out_file_prefix):
    original_text = get_all_text(in_path)
    lemma_list = [lemmatizer.lemmatize(t) for t in t_list]
    for s in lemma_list:
        print("Substituting the term " + s)
        modified_text = inject_term_list([s], original_text, lemmatizer)
        save_text(unicode(modified_text, "utf-8"), os.path.join(out_path, out_file_prefix + "_" + s + ".txt"))

def load_common_terms(in_file_path):
    l_file = open(in_file_path,"r")
    raw = l_file.read().decode("utf-8").lower()
    tokens = nltk.word_tokenize(raw)
    
    return tokens

def main():
    in_folder = sys.argv[1:][0]
    input_path = os.path.join(OUTPUT_PATH, sys.argv[1:][0])
    modified_file_name = in_folder + "_injected.txt"
    replace_term_list_cs = load_common_terms(CS_COMMON_TERM_PATH)
    modify_and_save(input_path, OUTPUT_PATH, modified_file_name, replace_term_list_cs, LEMMATIZER) 

if __name__ == '__main__':
    """
    Use it by calling it as: python modifydomainfiles.py "input_folder_name"
    """
    main()
    
    
#    modify_and_save_single_terms(INPUT_PATH_TR, OUTPUT_PATH, REPLACE_TERM_LIST_CS, STEMMER, "CS_TR")
#    modify_and_save_single_terms(INPUT_PATH_HC, OUTPUT_PATH, REPLACE_TERM_LIST_CS, STEMMER, "CS_HC")
#    modify_and_save(INPUT_PATH_HC, OUTPUT_PATH, MODIFIED_FILE_HC, replace_term_list_cs, STEMMER)
#    modify_and_save(INPUT_PATH_TR, OUTPUT_PATH, MODIFIED_FILE_TR, replace_term_list_cs, STEMMER)
#     modify_and_save(INPUT_PATH_TR, OUTPUT_PATH, MODIFIED_FILE_TR, REPLACE_TERM_LIST_CS_TR, STEMMER)
#     modify_and_save(INPUT_PATH_HC, OUTPUT_PATH, MODIFIED_FILE_HC, REPLACE_TERM_LIST_CS_HC, STEMMER)
#    modify_and_save_single_terms(INPUT_PATH_HC, OUTPUT_PATH, REPLACE_TERM_LIST_CS_HC, STEMMER, "HC")
    pass