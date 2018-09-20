'''
Created on Sep 19, 2018

@author: alessioferrari
This module generate tests to be used by Amazon Mechanical Turk.

- Given a list of words, w_0...w_N, and a list of domains d_1...d_D to consider, generates a CSV file 
- Each line of the CSV file is associated to a word  
- Each line of the CSV file has the following form [word, s_0, ..., s_D], 
where D is the number of domains to consider 
- For each word, the system searches the files in the DATASET folder associated to the domains,
and randomly extract one sentence from each domain folder. The extracted sentence in placed in 
the position associated to the domain in the CSV file row.
- For each word, we have S lines, where S is selected by the user. Each line has different 
combinations of sentences from the same domain sets.

@param words: list of words to consider
@param domains: list of domain folders to consider
@param sent_num: number indicating the number S of lines desired for each word
'''
'''
Given a document and a word w, returns a random sentence containing 
the word w in the documents 
'''
'''
Given a document, this function returns a random sentence 
including the word w from the document.
'''

import csv
import datetime
from random import sample
import re

from nltk.tokenize import sent_tokenize, word_tokenize


def get_random_sentence(doc, w, sent_max_len = 200, sent_min_len = 50,window = 500):
    with open(doc, mode="r", encoding="utf-8") as f:
        raw = f.read().lower()
        pos_w = [m.start() for m in re.finditer(w.lower(), raw)]
        segments = [raw[pos - window:pos + window] for pos in pos_w]
        sentences = [sent for segment in segments for sent in sent_tokenize(segment.lower())[1:-2]]
        sentences_w = [sent for sent in sentences if w.lower() in sent]
        sentences_w_pure = [sent for sent in sentences_w if u'\n' not in sent and len(sent) < sent_max_len and len(sent) > sent_min_len]
         
        selected_good = False
        while selected_good == False:
            selected = sample(sentences_w_pure, 1)
            if w.lower() in word_tokenize(selected[0]):
                selected_good = True
 
    return selected

def get_random_sentence_slow(doc, w, sent_max_len = 120):
    
    with open(doc, mode="r", encoding="utf-8") as f:
        raw = f.read()
        sentences = sent_tokenize(raw.lower())
        sentences_w = [sent for sent in sentences if w.lower() in sent or (w.lower() + 's') in sent]
        sentences_w_pure = [sent for sent in sentences_w if u'\n' not in sent and len(sent) < sent_max_len]
        
        selected_good = False
        while selected_good == False:
            selected = sample(sentences_w_pure, 1)
            if w.lower() in word_tokenize(selected[0]):
                selected_good = True

    return selected

'''
@param words: words for which the file shall be generated
@param domains: domain file names, including the path
@param sent_num: number of sentences for each word
@param file_name: output file name
'''
def generate_CSV(words, domains, sent_num, file_name):
    
    with open(file_name, mode='w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter='\t',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)   
          
        for w in words:
            print('\n' + str(datetime.datetime.now()) + ' Generating rows for ' + w + '\n')
            for i in range(sent_num):
                csv_row = list()
                csv_row.append(w)
                for d in domains:
                    sent_w = get_random_sentence(d, w)
                    csv_row.append(sent_w)
                print(csv_row)
                csv_writer.writerow(csv_row)