# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 18:24:48 2013

@author: amcelhinney

Description:
    Selenium Scraping Helper functions
"""
from bs4 import BeautifulSoup
from selenium import webdriver
from pyvirtualdisplay import Display
# the code profiler says that this is not used, however it is
from selenium.webdriver.common.proxy import *

'''
class myClass:
    
  def __init__(self):
'''
      
def createDriver(proxyPort = None, headLess = True):
    """
    Creates a Selenium driver
    """
    if headLess == True:
        # Ensure the window doesnt pop up, aka "headless"    
        display = Display(visible=0, size=(800, 600))
        display.start()
    
    if proxyPort is not None:
        proxy = Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': proxyPort,
        'ftpProxy': proxyPort,
        'sslProxy': proxyPort,
        # per this article, this should be defaulted to value below
        # https://developer.mozilla.org/en-US/docs/No_Proxy_For_configuration
        'noProxy': 'localhost, 127.0.0.1' 
        })
        driver = webdriver.Firefox(proxy=proxy)
    else:
        driver = webdriver.Firefox()
    
    return driver
    
    
def getHTML(driver, url):
    """
    Gets the html for a given site and driver
    """
    driver.get(url)
    soup = BeautifulSoup(driver.page_source)
    return soup
        
    




if __name__ == "__main__":
    headLess = True
    proxyPort = '173.213.113.111:7808'
    proxyPort = '109.227.124.27:8080'
    #driver = createDriver(proxyPort, headLess = False)
    driver = createDriver(headLess = True)
    url = 'http://ip-addr.es'
    html = getHTML(driver, url)
    print html.prettify()