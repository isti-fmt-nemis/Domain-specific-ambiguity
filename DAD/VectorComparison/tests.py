from glob import glob
import os

from gensim.models import Word2Vec
import nltk
from nltk.stem.snowball import SnowballStemmer

import comparison
import vectorization


#from sklearn.metrics.pairwise import cosine_similarityfrom
###### experiment parameters ######
language = 'english'
stemmer = SnowballStemmer(language)

############## models creation ####################################

def create_model(data_path, model_path):# '../vectorAnalisysWorkspace/CS_corpus_5'
    print '...building the vector model from '+ data_path
    model = vectorization.train_model_on_dir(data_path, language, stemmer)
    model.save(model_path)

############## saved models #######################################
#animalsNOstop = Word2Vec.load('../vectorAnalisysWorkspace/saved_model_ANIMALS5_NO_stopwords')
#animalsYESstop = Word2Vec.load('../vectorAnalisysWorkspace/saved_model_ANIMALS5_stopwords')
#run1 = Word2Vec.load('../vectorAnalisysWorkspace/ANIMALS_RUN1')#animals without stopwords
#run2 = Word2Vec.load('../vectorAnalisysWorkspace/ANIMALS_RUN2')#animals without stopwords
#run3 = Word2Vec.load('../vectorAnalisysWorkspace/ANIMALS_RUN3')#animals without stopwords
#run4 = Word2Vec.load('../vectorAnalisysWorkspace/ANIMALS_RUN4')#animals without stopwords
#run5 = Word2Vec.load('../vectorAnalisysWorkspace/ANIMALS_RUN5')#animals without stopwords
#run6 = Word2Vec.load('../vectorAnalisysWorkspace/ANIMALS_RUN6')#animals without stopwords
#run7 = Word2Vec.load('../vectorAnalisysWorkspace/ANIMALS_RUN7')#animals without stopwords
#run8 = Word2Vec.load('../vectorAnalisysWorkspace/ANIMALS_RUN8')#animals without stopwords

############# analysis methods ##########################

def test1(word, title1, title2, model1, model2):#compare the same word on two models. title are string describing the models
    stem= stemmer.stem(word)

    print '========[ '+ str(word)+ ' ]========'
    print 'Model 1: ' + title1
    print 'Model 2: ' + title2

    print '--------------'

    comparison.frequency_comparison(model1,model2,stem)

    print '--------------'
    comparison.vectors_comparison(model1,model2,stem)

    print '--------------'
    comparison.neighbors_comparison(model1,model2,stem)

def test3(title1, title2, model1, model2,threshold):#takes the n=threshold most frequent words from the two models and run the comparison
    for word in comparison.frequent_common_words(model1, model2,threshold):
        test1(word, title1, title2, model1, model2)

def big_training(stems, model_path, runs, size, window, min_count,iter):

    if not os.path.isdir(model_path):
        os.makedirs(model_path)

    for n in range(0,runs):
        print("Run "+ str(n) + " of " + str(runs))
        model = vectorization.train_model_on_stems(stems, size, window, min_count,iter)
        model.save(model_path+'/RUN_{}'.format(n))



############# CREATE DIFFERENT TRAININGS ##########################
# print("Extracting and preprocessing corpus")
# stems = vectorization.extract_stems_from_dir('../vectorAnalisysWorkspace/ANIMALS_corpus_5', language, stemmer)
# 
# runs = 3
# size = 50
# window = 10
# min_count = 1
# iter = 5
# path = '../vectorAnalisysWorkspace/modelli/SZ-{}_WIN-{}_MINCNT-{}_ITER-{}'.format(size, window, min_count, iter)
# print(path)
# big_training(stems, path, runs, size, window, min_count, iter)

############# RUN! ##########################