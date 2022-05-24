import helper_functions
import time
import datetime as dt
import tweepy
import json

# Load in Twitter credentials from local drive
with open('../../Dropbox/100DaysOfCodePRIVATE/BigramCreds.json') as file:
    creds = json.loads(file.read())

API_KEY = creds['API_KEY']
API_SECRET = creds['API_SECRET']
ACCESS_TOKEN = creds['ACCESS_TOKEN']
ACCESS_SECRET = creds['ACCESS_SECRET']

# Set up connection with Twitter API v2 using Tweepy wrapper
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Run continuously
while True:
    try:
        # Define search criteria
        query = api.search_tweets(q='machine learning',  # returns tweets that include 'machine learning'
                                  lang='en',             # returns English-language tweets
                                  count=100,             # returns 100 tweets
                                  result_type='recent'   # returns most recent tweets
                                  )
        # Loop through all queried tweets and find the first one that meets all selection criteria
        for i in range(len(query)):
            tweet = query[i]

            # Check if selection criteria are met
            if helper_functions.conditions_met(tweet):
                # Returns a formatted bigram poem
                poem = helper_functions.bigram_tweet(tweet)
                print(poem, '\n')

                # Sends out poem as a tweet
                api.update_status(poem)

                # Prints link to original tweet
                print(f'https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}')

                # Stops reviewing tweets from query after successful post
                break

    # Prints error if given
    except Exception as e:
        print(e, '\n')

    # Prints current timestamp
    print(dt.datetime.now(), '\n')

    # Sleeps for stated number of seconds
    time.sleep(60)
