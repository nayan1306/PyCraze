import requests
from bs4 import BeautifulSoup
import re

# URL of the page we want to scrape
url = 'https://en.wikiquote.org/wiki/Main_Page'

# Send a GET request to the URL
response = requests.get(url)


# Check if the request was successful
if response.status_code == 200:
    # Parse the page content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'lxml')
    
    
    quote = soup.find('div',attrs={'id':'mf-qotd'}).find('td').text
    # Remove extra characters (new lines, etc.)
    cleaned_quote = re.sub(r'\s+', ' ', quote).strip()
    
    print(cleaned_quote)
   

    
else:
    print(f'Failed to retrieve the page. Status code: {response.status_code}')
