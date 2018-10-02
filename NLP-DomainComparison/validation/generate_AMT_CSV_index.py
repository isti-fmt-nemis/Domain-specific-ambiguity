'''
Created on Oct 1, 2018

@author: alessioferrari
'''
'''
@param words: words for which the file shall be generated
@param domains: 
@param sent_num: number of sentences for each word
@param file_name: output file name
'''



import csv
import datetime

from validation import inverted_index


def get_random_sentence_index_caller(term, path_to_files, index_pkl):
    s = inverted_index.get_random_sentence_index(term, path_to_files, index_pkl)
    return s

                
                
def generate_CSV_from_index(words, in_domains, sent_num, file_name):
    
    '''
    I have to first unpack the in_domains, which are couple of folder:index, 
    by loading the inverted indexes, and replacing the index file pointer with the 
    pointer to the inverted index object.
    '''
    
    domains = dict(in_domains)
    for domain in domains.keys():
        domains[domain] = inverted_index.load_index(domains[domain])
    
    with open(file_name, mode='w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter='\t',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL) 
        

          
        for w in words:
            print('\n' + str(datetime.datetime.now()) + ' Generating rows for ' + w + '\n')
            for i in range(sent_num):
                csv_row = list()
                csv_row.append(w)
                for d in domains.keys():
                    sent_w = get_random_sentence_index_caller(w, d, domains[d])
                    csv_row.append(sent_w)
                print(csv_row)
                csv_writer.writerow(csv_row)            
                