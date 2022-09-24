# Import modules
import requests
from bs4 import BeautifulSoup
import random
# -----------------------------------------------------------
# Get list of completed book summaries
def getBooks():
    items = []
    url = "https://github.com/callumr00/callumr.com/tree/main/books"

    soup = BeautifulSoup(requests.get(url).content, 'html.parser')

    pages = soup.find_all('div', class_='Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item')

    for i in range(len(pages)):
        items.append(pages[i].find_all('a')[0].text.strip())

    return items

# Get quotes from each book summary
def getQuotes():
    items = []
    for item in getBooks():
        url = "https://callumr.com/books/" + item

        soup = BeautifulSoup(requests.get(url).content, 'html.parser')

        quotes = soup.find_all('div', class_='content__quote')

        for i in range(len(quotes)):
            items.append(quotes[i].text)

    return items

# Get random quotes of a defined amount
def showQuotes(amnt):
    quotes = getQuotes()

    sample = random.sample(range(1,len(quotes)),amnt)

    for item in sample:
        print(quotes[item])

# showQuotes(number of quotes)
showQuotes(3)