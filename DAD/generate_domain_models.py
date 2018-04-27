'''
Created on Apr 27, 2018

@author: alessioferrari
'''
import os.path

from nltk.stem.wordnet import WordNetLemmatizer

from vector_comparison import vectorization


CORPORA_DIR = "./DATASETS"
MODEL_PATH = "./MODELS"
SIZE = 50
WINDOW = 10
MIN_COUNT = 10
ITER = 5

LANGUAGE = 'english'
LEMMATIZER = WordNetLemmatizer()

if __name__ == '__main__':
    corpora = [subdirs for subdirs, dirs, files in os.walk(CORPORA_DIR)]
    for corpus in corpora[1:]:
        print "training model on" + corpus
        model = vectorization.train_model_on_dir(corpus, LANGUAGE, LEMMATIZER, SIZE, WINDOW, MIN_COUNT, ITER)
        print "model trained, saving it"
        MODEL_NAME = os.path.basename(os.path.normpath(corpus)) + ".bin"
        model.save(os.path.join(MODEL_PATH, MODEL_NAME))
        print "done\n\n"