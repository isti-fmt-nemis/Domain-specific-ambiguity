from glob import glob
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from gensim.models import Word2Vec

def extract_lemmas_from_dir(dir, language, lemmatizer):
    corpus = [open(txtFile).read().decode("utf8") for txtFile in glob(dir+"/*.txt")]
    stop_words = stopwords.words(language)
    sentences = [sent_tokenize(text, language) for text in corpus]
    sentences = [val for sublist in sentences for val in sublist]
    sentences = map(word_tokenize, sentences)
    token_sentences = [[token for token in sentence if (token.lower() not in stop_words and token.isalnum())] for
                       sentence in sentences];
    # token_sentences = [[token for token in sentence if token.isalnum()] for sentence in sentences];#CON STOPWORDS
    return [[lemmatizer.lemmatize(token) for token in tokens] for tokens in token_sentences]

def train_model_on_lemmas(lemmas, size, window, min_count,iter):
    return Word2Vec(lemmas, size=size, window=window, min_count=min_count, iter=iter)

def train_model(corpus, language, lemmatizer, size, window, min_count,iter):
    stop_words = stopwords.words(language)

    sentences = [sent_tokenize(text, language) for text in corpus]
    sentences = [val for sublist in sentences for val in sublist]
    sentences  =  map(word_tokenize, sentences)
    token_sentences = [[token for token in sentence if (token.lower() not in stop_words and (token.isalnum() or token.startswith('_')))] for sentence  in sentences];#considering also non alphanumeric chars
    #ORIGINAL token_sentences = [[token for token in sentence if (token.lower() not in stop_words and token.isalnum())] for sentence  in sentences];
    #token_sentences = [[token for token in sentence if token.isalnum()] for sentence in sentences];#CON STOPWORDS
    lemmas = [[lemmatizer.lemmatize(token) for token in tokens] for tokens in token_sentences]
    #print stems

    model = Word2Vec(lemmas, size=size, window=window, min_count=min_count, iter=iter)
    #size = size of the NN layers, which correspond to the degrees of freedom the training algorithm has. Bigger size values require more training data, but can lead to better (more accurate) models. Reasonable values are in the tens to hundreds.
    #A reasonable value for min_count is between 0-100, depending on the size of your dataset.

    return model

def train_model_on_dir(dir, language, lemmatizer, size, window, min_count, iter):
    return train_model([open(txtFile).read().decode("utf8").lower() for txtFile in glob(dir+"/*.txt")], language, lemmatizer, size, window, min_count, iter)