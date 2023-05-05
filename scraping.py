import requests
from bs4 import BeautifulSoup

# Base URL for the episode transcripts
base_url = 'https://transcripts.foreverdreaming.org/'
url = 'https://transcripts.foreverdreaming.org/viewforum.php?f=50&start=78'

episode_urls = []

dialogues_dict = {}

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# fibd all the topics on the page and extract the urls of the episode transcripts
topics = soup.find_all('a', class_='topictitle')
for topic in topics:
    episode_url = base_url + topic['href']
    episode_urls.append(episode_url)

# loop through all the episode urls and extract the dialogues
for episode_url in episode_urls:
    response = requests.get(episode_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    episode_num = soup.find('h2', class_='topic-title').text.split(':')[0].strip()
    dialogues = soup.find('div', class_='postbody').get_text()

    dialogues_dict[episode_num] = dialogues

with open('dialogues1.txt', 'w', encoding='utf-8') as file:
    for episode_num, dialogues in dialogues_dict.items():
        file.write("Episode {} - Number of dialogues: {}".format(episode_num, len(dialogues.split('\n'))))
        file.write(dialogues)
        file.write('\n\n')

