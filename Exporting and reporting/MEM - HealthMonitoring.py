# The letter "Ł" can be used as a seperator in Excel.

import bs4
import requests
from bs4 import BeautifulSoup

# url = 'local location including extention'
result = open(url)
soup = BeautifulSoup(result, 'html.parser')
# print(soup.prettify())
results = soup.find_all('div', {'class': 'fxc-summary-item-row'})
# print(results)
for result in results:    
    question = result.find('div', {'class': 'fxc-summary-item fxc-summary-label'})
    if question:
        answer = result.find('div', {'class': 'fxc-summary-item fxc-summary-item-value'})
        text = f"{question.text}Ł{answer.text.strip()}"
        print(text)