import random
import helper_functions
import time
import datetime as dt

with open('arrested_development.txt') as file:
    ad = file.read()

ad = ad.split(',')
# phrase = random.choice(ad)
# ad_poem = helper_functions.bigram_poem(phrase)

# print(ad_poem)



# Load credentials
import tweepy
import json

with open('../../Dropbox/100DaysOfCodePRIVATE/JTCreds.json') as file:
    creds = json.loads(file.read())

API_KEY = creds['API_KEY']
API_SECRET = creds['API_SECRET']
ACCESS_TOKEN = creds['ACCESS_TOKEN']
ACCESS_SECRET = creds['ACCESS_SECRET']

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)


while True:
    # print(dt.datetime.now())
    # query = api.search_tweets(q='machine learning', lang='en', count=100, result_type='recent')
    # for i in range(len(query)):
    #     tweet = query[i]
    #
    #     if helper_functions.conditions_met(tweet):
    #         poem = helper_functions.bigram_tweet(tweet)
    #         # poem = helper_functions.bigram_poem(tweet.text)
    #         print(poem, dt.datetime.now(), '\n')
    #
    #         # phrase = random.choice(ad)
    #         # ad_poem = helper_functions.bigram_poem(phrase)
    #         api.update_status(poem)
    #
    #         break
    #
    # time.sleep(60)

    try:
        query = api.search_tweets(q='machine learning', lang='en', count=100, result_type='recent')
        for i in range(len(query)):
            tweet = query[i]

            if helper_functions.conditions_met(tweet):
                poem = helper_functions.bigram_tweet(tweet)
                # poem = helper_functions.bigram_poem(tweet.text)
                print(poem, '\n')

                # phrase = random.choice(ad)
                # ad_poem = helper_functions.bigram_poem(phrase)
                api.update_status(poem)

                break

    except Exception as e:
        print(e)

    print(dt.datetime.now())
    time.sleep(60)
