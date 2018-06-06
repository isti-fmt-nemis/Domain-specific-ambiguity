from glob import glob
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from gensim.models import Word2Vec

STOP_PATTERNS = ["== references ==", "== external links ==", "== see also =="]

LONG_SW = ["a", "able", "about", "above", "abst", "accordance", "according", "accordingly", "across", "act", "actually", "added", "adj", "affected", "affecting", "affects", "after", "afterwards", "again", "against", "ah", "all", "almost", "alone", "along", "already", "also", "although", "always", "am", "among", "amongst", "an", "and", "announce", "another", "any", "anybody", "anyhow", "anymore", "anyone", "anything", "anyway", "anyways", "anywhere", "apparently", "approximately", "are", "aren", "arent", "arise", "around", "as", "aside", "ask", "asking", "at", "auth", "available", "away", "awfully", "b", "back", "be", "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand", "begin", "beginning", "beginnings", "begins", "behind", "being", "believe", "below", "beside", "besides", "between", "beyond", "biol", "both", "brief", "briefly", "but", "by", "c", "ca", "came", "can", "cannot", "can't", "cause", "causes", "certain", "certainly", "co", "com", "come", "comes", "contain", "containing", "contains", "could", "couldnt", "d", "date", "did", "didn't", "different", "do", "does", "doesn't", "doing", "done", "don't", "down", "downwards", "due", "during", "e", "each", "ed", "edu", "effect", "eg", "eight", "eighty", "either", "else", "elsewhere", "end", "ending", "enough", "especially", "et", "et-al", "etc", "even", "ever", "every", "everybody", "everyone", "everything", "everywhere", "ex", "except", "f", "far", "few", "ff", "fifth", "first", "five", "fix", "followed", "following", "follows", "for", "former", "formerly", "forth", "found", "four", "from", "further", "furthermore", "g", "gave", "get", "gets", "getting", "give", "given", "gives", "giving", "go", "goes", "gone", "got", "gotten", "h", "had", "happens", "hardly", "has", "hasn't", "have", "haven't", "having", "he", "hed", "hence", "her", "here", "hereafter", "hereby", "herein", "heres", "hereupon", "hers", "herself", "hes", "hi", "hid", "him", "himself", "his", "hither", "home", "how", "howbeit", "however", "hundred", "i", "id", "ie", "if", "i'll", "im", "immediate", "immediately", "importance", "important", "in", "inc", "indeed", "index", "information", "instead", "into", "invention", "inward", "is", "isn't", "it", "itd", "it'll", "its", "itself", "i've", "j", "just", "k", "keeptkeeps", "kept", "kg", "km", "know", "known", "knows", "l", "largely", "last", "lately", "later", "latter", "latterly", "least", "less", "lest", "let", "lets", "like", "liked", "likely", "line", "little", "'ll", "look", "looking", "looks", "ltd", "m", "made", "mainly", "make", "makes", "many", "may", "maybe", "me", "mean", "means", "meantime", "meanwhile", "merely", "mg", "might", "million", "miss", "ml", "more", "moreover", "most", "mostly", "mr", "mrs", "much", "mug", "must", "my", "myself", "n", "na", "name", "namely", "nay", "nd", "near", "nearly", "necessarily", "necessary", "need", "needs", "neither", "never", "nevertheless", "new", "next", "nine", "ninety", "no", "nobody", "non", "none", "nonetheless", "noone", "nor", "normally", "nos", "not", "noted", "nothing", "now", "nowhere", "o", "obtain", "obtained", "obviously", "of", "off", "often", "oh", "ok", "okay", "old", "omitted", "on", "once", "one", "ones", "only", "onto", "or", "ord", "other", "others", "otherwise", "ought", "our", "ours", "ourselves", "out", "outside", "over", "overall", "owing", "own", "p", "page", "pages", "part", "particular", "particularly", "past", "per", "perhaps", "placed", "please", "plus", "poorly", "possible", "possibly", "potentially", "pp", "predominantly", "present", "previously", "primarily", "probably", "promptly", "proud", "provides", "put", "q", "que", "quickly", "quite", "qv", "r", "ran", "rather", "rd", "re", "readily", "really", "recent", "recently", "ref", "refs", "regarding", "regardless", "regards", "related", "relatively", "research", "respectively", "resulted", "resulting", "results", "right", "run", "s", "said", "same", "saw", "say", "saying", "says", "sec", "section", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen", "self", "selves", "sent", "seven", "several", "shall", "she", "shed", "she'll", "shes", "should", "shouldn't", "show", "showed", "shown", "showns", "shows", "significant", "significantly", "similar", "similarly", "since", "six", "slightly", "so", "some", "somebody", "somehow", "someone", "somethan", "something", "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "specifically", "specified", "specify", "specifying", "still", "stop", "strongly", "sub", "substantially", "successfully", "such", "sufficiently", "suggest", "sup", "surett", "take", "taken", "taking", "tell", "tends", "th", "than", "thank", "thanks", "thanx", "that", "that'll", "thats", "that've", "the", "their", "theirs", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "thered", "therefore", "therein", "there'll", "thereof", "therere", "theres", "thereto", "thereupon", "there've", "these", "they", "theyd", "they'll", "theyre", "they've", "think", "this", "those", "thou", "though", "thoughh", "thousand", "throug", "through", "throughout", "thru", "thus", "til", "tip", "to", "together", "too", "took", "toward", "towards", "tried", "tries", "truly", "try", "trying", "ts", "twice", "two", "u", "un", "under", "unfortunately", "unless", "unlike", "unlikely", "until", "unto", "up", "upon", "ups", "us", "use", "used", "useful", "usefully", "usefulness", "uses", "using", "usually", "v", "value", "various", "'ve", "very", "via", "viz", "vol", "vols", "vs", "w", "want", "wants", "was", "wasnt", "way", "we", "wed", "welcome", "we'll", "went", "were", "werent", "we've", "what", "whatever", "what'll", "whats", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "wheres", "whereupon", "wherever", "whether", "which", "while", "whim", "whither", "who", "whod", "whoever", "whole", "who'll", "whom", "whomever", "whos", "whose", "why", "widely", "willing", "wish", "with", "within", "without", "wont", "words", "world", "would", "wouldnt", "www", "x", "y", "yes", "yet", "you", "youd", "you'll", "your", "youre", "yours", "yourself", "yourselves", "you've", "z", "zero"]

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

def OLD_train_model(corpus, language, lemmatizer, size, window, min_count,iter):
    stop_words = stopwords.words(language)

    sentences = [sent_tokenize(text, language) for text in corpus]
    sentences = [val for sublist in sentences for val in sublist]
    sentences  =  map(word_tokenize, sentences)
    token_sentences = [[token for token in sentence if (token.lower() not in stop_words and (token.isalnum() or token.startswith('_')))] for sentence  in sentences];#considering also non alphanumeric chars
    #ORIGINAL token_sentences = [[token for token in sentence if (token.lower() not in stop_words and token.isalnum())] for sentence  in sentences];
    #token_sentences = [[token for token in sentence if token.isalnum()] for sentence in sentences];#CON STOPWORDS
    lemmas = [[lemmatizer.lemmatize(token) for token in tokens] for tokens in token_sentences]

    model = Word2Vec(lemmas, size=size, window=window, min_count=min_count, iter=iter)
    #size = size of the NN layers, which correspond to the degrees of freedom the training algorithm has. Bigger size values require more training data, but can lead to better (more accurate) models. Reasonable values are in the tens to hundreds.
    #A reasonable value for min_count is between 0-100, depending on the size of your dataset.

    return model

def train_model(corpus, language, lemmatizer, size, window, min_count, iter):
    
    stop_words = stopwords.words(language)

    corpus_clean = list()
    for doc_elem in corpus:
        stop_reading_positions = [doc_elem.find(stop_pattern) for stop_pattern in STOP_PATTERNS]
        stop_reading_positions_clean = [p for p in stop_reading_positions if not p == -1]
        if len(stop_reading_positions_clean) != 0:
            corpus_clean.append(doc_elem[:min(stop_reading_positions_clean)])
        else:
            corpus_clean.append(doc_elem)
    
    sentences = [sent_tokenize(text, language) for text in corpus_clean]
    sentences = [val for sublist in sentences for val in sublist]
    sentences  =  map(word_tokenize, sentences)
    token_sentences = [[token for token in sentence if (token.lower() not in stop_words and token.lower() not in LONG_SW and (token.isalnum() or token.startswith('_')))] for sentence in sentences]

    lemmas = [[lemmatizer.lemmatize(token) for token in tokens] for tokens in token_sentences]

    model = Word2Vec(lemmas, size=size, window=window, min_count=min_count, iter=iter)
    
    return model
    
def train_model_on_dir(dir, language, lemmatizer, size, window, min_count, iter):
    return train_model([open(txtFile).read().decode("utf8").lower() for txtFile in glob(dir+"/*.txt")], language, lemmatizer, size, window, min_count, iter)