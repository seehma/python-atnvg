from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('./chromedriver')
browser.get('https://www.beckhoff.de')

browser.switch_to.frame('frame_left')
navButtonAutomation = browser.find_element_by_link_text('Automation')
navButtonAutomation.click()
navButtonTwincat3 = browser.find_element_by_link_text('TwinCAT 3')
navButtonTwincat3.click()
navButtonDownloadTC3 = browser.find_element_by_link_text('Download TwinCAT 3')
navButtonDownloadTC3.click()

browser.switch_to.default_content()
browser.switch_to.frame('main')
linkTextTE1xxxEngineering = browser.find_element_by_link_text('TE1xxx | Engineering')
linkTextTE1xxxEngineering.click()

tableCellDownloadName = browser.find_elements_by_class_name('download-name')
for tableTag in tableCellDownloadName:
    if tableTag.tag_name == 'td':
        print('Product: '+tableTag.text)

tableCellDownloadVersion = browser.find_elements_by_class_name('download-version')
for tableTag in tableCellDownloadVersion:
    if tableTag.tag_name == 'td':
        print('Version: '+tableTag.text)

