'''
Created on Sep 20, 2018

@author: alessioferrari
'''
                      

'''
This function merges all the documents in a domain folder into a single file, 
named like the original folder.
'''  

from glob import glob
import os
from random import sample


def merge_domain_documents(domain_docs_path, out_file_path, sample_docs = False, sample_size = 1000):
    out_file = out_file_path + domain_docs_path.split(os.sep)[-1] + '.txt'

    with open(out_file, mode = 'w', encoding='utf-8') as fout_handler:
        if sample_docs == False:
            file_list = glob(domain_docs_path+"/*.txt")
        else:
            file_list = sample(glob(domain_docs_path+"/*.txt"), sample_size)
    
            
        for txtFile in file_list: 
                with open(txtFile,  mode = 'r', encoding='utf-8') as infile:
                    for line in infile:
                        fout_handler.write(line)
            
 
'''
Iteratevely calls merge_domain_documents in all the folders included in
base_path
''' 
def merge_domains(base_path, out_file_path):
    corpora = [subdirs for subdirs, _, _ in os.walk(base_path)]
    for corpus in corpora[1:]:
        merge_domain_documents(corpus, out_file_path)
        

'''
Iteratrively calls merge_domain_documents but asking to sample the files
'''
def sample_and_merge_domains(base_path, out_file_path, s_size = 1000):
    corpora = [subdirs for subdirs, _, _ in os.walk(base_path)]
    for corpus in corpora[1:]:
        merge_domain_documents(corpus, out_file_path, sample_docs = True, sample_size = s_size)

    