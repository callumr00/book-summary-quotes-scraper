# Import modules
import requests
from bs4 import BeautifulSoup
import os
import random
from tqdm import tqdm
# -----------------------------------------------------------
# Get list of completed book summaries
def getBooks():
    # Create empty list for book summaries
    items = []

    # Set URL at the location of the list of book summaries
    url = "https://github.com/callumr00/callumr.com/tree/main/books"

    # Find all book summary pages
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    pages = soup.find_all('div', class_='Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item')

    # Append each book summary page to list
    for i in range(len(pages)):
        items.append(pages[i].find_all('a')[0].text.strip())

    # Return list of book summaries
    return items

# Get quotes from each book summary
def getQuotes():
    # Create empty list for quotes
    items = []

    # Print task update
    print(f"\nGetting a selection of {amnt} quotes from book summaries at callumr.com...\n")

    # For each book summary, append quotes to list
    for i in tqdm(getBooks()):
        # Set URL of each book summary
        url = "https://callumr.com/books/" + i

        # Find all quotes on page
        soup = BeautifulSoup(requests.get(url).content, 'html.parser')
        quotes = soup.find_all('div', class_='content__quote')

        # Append each quote to list
        for i in range(len(quotes)):
            items.append(quotes[i].text)

    # Print horizontal line and centered header
    print(f"\n{'─'*os.get_terminal_size().columns}\n")
    print(' Quotes '.center(os.get_terminal_size().columns, ' '))

    # Return list of quotes
    return items

# Show random quotes of a defined amount
def showQuotes(amnt):
    # Get populated list of quotes
    quotes = getQuotes()

    # Generate random numbers
    sample = random.sample(range(1,len(quotes)),amnt)

    # Get quotes, using generated random numbers for the index of each
    for item in sample:
        print(quotes[item])

# Define amount of quotes to show
amnt = 3
showQuotes(amnt)