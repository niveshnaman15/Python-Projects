
# Web Scraping with BeautifulSoup
import requests
from bs4 import BeautifulSoup

# Sample scraping from example.com
url = 'https://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract and print title
title = soup.title.string
print("Page Title:", title)
