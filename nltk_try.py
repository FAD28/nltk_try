import nltk
corp = nltk.corpus.ConllCorpusReader('.', 'tiger_release_aug07.corrected.16012013.conll09',
                                     ['ignore', 'words', 'ignore', 'ignore', 'pos'],
                                     encoding='utf-8')

# import random
#
# tagged_sents = list(corp.tagged_sents())
# random.shuffle(tagged_sents)
#
# # set a split size: use 90% for training, 10% for testing
# split_perc = 0.1
# split_size = int(len(tagged_sents) * split_perc)
# train_sents, test_sents = tagged_sents[split_size:], tagged_sents[:split_size]

from ClassifierBasedGermanTagger
from ClassifierBasedGermanTagger.ClassifierBasedGermanTagger import ClassifierBasedGermanTagger
tagger = ClassifierBasedGermanTagger(train=train_sents)

accuracy = tagger.evaluate(test_sents)

tagger.tag(['Das', 'ist', 'ein', 'einfacher', 'Test'])
print(tagger.tag(['Das', 'ist', 'ein', 'einfacher', 'Test']))
