from __future__ import division

from gensim.matutils import unitvec
from numpy.core.numeric import dot


def neighbors_intersection(list1, list2):
    intersection =[]
    for s in list1 :
        for v in list2:
            if s[0]==v[0]:
                intersection.append(s[0])
    return intersection

def neighbors_comparison(model1,model2,stem): #stampa i vicini della parola nei due modelli e la loro intersezione.
    n1=model1.most_similar(stem)
    n2 = model2.most_similar(stem)
    intersection = neighbors_intersection(n1,n2)
    perc =  len(intersection)/max(len(n1),len(n2))
    print 'Percentage of overlapping: ' + str(perc)
    print 'Neighbors : '+str(intersection)
    print n1
    print n2

def vectors_comparison(model1,model2,stem): #stampa i vettori della parola nei due modelli e la loro cosin similarity.
    v1 = model1[stem]
    v2 = model2[stem]
    cosim = dot(unitvec(v1),unitvec(v2))
    print 'Cosine similarity between vectors: '+str(cosim)

def frequency_comparison(model1,model2,stem):
    c1 = model1.vocab[stem].count
    t1 = len(model1.vocab)
    f1 = round(c1/t1,4)

    c2 = model2.vocab[stem].count
    t2 = len(model2.vocab)
    f2 = round(c2/t2,4)
    print ' Count in model 1'+ str(c1)+ ' freq: ' + str(f1)
    print ' Count in model 1'+ str(c2)+ ' freq: ' + str(f2)

def top_freq_word(title,model):
    print 'MOST FREQUENT WORDS IN MODEL: '+ title
    for count in range(0,100):
        for word, vocab_obj in model.vocab.items():
            if (vocab_obj.index == count):
                print str(count) +' '+ str(word) +' '+  str(vocab_obj.count)

def common_words(model1,model2):
    s1 =set([])
    s2 = set([])
    for word in model1.vocab.items():
        s1.add(word[0])
    print len(s1)
    for word in model2.vocab.items():
        s2.add(word[0])
    print len(s2)
    shared_items = s1 & s2
    return shared_items

def frequent_common_words(model1,model2,treshold):
    s1 = set([])
    s2 = set([])
    for word, vocab_obj in model1.vocab.items():
        if (vocab_obj.index < treshold):
            s1.add(word)
    print 'MOST FREQUENT WORDS FIRST GROUP:'
    print str(s1)
    for word, vocab_obj in model2.vocab.items():
        if (vocab_obj.index < treshold):
            s2.add(word)
    print 'MOST FREQUENT WORDS SECOND GROUP:'
    print str(s2)
    shared_items = s1 & s2
    return shared_items