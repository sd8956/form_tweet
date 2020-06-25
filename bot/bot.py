import tweepy, time, os
from dotenv import load_dotenv

load_dotenv()

def twitter_setup():
    auth = tweepy.OAuthHandler(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'))
    auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_SECRET'))

    api = tweepy.API(auth)
    return api

def make_tweet(tweet):
    bot = twitter_setup()

    try:
        bot.update_status(tweet)
    except tweepy.TweepError as e:
        print(e.reason)

