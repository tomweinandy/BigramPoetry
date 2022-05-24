import random
import helper_functions

with open('arrested_development.txt') as file:
    ad = file.read()

ad = ad.split(',')
phrase = random.choice(ad)
poem = helper_functions.bigram_poem(phrase)

print(poem)



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

# Query
query = api.search_tweets(q='machine learning', lang='en', count=100)


for i in range(len(query)):
    tweet = query[i]

    if helper_functions.conditions_met(tweet):

        helper_functions.bigram_tweet(tweet)

        break

