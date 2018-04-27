'''
Created on May 8, 2017

@author: alessioferrari

'''
import csv
import os

import nltk


RESULT_FILE_PATH = "../RESULTS"

FILE_HC = "HC_results.txt"
FILE_TR = "TR_results.txt"
FILE_AN = "AN_results.txt"


def get_term(block):
    tokens = nltk.word_tokenize(block, "english")
    if len(tokens) == 0:
        return 0
    else:
        return tokens[0]

def get_cosine(block):
    lines = nltk.line_tokenize(block)

    l = [l.strip('cosine similarity between vectors: ') for l in lines if l.startswith('cosine')]
    if len(l) == 0:
        return 0
    else:
        return l[0]

def save_csv(out_file_path, dictionary):
    with open(out_file_path, 'wb') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in dictionary.items():
            writer.writerow([key, value])

def convert_to_csv(source_path, source_file):
    
    l_file = open(os.path.join(source_path, source_file),"r")
    raw = l_file.read().decode('utf8').lower()
    
    word_blocks = raw.split('comparing ')
    cosine_dict = dict()
    
    for b in word_blocks:
        term = get_term(b)
        if term != 0:
            cosine = get_cosine(b) 
            cosine_dict[term] = float(cosine)
    
    save_csv(os.path.join(source_path, source_file.strip(".txt") + ".csv"), cosine_dict)
        
def __print_merged_table(in_table, out_file):
    
    table_header = ['Terms']
    for item in in_table[in_table.keys()[0]].keys():
        table_header.append(item)
     
    with open(out_file, 'wb') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(table_header) 
    
        for row_name in in_table.keys():
            new_row = [row_name]
            for k in in_table[row_name].keys():
                new_row.append(in_table[row_name][k])
            writer.writerow(new_row)
            
        
def merge_csv(source_path, out_file):
    
    tables_dict = dict()
    tables_dict_tmp = dict()
    merged_table = dict()
    
    for f in os.listdir(source_path):
        if f.endswith('.csv'):
            with open(os.path.join(source_path, f), 'rb') as csvfile:
                tables_dict_tmp[f] = csv.reader(csvfile, delimiter=',')
                row_list = list()
                for row in tables_dict_tmp[f]:
                    row_list.append(row)
                    tables_dict[f] = row_list
    
    for k in tables_dict.keys():
        for row in tables_dict[k]:
            if row[0] not in merged_table.keys():
                merged_table[row[0]] = dict()
            merged_table[row[0]][k.strip('_D2.csv')] = row[1]
    
    __print_merged_table(merged_table, out_file)
                
def convert_results_files(result_file_path):                
    for f in os.listdir(result_file_path):
        if f.endswith('.txt'):
            print "Converting " + f
            convert_to_csv(result_file_path, f)
    
    
    
if __name__ == '__main__':
    convert_results_files(RESULT_FILE_PATH)
    merge_csv(RESULT_FILE_PATH, os.path.join(RESULT_FILE_PATH,'Merged.csv'))
    print "done"
