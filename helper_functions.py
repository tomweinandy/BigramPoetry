import nltk
import datetime as dt


def conditions_met(tweet):
    conditions_list = ['RT' not in tweet.text,
                       len(tweet.text.split(' ')) > 2,
                       # 'http' not in tweet.text,
                       tweet.lang == 'en',
                       tweet.user.screen_name != 'BrigramPoetry']
    return all(conditions_list)


def cleaner(phrase):
    # phrase = phrase.replace('\n', ' ').replace('VIDEO', '')  # remove edge cases with bad formatting
    # phrase = phrase.replace(' -', ' ').replace(' –', ' ').replace(' ‘', '')
    # phrase = phrase.replace('- ', ' ').replace(' /', ' ').replace('— ', ' ')
    # phrase = phrase.replace(': ', ' ').replace(':)', '').replace('&amp', 'and')

    rejects = '¿.?!,[]|"“();…{}«•*+@~<>'                                  # define punctuation to be removed
    phrase_reject = phrase.translate({ord(c): None for c in rejects})     # remove defined punctuation
    phrase_split = phrase_reject.split(' ')                               # split phrase by whitespace
    phrase_clear = list(filter(None, phrase_split))                       # strip any extra whitespace
    return phrase_clear


def bigram_poem(phrase_raw):                                              # define new function bigram_poem
    phrase_cleaned = cleaner(phrase_raw)
    phrase_shortened = phrase_cleaned[0:8]                                # only use the first 8 terms
    phrase_bigram = list(nltk.bigrams(phrase_shortened))                  # convert to bigram list
    poem = ''                                                             # create new string
    for bigram in phrase_bigram:                                          # loop through bigrams
        poem += ' ' + bigram[0] + ' ' + bigram[1] + ' \n'                 # add looped bigrams to string w line break
    return poem


def bigram_tweet(tweet):
    # Compile tweet
    header = f'A Bigram Poem inspired by {tweet.user.screen_name}:\n'
    # print(header)
    poem = bigram_poem(tweet.text)
    footer = f'   - {tweet.user.name}'
    full_tweet = header + poem + footer

    # twitter.update_status(status=full_tweet)  # tweet out on @BigramPoetry account

    print(full_tweet)  # print result, timestamp (for testing)
    print(dt.datetime.now(), '\n')
