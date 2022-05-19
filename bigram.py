import nltk


def bigram_poem(phrase):                                                  # define new function bigram_poem
    rejects = '¿.?!,[]|"“();…{}«•*+@~<>'                                  # define punctuation to be removed
    phrase_reject = phrase.translate({ord(c): None for c in rejects})     # remove defined punctuation
    phrase_split = phrase_reject.split(' ')                               # split phrase by whitespace
    phrase_clear = list(filter(None, phrase_split))                       # strip any extra whitespace
    phrase_shortened = phrase_clear[0:8]                                  # only use the first 8 terms
    phrase_bigram = list(nltk.bigrams(phrase_shortened))                  # convert to bigram list
    poem = ''                                                             # create new string
    for bigram in phrase_bigram:                                          # loop through bigrams
        poem += ' ' + bigram[0] + ' ' + bigram[1] + ' \n'                 # add looped bigrams to string w line break
    return poem
