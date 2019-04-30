# Domain-specific-ambiguity
This is a tool for comparing terms of different domains, based on word embeddings models created from
the documents of different wikipedia portals. The portals are Computer Science, Electronic Engineering,
Mechanical Engineering, Sports, Medicine, Literature.

The project includes three packages:

1. domain_analysis: includes utilities to get statistics and manipulate the domain files.
2. vector_comparison: includes the utilities to build the word embeddings.
3. wiki_crawler: includes the software to download wikipedia pages from the different domains.

The project includes one utility main files:

- generate_domain_models.py: used to generate the models, which are saved in MODELS

Please refer to the following papers for more details---and cite the papers if you use the code:


Ferrari, A., Esuli, A., & Gnesi, S. (2018, August). Identification of cross-domain ambiguity with language models. In 2018 5th International Workshop on Artificial Intelligence for Requirements Engineering (AIRE) (pp. 31-38). IEEE.

Ferrari, A., Donati, B., & Gnesi, S. (2017, September). Detecting domain-specific ambiguities: an NLP approach based on Wikipedia crawling and word embeddings. In 2017 IEEE 25th International Requirements Engineering Conference Workshops (REW) (pp. 393-399). IEEE.
