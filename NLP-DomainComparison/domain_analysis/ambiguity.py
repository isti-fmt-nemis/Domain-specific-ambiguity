import itertools

import spacy

import numpy as np


nlp = spacy.load('en')


def get_sorted_vocab(mdl):
    with_freq = [(word, vocab_entry.count) for word, vocab_entry in mdl.wv.vocab.items()]
    return sorted(with_freq, key=lambda x: -x[1])


tags = dict()


def get_tag(word):
    if word in tags:
        return tags[word]
    tag = list(nlp(word))[0].tag_
    tags[word] = tag
    return tag


def get_frequent_shared_words_spacy(domains, size=100):
    sorted_vocabs = list()
    for domain in domains:
        sorted_vocabs.append(get_sorted_vocab(domain))
    min_vocab_size = min([len(sorted_vocab) for sorted_vocab in sorted_vocabs])
    head = size
    while True:
        common = set([word for word, freq in sorted_vocabs[0][:head]])
        for sorted_vocab in sorted_vocabs[1:]:
            common = common.intersection(set([word for word, freq in sorted_vocab[:head]]))
        if len(common) < size:
            head += 1
            continue
        to_remove = set()
        for word in common:
            if get_tag(word) != 'NN':
                to_remove.add(word)
            elif len(word) == 1:
                to_remove.add(word)
            elif word.isnumeric():
                to_remove.add(word)
        common.difference_update(to_remove)
        if len(common) >= size or head >= min_vocab_size:
            return common
        head += 1


def get_frequent_words_spacy(domain, size=100):
    sorted_vocab = get_sorted_vocab(domain)
    head = size
    selected = set([word for word, freq in sorted_vocab[:head]])
    to_remove = set()
    for word in selected:
        if get_tag(word) != 'NN':
            to_remove.add(word)
        elif len(word) == 1:
            to_remove.add(word)
        elif word.isnumeric():
            to_remove.add(word)
    selected.difference_update(to_remove)
    while True:
        if len(selected) >= size or head >= len(selected):
            return selected
        head += 1
        word = sorted_vocab[head]
        if get_tag(word) == 'NN' and len(word) > 1 and not word.isnumeric():
            selected.add(word)
            
def get_min_freq_words_spacy(domain, min_freq=1000):
    sorted_vocab = get_sorted_vocab(domain)
    selected = set([word for word, freq in sorted_vocab if freq>=min_freq])
    to_remove = set()
    for word in selected:
        if get_tag(word) != 'NN':
            to_remove.add(word)
        elif len(word) == 1:
            to_remove.add(word)
        elif word.isnumeric():
            to_remove.add(word)
    selected.difference_update(to_remove)
    return selected


def ambiguity_mse_rank(domains, vocab_size=100, w2v_topn=100):
    words = get_frequent_shared_words_spacy(domains, vocab_size)
    output = list()
    for word in words:
        sorted_tops = list()
        sorted_words = list()
        tops = list()
        for domain in domains:
            sorted_tops.append(domain.wv.most_similar(word, topn=w2v_topn))
            sorted_words.append([word for word, score in sorted_tops[-1]])
            tops.append(dict(sorted_tops[-1]))

        shared = set()
        for top_word in tops:
            shared.update(top_word.keys())

        mse = 0
        for shared_word in shared:
            min_rank = w2v_topn + 1

            for sorted_word in sorted_words:
                try:
                    min_rank = min(min_rank, sorted_word.index(shared_word) + 1)
                except:
                    pass
            scores = list()
            for top in tops:
                scores.append(top.get(shared_word, 0))

            mse += np.var(scores) / min_rank
        counts = list()
        for domain in domains:
            counts.append(domain.wv.vocab[word].count)
        output.append((word, len(shared), mse, counts))
    return sorted(output, key=lambda x: -x[2])


def ambiguity_mse_rank_multi(domains, vocab_size=100, w2v_topn=100):
    count = len(domains)
    by_word = dict()
    for size in range(2, count + 1):
        for to_test in itertools.combinations(domains, size):
            for word, shared, mse, counts in ambiguity_mse_rank([model for _, model in to_test], vocab_size, w2v_topn):
                if word in by_word:
                    prev_mse = by_word[word][2]
                    if mse >= prev_mse:
                        by_word[word] = ([name for name, _ in to_test], word, shared, mse, counts)
                else:
                    by_word[word] = ([name for name, _ in to_test], word, shared, mse, counts)
    return sorted(by_word.values(), key=lambda x: -x[3])


def ambiguity_mse_rank_main_domain(main_domain, domains, min_freq_ratio = 0.5, vocab_size=200, w2v_topn=1000, min_freq_main =800):
    words = get_min_freq_words_spacy(main_domain, min_freq_main)
    output = list()
    for word in words:
        word_freq = main_domain.wv.vocab[word].count
        min_freq = word_freq*min_freq_ratio
        sorted_tops = list()
        sorted_words = list()
        tops = list()
        for domain in domains:
            try:
                other_domain_word_freq = domain.wv.vocab[word].count
            except KeyError:
                other_domain_word_freq = 0
            if other_domain_word_freq >= min_freq and other_domain_word_freq <= word_freq:
                domain_sim = list()
                try:
                    most_similar = domain.wv.most_similar(word, topn=w2v_topn)
                    for similar_word in most_similar:
                        domain_sim.append(similar_word)

                except KeyError:
                    continue
                sorted_tops.append(domain_sim)
                sorted_words.append([word for word, score in sorted_tops[-1]])
                tops.append(dict(sorted_tops[-1]))

        shared = set()
        for top_word in tops:
            shared.update(top_word.keys())
        if len(shared)>0:

            main_domain_sim = list()
            try:
                most_similar = main_domain.wv.most_similar(word, topn=w2v_topn)
                for similar_word in most_similar:
                    main_domain_sim.append(similar_word)

            except KeyError:
                continue
            sorted_tops.append(main_domain_sim)
            sorted_words.append([word for word, score in sorted_tops[-1]])
            tops.append(dict(sorted_tops[-1]))
            shared = set()
            for top_word in tops:
                shared.update(top_word.keys())

            mse = 0
            for shared_word in shared:
                min_rank = w2v_topn + 1

                for sorted_word in sorted_words:
                    try:
                        min_rank = min(min_rank, sorted_word.index(shared_word) + 1)
                    except:
                        pass
                scores = list()
                for top in tops:
                    scores.append(top.get(shared_word, 0))

                mse += np.var(scores) / min_rank
            counts = list()
            counts.append(word_freq)
            for domain in domains:
                try:
                    counts.append(domain.wv.vocab[word].count)
                except KeyError:
                    counts.append(0)
            output.append((word, len(shared), mse, counts))
    return sorted(output, key=lambda x: -x[2])


def ambiguity_mse_rank_merge(domains, min_freq_ratio=0.5, vocab_size=200, w2v_topn=1000):
    by_word = dict()
    for domain in domains:
        other_domains = set(domains).difference(set([domain]))
        for word, shared, mse, counts in ambiguity_mse_rank_main_domain(domain[1],
                                                                        [model for _, model in other_domains],
                                                                        min_freq_ratio, vocab_size, w2v_topn):
            if word in by_word:
                prev_mse = by_word[word][2]
                if mse >= prev_mse:
                    by_word[word] = (domain[0], word, shared, mse, counts)
            else:
                by_word[word] = (domain[0], word, shared, mse, counts)
    return sorted(by_word.values(), key=lambda x: -x[3])
