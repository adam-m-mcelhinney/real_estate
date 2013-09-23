# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:06:24 2013

@author: amcelhinney

Description:
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.proxy import *


PROXY = "173.213.113.111:7808"

proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': PROXY,
    'ftpProxy': PROXY,
    'sslProxy': PROXY,
    'noProxy': '' # set this value as desired
    })




if __name__ == "__main__":
    #driver = webdriver.Firefox()
    driver = webdriver.Firefox(proxy=proxy)

    url = 'https://check.torproject.org/'
    
    driver.get(url)
    
    print driver.page_source
    # THIS WORKS!