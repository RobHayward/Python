#!/usr/bin/python
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://bbc.co.uk/weather/bn3')
try: 
    elem = browser.find_element_by_tag_name('Find a Forecast')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name')

