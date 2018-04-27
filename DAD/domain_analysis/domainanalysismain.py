'''
Created on May 4, 2017

@author: alessioferrari
'''
import io
import os

import nltk
from nltk.corpus import stopwords
from nltk.data import load
from nltk.probability import FreqDist
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize.regexp import wordpunct_tokenize


INPUT_PATH_TR = "../../DATASETS/Trains"
INPUT_PATH_CS = "../DATASETS/Computer science_D_2"
INPUT_PATH_HC = "../../DATASETS/Health_care"
OUTPUT_PATH = "../DATASETS"

NAMES_FILE_TR = "names_file_trains.txt"
NAMES_FILE_CS = "names_file_computer_science_freq.txt"
NAMES_FILE_HC = "names_file_healthcare.txt"
NAMES_FILE_CS_TR = "names_file_cs_tr.txt"
NAMES_FILE_CS_HC = "names_file_cs_hc.txt"

"""this hack below is to deal with undesired parentheses identified as nouns by nltk pos tagger"""
_POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
tagger = load(_POS_TAGGER)
regexp_tagger = nltk.tag.RegexpTagger([(r'\(|\)', '--')], backoff = tagger) 

def is_name(term):
    
    
    pos_term = regexp_tagger.tag([term])
    pos = pos_term[0][1]
   
    if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
        return True
    else:
        return False

def remove_chars(token):
    char_list = ["(", "u'", ")", ",", "'"]
    clean_token = str(token)
        
    for ch in char_list:
        clean_token = clean_token.replace(ch, "")
    
    return clean_token
            
def get_top_K_names(in_tokens, k):
    '''
    This function output the top k the names in in_tokens,
    with their frequencies in a sorted list
    '''
    
    top_names = dict()
    text = nltk.Text(in_tokens)
    fdist = FreqDist(text)
    most_common_terms = fdist.most_common()
    index = 0
    name_counter = 0
    
    while name_counter <= k:
        token = most_common_terms[index][0]
        clean_token = remove_chars(token)
        if is_name(clean_token):
            top_names[clean_token] = fdist[token]
            name_counter = name_counter + 1
        index = index + 1
    
    return sorted(top_names.iteritems(), key=lambda x:x[1], reverse=True) 


def print_freq_dist(in_tokens):
    "plot the frequency distributions for tokens in in_tokens"
    
    
    text = nltk.Text(in_tokens)
    fdist = FreqDist(text)
    fdist.plot(100, cumulative=False)

def get_text(in_file): 
    "returns the text included in in_file, all in lowercase"    
    l_file = open(in_file,"r")
    raw = l_file.read().decode('utf8').lower()
    text = '\n'.join(nltk.line_tokenize(raw))
    
    return text

def get_all_text(in_folder):
    "returns all the text included in the files belonging to in_folder, ignoring hidden files"
    
    text = ''.join([get_text(os.path.join(in_folder, f)) for f in os.listdir(in_folder) if not f.startswith('.')])
    return text
            
def get_clean_text_tokens(in_text):
    "returns a list of lemmatised tokens, after cleaning in_text from stopwords, numbers, and one-letter words"
    
    stop_words = set(stopwords.words("english")) 
    tokens = [t for t in wordpunct_tokenize(in_text)]
    tokens = filter(lambda x: x not in stop_words, tokens)
    tokens = filter(lambda x: x.isalpha(), tokens)
    tokens = filter(lambda x: len(x) > 1, tokens) 
      
    wordnet_lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [wordnet_lemmatizer.lemmatize(t) for t in tokens]
    
    return lemmatized_tokens

def get_names(in_text):
    "returns a version of in_text in which only nouns (NN, NNP, NNS, NNPS) are included"
    
    tokens = nltk.word_tokenize(in_text)
    pos_text = regexp_tagger.tag(tokens) 
    names = [n.encode('utf-8') for n,pos in pos_text if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS')]
    names_text = ' '.join(names).strip()
    
    return names_text
    
def plot_lemma_frequencies(in_path):
    "plot the frequency distributions for the lemmas included in the files in in_path"
    
    lemmatised_tokens = get_clean_text_tokens(get_all_text(in_path))
    print_freq_dist(lemmatised_tokens)

def save_text(in_text, in_dest_file_path):
    with io.open(in_dest_file_path,'w',encoding='utf-8') as f:
        f.write(in_text)
        f.close()

def save_top_k_names(input_path, output_path, names_file, k, freq=False):    
    lemmatised_tokens = get_clean_text_tokens(get_all_text(input_path))
    top_k_names = get_top_K_names(lemmatised_tokens, k)
    if freq == False:
        names_rank = [item[0] for item in top_k_names]
    else:
        names_rank = [''.join(str(item)) for item in top_k_names]
    names_to_print_text = ('\n'.join(names_rank)).strip()
    save_text(unicode(names_to_print_text, "utf-8"), os.path.join(output_path, names_file))
    
def save_top_h_common_names(input_path_d1, input_path_d2, output_path, names_file, k):
    "rank the terms based on their relative frequency in the domains. Each term that is common \
    among domains is assigned a rank by summing its position in the two lists of most frequent terms"
    
    lemmatised_tokens_d1 = get_clean_text_tokens(get_all_text(input_path_d1))
    top_k_names_d1 = get_top_K_names(lemmatised_tokens_d1, k)
    names_d1 = [item[0] for item in top_k_names_d1]    
    rank_d1 = [item[1] for item in top_k_names_d1]
    
    lemmatised_tokens_d2 = get_clean_text_tokens(get_all_text(input_path_d2))
    top_k_names_d2 = get_top_K_names(lemmatised_tokens_d2, k)
    names_d2 = [item[0] for item in top_k_names_d2]
    rank_d2 = [item[1] for item in top_k_names_d2]
    
    names_rank = dict()
    
    for n in names_d1:
        if n in names_d2:
            names_rank[n] = rank_d1[names_d1.index(n)] + rank_d2[names_d2.index(n)]   
            
    common_frequent_names = sorted(names_rank.iteritems(), key=lambda x:x[1], reverse=True)
     
    names_to_print = [item[0] for item in common_frequent_names]
    names_to_print_text = ('\n'.join(names_to_print)).strip()
    save_text(unicode(names_to_print_text, "utf-8"), os.path.join(output_path, names_file))
    
if __name__ == '__main__':
#    save_top_h_common_names(INPUT_PATH_CS, INPUT_PATH_TR, OUTPUT_PATH, NAMES_FILE_CS_TR, k = 100)
#    save_top_h_common_names(INPUT_PATH_CS, INPUT_PATH_HC, OUTPUT_PATH, NAMES_FILE_CS_HC, k = 100)
    
    
#     save_top_k_names(INPUT_PATH_TR, OUTPUT_PATH, NAMES_FILE_TR, 100)
#     save_top_k_names(INPUT_PATH_HC, OUTPUT_PATH, NAMES_FILE_HC, 100)    
    save_top_k_names(INPUT_PATH_CS, OUTPUT_PATH, NAMES_FILE_CS, 100, freq=True)
    
    #text = get_all_text(INPUT_PATH_CS)
    #names_text = get_names(text)
    #save_text(unicode(names_text, "utf-8"), os.path.join(OUTPUT_PATH, NAMES_FILE_CS))
    
    #text = get_all_text(INPUT_PATH_HC)
    #names_text = get_names(text)
    #save_text(unicode(names_text, "utf-8"), os.path.join(OUTPUT_PATH, NAMES_FILE_HC))
    
#     names_text = get_text(os.path.join(OUTPUT_PATH, NAMES_FILE))
#     lemmatised_tokens = get_clean_text_tokens(names_text)
#     print_freq_dist(lemmatised_tokens)
    
    