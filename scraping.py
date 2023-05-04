import requests
from bs4 import BeautifulSoup

# Base URL for the episode transcripts
base_url = 'https://transcripts.foreverdreaming.org/'

# URL of the forum containing all the episode transcripts
url = 'https://transcripts.foreverdreaming.org/viewforum.php?f=50&start=78'

# List to store the URLs of all the episode transcripts
episode_urls = []

# Dictionary to store the dialogues for each episode
dialogues_dict = {}

# Loop through all the pages of the forum and extract the URLs of the episode transcripts
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the topics on the page and extract the URLs of the episode transcripts
topics = soup.find_all('a', class_='topictitle')
for topic in topics:
    episode_url = base_url + topic['href']
    episode_urls.append(episode_url)

# Loop through all the episode URLs and extract the dialogues
for episode_url in episode_urls:
    # Send a GET request to the episode transcript page and parse the HTML content using BeautifulSoup
    response = requests.get(episode_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the episode number and dialogues
    episode_num = soup.find('h2', class_='topic-title').text.split(':')[0].strip()
    dialogues = soup.find('div', class_='postbody').get_text()

    # Store the dialogues in the dictionary
    dialogues_dict[episode_num] = dialogues

# Write the dialogues for each episode to a text file
with open('dialogues1.txt', 'w', encoding='utf-8') as file:
    for episode_num, dialogues in dialogues_dict.items():
        file.write("Episode {} - Number of dialogues: {}".format(episode_num, len(dialogues.split('\n'))))
        file.write(dialogues)
        file.write('\n\n')
