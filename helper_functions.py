import nltk
import re


def conditions_met(tweet):
    """
    Checks if the conditions are met
    :param tweet: A status type object
    :return: True if all conditions hold, False if any one condition is not true
    """
    conditions_list = [
        'RT' not in tweet.text,                    # exclude retweets
        tweet.text[0] != '@',                      # exclude replies
        len(tweet.text.split(' ')) > 2,            # tweet must be 3 or more words long
        tweet.lang == 'en',                        # tweet must be in English
        tweet.user.screen_name != 'BrigramPoetry'  # exclude tweets from self
    ]
    return all(conditions_list)


def cleaner(phrase):
    """
    Processes the text, mostly by removing special characters
    :param phrase: Tweet text input
    :return: List of words from the tweet
    """
    # Remove problematic strings and characters
    replacers = ['\n', 'VIDEO', ' -', '- ', '— ', ' —', ' /']
    for replacer in replacers:
        phrase = phrase.replace(replacer, ' ')                         # replace with whitespace
    phrase = phrase.replace('&amp', 'and')

    rejects = ':¿.?!,[]|"“();…{}«•*+@~<>'                              # define punctuation to be removed
    phrase_reject = phrase.translate({ord(c): None for c in rejects})  # remove defined punctuation
    phrase_no_url = re.sub(r'http\S+', '', phrase_reject)              # remove urls
    phrase_split = phrase_no_url.split(' ')                            # split phrase by whitespace
    phrase_list = list(filter(None, phrase_split))                     # strip any extra whitespace
    return phrase_list


def bigram_poem(phrase_raw):
    """
    Create a bigram poem from the raw text of a tweet
    :param phrase_raw: Raw text from tweet
    :return: A bigram poem from the first 8 words
    """
    phrase_cleaned = cleaner(phrase_raw)
    phrase_shortened = phrase_cleaned[0:8]                 # only use the first 8 words
    phrase_bigram = list(nltk.bigrams(phrase_shortened))   # convert to bigram list
    poem = ''                                              # create new string
    for bigram in phrase_bigram:                           # loop through bigrams
        poem += ' ' + bigram[0] + ' ' + bigram[1] + ' \n'  # add looped bigrams to string w line break
    return poem


def bigram_tweet(tweet):
    """
    Compile bigram poem into a tweet
    :param tweet: The entire tweet of status type
    :return: Bigram poem with header and footer to be sent out as tweet
    """
    # Compile tweet
    header = f'A Bigram Poem inspired by {tweet.user.screen_name}:\n'
    poem = bigram_poem(tweet.text)
    footer = f'   - {tweet.user.name}'
    full_tweet = header + poem + footer

    return full_tweet
