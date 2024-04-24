# This script is working for
# Setting Catalogs
# The letter "Ł" can be used as a seperator in Excel.

import bs4
import requests
from bs4 import BeautifulSoup

# url = 'local location including extention'
result = open(url)
soup = BeautifulSoup(result, 'html.parser')
results = soup.find_all('div', {'class': 'fxc-weave-pccontrol fxc-section-control fxc-base msportalfx-customHtml msportalfx-form-formelement fxc-has-label'})
for result in results:
    question = result.find('label', {'class': 'azc-form-label'})
    answer = result.find('div', {'data-bind': 'text: customContent'})
    text = f"{question.text}Ł{answer.text}"
    print(text)