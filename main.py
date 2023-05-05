import tweepy
import time
import random

api_key = "cJuF7sWrFwE6PvOSHhtgrqKvD"
api_key_secret = "5gfSabIlwrScMbiW6MTHQZyRLqegFS8FXYRuXdcxZJeDNyEIuA"
access_token = "1653852947812581376-Ye6qQtQ1eldIgLP26ACoCrUxPIZf2i"
access_token_secret = "IHDPirvT3QFBRpT9U17bDNKIDmCeoS5l2aa354M0jvA1h"
bearer = r"AAAAAAAAAAAAAAAAAAAAACLenAEAAAAAsLzoCCFBXgwwo1wXcqZ9EkZd4eQ%3DY9VRw25UMETNC8fIa0phlOw9ph9ZCXizsS3RJsrLuqcNLVW9QI"
client = tweepy.Client(bearer, api_key, api_key_secret, access_token, access_token_secret)
authenticator = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)

clientid = "dHlPTlZ2bnNibjBHNzFvMGlJWHk6MTpjaQ"
clientsecret = "AMm2G1ysWP463wh6Mz8LblT-vOq-7IxpChYemf6hiEdA0eoWTC"

api = tweepy.API(authenticator)


with open('dialogues1.txt', 'r', encoding='utf-8') as file:
    dialogues = file.read().split('\n\n')

# Set up a loop to tweet a random dialogue every 24 hours
while True:
    # Get a random dialogue from the list
    random_dialogue = random.choice(dialogues)

    # Tweet the random dialogue
    client.create_tweet(text=random_dialogue)

    # Wait for 24 hours before tweeting again
    time.sleep(86400)