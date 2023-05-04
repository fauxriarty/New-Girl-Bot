import requests
from bs4 import BeautifulSoup

# Base URL for the episode transcripts
base_url = 'https://transcripts.foreverdreaming.org/'

# URL of the forum containing all the episode transcripts
url = 'https://transcripts.foreverdreaming.org/viewforum.php?f=50'

# List to store the URLs of all the episode transcripts
episode_urls = []

# Dictionary to store the dialogues for each episode
dialogues_dict = {}

# Loop through all the pages of the forum and extract the URLs of the episode transcripts
page_num = 1
while True:
    # Send a GET request to the current page of the forum and parse the HTML content using BeautifulSoup
    response = requests.get(f'{url}&start={(page_num - 1) * 25}')
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the topics on the page and extract the URLs of the episode transcripts
    topics = soup.find_all('a', class_='topictitle')
    for topic in topics:
        episode_url = base_url + topic['href']
        episode_urls.append(episode_url)

    # Check if there is a "Next" button to go to the next page
    next_button = soup.find('a', class_='next')
    if next_button:
        page_num += 1
    else:
        break

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

for dialogues in dialogues_dict.items():
    print(dialogues)
