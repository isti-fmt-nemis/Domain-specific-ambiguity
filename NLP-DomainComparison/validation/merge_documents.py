'''
Created on Sep 20, 2018

@author: alessioferrari
'''
                      

from glob import glob
import os

'''
This function merges all the documents in a domain folder into a single file, 
named like the original folder.
'''  

def merge_domain_documents(domain_docs_path, out_file_path):
    out_file = out_file_path + domain_docs_path.split(os.sep)[-1] + '.txt'

    with open(out_file, mode = 'w', encoding='utf-8') as fout_handler:
        for txtFile in glob(domain_docs_path+"/*.txt"): 
                with open(txtFile,  mode = 'r', encoding='utf-8') as infile:
                    for line in infile:
                        fout_handler.write(line)
 
'''
Iteratevely calls merge_domain_documents in all the folders included in
base_path
''' 
def merge_domains(base_path, out_file_path):
    corpora = [subdirs for subdirs, dirs, files in os.walk(base_path)]
    for corpus in corpora[1:]:
        merge_domain_documents(corpus, out_file_path)
        
