# This script is working for
# Security Baselines
# Defender Baselines
# Edge Baselines
# Microsoft 365 Apps Baselines
# The letter "Ł" can be used as a seperator in Excel.

import bs4
import requests
from bs4 import BeautifulSoup

# url = 'local location including extention'
result = open(url)
soup = BeautifulSoup(result, 'html.parser')
results = soup.find_all('div', {'class': 'fxc-weave-pccontrol fxc-section-control fxc-base msportalfx-customHtml msportalfx-form-formelement fxc-has-label'})
for result in results:
    question = result.find('div', {'class': 'azc-form-labelcontainer azc-text-label'})
    edgeSettings = result.find('div', {'data-bind': 'text: customContent'})
    dropdown = result.find('div', {'class': 'azc-formControl azc-input fxc-dropdown-open msportalfx-tooltip-overflow azc-validation-border fxc-dropdown-input azc-disabled'})
    radiobutton = result.find('li', {'class': 'fxs-portal-border azc-optionPicker-item fxs-portal-button-primary fxs-button-disabled fxs-portal-optionPicker-disabled azc-disabled'})
    checkyourself = result.find('div', {'class': 'azc-inputbox-wrapper azc-numericTextBox-wrapper'})
    text = f"{question.text.strip()}"

    if dropdown:
        answer = dropdown
        text = f"{question.text.strip()}Ł{answer.text}"
        print(text)
        continue

    if radiobutton:
        answer = radiobutton
        text = f"{question.text.strip()}Ł{answer.text}"
        print(text)
        continue

    if edgeSettings:
        answer = edgeSettings
        text = f"{question.text.strip()}Ł{answer.text}"
        print(text)
        continue

    if checkyourself:
        text = f"{question.text.strip()}ŁCheck the data yourself, value cannot be fetched."
        print(text)
        continue

    else:
        text = f"{question.text.strip()}ŁCheck the data yourself, value cannot be fetched."
        print(text)
        continue
