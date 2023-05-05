import tweepy
import random
import time

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

"""
with open('dialogues.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Randomly select a starting index for the dialogue
start_index = random.randint(0, len(lines)-4)

# Get the two consecutive dialogues
dialogue1 = lines[start_index].strip()
dialogue2 = lines[start_index+1].strip()
dialogue3 = lines[start_index+2].strip()
dialogue4 = lines[start_index+3].strip()
# Create the tweet
tweet = f"-{dialogue1}\n-{dialogue2}\n-{dialogue3}\n-{dialogue4}\n"

# Post the tweet
client.create_tweet(text=tweet) """

with open('dialogues.txt', 'r') as f:
    dialogues = f.readlines()

# Set the number of dialogues to select for each tweet
num_dialogues = 4

while True:
    # Choose a random starting point in the dialogues list
    start_idx = random.randint(0, len(dialogues) - num_dialogues - 1)

    # Extract the selected dialogues
    selected_dialogues = dialogues[start_idx:start_idx + num_dialogues]

    # Check if at least 2 dialogues have more than 4 words
    num_long_dialogues = 0
    for dialogue in selected_dialogues:
        if len(dialogue.split()) >= 3:
            num_long_dialogues += 1

    if num_long_dialogues >= 2:
        # Concatenate the dialogues into a single string
        dialogue_str = '\n-'.join(selected_dialogues)

        # Tweet the dialogues
        client.create_tweet(text=dialogue_str)

        # Wait for 24 hours before tweeting again
        time.sleep(86400)

    else:
        # Get a new set of dialogues
        continue