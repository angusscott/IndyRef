'''
This implements: http://en.wikipedia.org/wiki/Inverted_index of 28/07/10
'''
 
from pprint import pprint as pp
from glob import glob
import pickle
try: reduce
except: from functools import reduce
try:    raw_input
except: raw_input = input
 
 
def parsetexts(fileglob='UsersTweetsClass/[ynu]*/*.txt'):
    texts, words = {}, set()
    print glob(fileglob)
    for txtfile in glob(fileglob):
        with open(txtfile, 'r') as f:
            txt = f.read().split()
            words |= set(txt)
            texts[txtfile.split('\\')[-1]] = txt
    return texts, words
 
def termsearch(terms): # Searches simple inverted index
    return reduce(set.intersection,
                  (invindex[term] for term in terms),
                  set(texts.keys()))
 
texts, words = parsetexts()
print('\nTexts')
#pp(texts)
print('\nWords')
words = sorted(words)
pp(words)
 
invindex = {}
for word in words:
    docs = [] 
    for txt, wrds in texts.items():
        if word in wrds:
            docs.append(txt)
    invindex[word] = set(docs)
    print word
print('\nInverted Index')
#pp({k:sorted(v) for k,v in invindex.items()})

pickle.dump( invindex, open( "tweetindex.p", "wb" ) )

 
# terms = ["what", "is", "it"]
# print('\nTerm Search for: ' + repr(terms))
# pp(sorted(termsearch(terms)))