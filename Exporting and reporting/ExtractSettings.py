# This script is working for

# Endpoint Security section of Intune:
# Security Baselines
# Defender Baselines
# Edge Baselines
# Microsoft 365 Apps Baselines

# Device Management section of Intune:
# MEM -Settings catalog
# MEM - Device restrictions
# MEM - Wi-Fi profiles
# MEM - Endpoint protection profiles
# MEM - Health monitoring

# The letter "Ł" can be used as a seperator in Excel. Work in progress!

import bs4
import requests
from bs4 import BeautifulSoup

# Checks what the input is
def check_input(url):
    result = open(url)
    soup = BeautifulSoup(result, 'html.parser')
    checkfor = soup.find('div', {'class': 'fxs-blade-title-subtitleText msportalfx-tooltip-overflow fxs-portal-subtext'})
    checkforSecurity = soup.find('div', {'class': 'fxs-breadcrumb-crumb fxs-portal-text fxs-breadcrumb-crumb-active'})
    checkfor = f"{checkfor.text}"
    print(checkfor)
   
    if checkfor:
        if checkfor == "Device configuration profile":
            settings_catalog(url)

        if checkfor == "Device Configuration Profiles - Wi-Fi":
            wifi_endpointprotection(url)

        if checkfor == "Device Configuration Profiles - Endpoint protection":
            wifi_endpointprotection(url)

        if checkfor == "Device Configuration Profiles - Windows health monitoring":
            health_monitoring(url)

        if checkfor == "Device Configuration Profiles - Device restrictions":
            device_restrictions(url)

        if checkfor == "Security baseline":
            endpoint_protection(url)

        else:
         print("Unable to detect HTML file.")   

    else:
        print("Unable to detect HTML file.")

# Endpoint Security section of Intune:
# Security Baselines
# Defender Baselines
# Edge Baselines
# Microsoft 365 Apps Baselines
def endpoint_protection(url):
    result = open(url)
    soup = BeautifulSoup(result, 'html.parser')
    results = soup.find_all('div', {'class': 'fxs-portal-border fxc-accordion-section fxc-accordion-section-expanded'})

    for result in results[1:]:
        headertext = result.find('div', {'class': 'fxc-accordion-header-text msportalfx-tooltip-overflow'})
        sections = result.find_all('div', {'class': 'fxc-weave-pccontrol fxc-section-control fxc-base msportalfx-customHtml msportalfx-form-formelement fxc-has-label'})
        layer2section = result.find_all('div', {'class': 'fxc-weave-pccontrol fxc-section-control msportalfx-nested-control fxc-base msportalfx-customHtml msportalfx-form-formelement fxc-has-label'})
        headertext = f"{headertext.text.strip()}"

        if layer2section:
                for s in layer2section:
                    question = s.find('div', {'class': 'azc-form-labelcontainer azc-text-label'})
                    edgeSettings = s.find('div', {'data-bind': 'text: customContent'})
                    dropdown = s.find('div', {'class': 'azc-formControl azc-input fxc-dropdown-open msportalfx-tooltip-overflow azc-validation-border fxc-dropdown-input azc-disabled'})
                    radiobutton = s.find('li', {'class': 'fxs-portal-border azc-optionPicker-item fxs-portal-button-primary fxs-button-disabled fxs-portal-optionPicker-disabled azc-disabled'})
                    checkyourself = s.find('div', {'class': 'azc-inputbox-wrapper azc-numericTextBox-wrapper'})

                    if dropdown:
                        answer = dropdown
                        text = f"{headertext}Ł{question.text.strip()}Ł{answer.text}"
                        print(text)
                        continue

                    if radiobutton:
                        answer = radiobutton
                        text = f"{headertext}Ł{question.text.strip()}Ł{answer.text}"
                        print(text)
                        continue

                    if edgeSettings:
                        answer = edgeSettings
                        text = f"{headertext}Ł{question.text.strip()}Ł{answer.text}"
                        print(text)
                        continue

                    if checkyourself:
                        text = f"{headertext}Ł{question.text.strip()}ŁCheck the data yourself, value cannot be fetched."
                        print(text)
                        continue

                    else:
                        text = f"{headertext}Ł{question.text.strip()}ŁCheck the data yourself, value cannot be fetched."
                        print(text)
                        continue

        for section in sections:                      
                question = section.find('div', {'class': 'azc-form-labelcontainer azc-text-label'})
                edgeSettings = section.find('div', {'data-bind': 'text: customContent'})
                dropdown = section.find('div', {'class': 'azc-formControl azc-input fxc-dropdown-open msportalfx-tooltip-overflow azc-validation-border fxc-dropdown-input azc-disabled'})
                radiobutton = section.find('li', {'class': 'fxs-portal-border azc-optionPicker-item fxs-portal-button-primary fxs-button-disabled fxs-portal-optionPicker-disabled azc-disabled'})
                checkyourself = section.find('div', {'class': 'azc-inputbox-wrapper azc-numericTextBox-wrapper'})
                text = f"{question.text.strip()}"

                if dropdown:
                    answer = dropdown
                    text = f"{headertext}Ł{question.text.strip()}Ł{answer.text}"
                    print(text)
                    continue

                if radiobutton:
                    answer = radiobutton
                    text = f"{headertext}Ł{question.text.strip()}Ł{answer.text}"
                    print(text)
                    continue

                if edgeSettings:
                    answer = edgeSettings
                    text = f"{headertext}Ł{question.text.strip()}Ł{answer.text}"
                    print(text)
                    continue

                if checkyourself:
                    text = f"{headertext}Ł{question.text.strip()}ŁCheck the data yourself, value cannot be fetched."
                    print(text)
                    continue

                else:
                    text = f"{headertext}Ł{question.text.strip()}ŁCheck the data yourself, value cannot be fetched."
                    print(text)
                    continue

# MEM - Device restrictions
def device_restrictions(url):
    # url = 'local location including extention'
    result = open(url)
    soup = BeautifulSoup(result, 'html.parser')
    results = soup.find_all('div', {'class': 'fxs-portal-border fxc-accordion-section fxc-accordion-section-expanded'})
    for result in results:
        sectiontitle = result.find('div', {'class': 'fxc-accordion-header-text msportalfx-tooltip-overflow'})
        # sectiontitle = f"{sectiontitle.text}"
        questionsections = result.find_all('div', {'class': 'fxc-summary-item-row'})
        for singlequestion in questionsections:
            question = singlequestion.find('div', {'class': 'fxc-summary-item fxc-summary-label'})
            answer = singlequestion.find('div', {'class': 'fxc-summary-item fxc-summary-item-value'})
            if singlequestion:
                text = f"{sectiontitle.text}Ł{question.text}Ł{answer.text}"
                print(text)

# MEM - Endpoint protection profiles
# MEM - Wi-Fi profiles
# MEM - HTML elements for Wi-Fi and Endpoint protection profiles in MEM are the same.
def wifi_endpointprotection(url):
    result = open(url)
    soup = BeautifulSoup(result, 'html.parser')
    results = soup.find_all('div', {'class': 'fxs-portal-border fxc-accordion-section fxc-accordion-section-expanded'})
    for result in results:
        sectiontitle = result.find('div', {'class': 'fxc-accordion-header-text msportalfx-tooltip-overflow'})
        questionsections = result.find_all('div', {'class': 'fxc-summary-item-row'})
        for singlequestion in questionsections:
            firewallRules = singlequestion.find_all('div', {'class': 'fxc-gc-text'})
            if firewallRules:
                for rule in firewallRules:
                    rule = f"{rule.text}"
                    if rule == "No rules":
                        continue            
                    else:
                        print(rule) 
            else:
                question = singlequestion.find('div', {'class': 'fxc-summary-item fxc-summary-label'})
                answer = singlequestion.find('div', {'class': 'fxc-summary-item fxc-summary-item-value'})
                text = f"{sectiontitle.text}Ł{question.text}Ł{answer.text}"
                print(text)

# MEM - Health monitoring
def health_monitoring(url):
    result = open(url)
    soup = BeautifulSoup(result, 'html.parser')
    results = soup.find_all('div', {'class': 'fxs-portal-border fxc-accordion-section fxc-accordion-section-expanded'})
    for result in results:
        sectiontitle = result.find('div', {'class': 'fxc-accordion-header-text msportalfx-tooltip-overflow'})
        questionsections = result.find_all('div', {'class': 'fxc-summary-item-row'})
        for singlequestion in questionsections:
            question = singlequestion.find('div', {'class': 'fxc-summary-item fxc-summary-label'})
            answer = singlequestion.find('div', {'class': 'fxc-summary-item fxc-summary-item-value'})
            text = f"{sectiontitle.text}Ł{question.text}Ł{answer.text.strip()}"
            print(text)

# MEM -Settings catalog
def settings_catalog(url):
    result = open(url)
    soup = BeautifulSoup(result, 'html.parser')
    sections = soup.find_all('div', {'class': 'fxs-portal-border fxc-accordion-section fxc-accordion-section-expanded'})
    for result in sections:
        sectiontitle = result.find('div', {'class': 'ext-intune-accordion-header-container'})
        sectiontitle = f"{sectiontitle.text.strip()}"
        questionsections = result.find_all('div', {'class': 'fxc-weave-pccontrol fxc-section-control fxc-base msportalfx-customHtml msportalfx-form-formelement fxc-has-label'})
        for singlequestion in questionsections:
            question = singlequestion.find('label', {'class': 'azc-form-label'})
            answer = singlequestion.find('div', {'data-bind': 'text: customContent'})
            text = f"{sectiontitle}Ł{question.text}Ł{answer.text}"
            print(text)

check_input("/Users/user/Downloads/Exporting and reporting/SecurityBaseline_M365Apps_ZeroTolerance - Microsoft Intune admin center.html")
