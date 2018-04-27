'''
Created on May 6, 2017

@author: alessioferrari
'''
import os

from gensim.matutils import unitvec
from gensim.models.word2vec import Word2Vec
from nltk.stem.wordnet import WordNetLemmatizer
from numpy import dot

from modifydomainfiles import load_common_terms    
from tests import language
import vectorization


#REPLACE_TERM_LIST_CS = [u'system',u'computer',u'data',u'time',u'displaystyle',u'game',u'user',u'software',u'version',u'number',u'company',u'model',u'application',u'program']
CS_COMMON_TERM_PATH = "../DATASETS/names_file_computer_science.txt"
CORPUS_DIR = "../DATASETS/Computer science_D_2"
MODEL_PATH = "../MODELS"
MODEL_NAME = "model.bin"
SIZE = 50
WINDOW = 10
MIN_COUNT = 10
ITER = 5

BUILD_M0DEL = True

LEMMATIZER = WordNetLemmatizer()

def build_model_on_lemmas():
    #1. extract stems
    lemmas = vectorization.extract_lemmas_from_dir(CORPUS_DIR, language, LEMMATIZER)
    print "lemmas extracted, training model"
    #2. train model on lemmas
    model = vectorization.train_model_on_lemmas(lemmas, SIZE, WINDOW, MIN_COUNT, ITER)
    print "model trained, saving it"
    #3. save model
    model.save(os.path.join(MODEL_PATH, MODEL_NAME))
    print "done"

def build_model_on_dir():

    print "training model"
    model = vectorization.train_model_on_dir(CORPUS_DIR, language, LEMMATIZER, SIZE, WINDOW, MIN_COUNT, ITER)
    print "model trained, saving it"
    model.save(os.path.join(MODEL_PATH, MODEL_NAME))
    print "done"

def compare_lemmas(lemma1, lemma2, mdl):
    
    try:
        v1 = mdl[lemma1]
        v2 = mdl[lemma2]
        cosim = dot(unitvec(v1),unitvec(v2))
        print 'Cosine similarity between vectors: '+str(cosim)
    
        n1= mdl.most_similar(lemma1)
        n2 = mdl.most_similar(lemma2)
        intersection = set([w for w, f in n1]) & set([w for w, f in n2])
        perc =  len(intersection)/max(len(n1),len(n2))
        print 'Percentage of overlapping: ' + str(perc)
        print 'Neighbors : '+str(intersection)
        print n1
        print n2
        print "\n"
    
    except KeyError:
        print "term " + lemma2 + " or " + lemma1 + " not in vocabulary"
        pass

if __name__ == '__main__':
    
    if BUILD_M0DEL:
        build_model_on_dir()
    
    replace_term_list_cs = load_common_terms(CS_COMMON_TERM_PATH)
    lemma1_list = [unicode(LEMMATIZER.lemmatize(t)) for t in replace_term_list_cs]
    lemma2_list = [unicode(('_' + t)) for t in lemma1_list]
    mdl = Word2Vec.load(os.path.join(MODEL_PATH, MODEL_NAME))
    print "model loaded"
    
    for i, elem in enumerate(lemma1_list):
        print "comparing " + lemma1_list[i] + " and " + lemma2_list[i]
        compare_lemmas(lemma1_list[i], lemma2_list[i] , mdl)
   
    
    pass