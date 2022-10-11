import tweepy
from random_phrase import random_phrase
from keys import *

# Use the API V2
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

########## REALTIME TWEET A MENTION ##########

class Tweetmentions(tweepy.StreamingClient):
    """Allows you to monitor a user and retweet all content in real time"""
    def on_tweet(self, tweet):
        if tweet.referenced_tweets == None:
            print(tweet.text)    
            client.create_tweet(text=random_phrase(),
                                in_reply_to_tweet_id=str(tweet.id)
                                )
            print('Successfully tweeted!')

stream_mentions = Tweetmentions(bearer_token=bearer_token) # Instantiating the class
# Set your rule for real-time streaming to be enabled
# For this project the rule will be: Every time someone mentions the @ of bot it will automatically respond with a random phrase 
stream_mentions.add_rules(tweepy.StreamRule("@your_bot_id")) 
stream_mentions.filter(tweet_fields=['referenced_tweets']) # Now you can start monitoring with the rule sets



