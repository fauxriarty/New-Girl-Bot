import tweepy
import random
import time
import requests

api_key = "xyz"
api_key_secret = "abc"
access_token = "123"
access_token_secret = "456"
bearer = r"abc"
client = tweepy.Client(bearer, api_key, api_key_secret, access_token, access_token_secret)
authenticator = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)

clientid = "klmn"
clientsecret = "abcdef"

api = tweepy.API(authenticator)

with open('dialogues.txt', 'r') as f:
    dialogues = f.readlines()

# Set the number of dialogues to select for each tweet
num_dialogues = 3

while True:
    # Check if internet connection is available
    try:
        requests.get('https://www.google.com/')
    except requests.exceptions.RequestException as e:
        print("No internet connection. Retrying in 2 mins...")
        time.sleep(120)
        continue
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
        dialogue_str = '\n'.join(selected_dialogues)

        # Tweet the dialogues
        client.create_tweet(text=dialogue_str)

        # Wait for 24 hours before tweeting again
        time.sleep(14400)

    else:
        # Get a new set of dialogues
        continue

