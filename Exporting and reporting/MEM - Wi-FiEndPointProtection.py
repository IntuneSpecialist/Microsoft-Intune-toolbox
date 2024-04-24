# This script is working for
# Wi-Fi profiles
# Endpoint Protection profiles
# The letter "Ł" can be used as a seperator in Excel.

import bs4
import requests
from bs4 import BeautifulSoup

# url = 'local location including extention'
result = open(url)
soup = BeautifulSoup(result, 'html.parser')
results = soup.find_all('div', {'class': 'fxs-portal-border fxc-accordion-section fxc-accordion-section-expanded'})
for result in results:
    rows = result.find_all('div', {'class': 'fxc-summary-item-row'})
    for row in rows:
        firewallRules = row.find_all('div', {'class': 'fxc-gc-text'})
        if firewallRules:
            for rule in firewallRules:
                rule = f"{rule.text}"
                if rule == "No rules":
                    continue            
                else:
                    print(rule) 
        else:
            question = row.find('div', {'class': 'fxc-summary-item fxc-summary-label'})
            answer = row.find('div', {'class': 'fxc-summary-item fxc-summary-item-value'})
            text = f"{question.text}Ł{answer.text}"
            print(text)