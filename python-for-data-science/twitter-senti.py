import tweepy
from textblob import TextBlob 
from decouple import config

consumer_key = config('consumer_key')
consumer_secret = config('consumer_secret')

access_token = config('access_token')
access_token_secret = config('access_token_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

api = tweepy.API(auth)

query = input("Enter a query: ")

public_tweets = api.search(query)

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("------------------------------")