import requests
import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.proxy import *
from pyvirtualdisplay import Display

#Code to verify my IP address
# http://chisflorinel.blogspot.com/2008/10/fetch-urls-anonymously-with-python.html
# Unix install instructions
# https://www.torproject.org/docs/debian.html.en#ubuntu

def check_ip_tor(proxy_ip_port = None):
    """
    Goes to the site, using selenium!
    Outputs:
    1. Your ip address, string
    2. Are you using tor, boolean
    """
    # Go to the site and read it
    url = 'https://check.torproject.org/'
    
    # Ensure the window doesnt pop up, aka "headless"    
    display = Display(visible=0, size=(800, 600))
    display.start()

    if proxy_ip_port is not None:
        
        proxy = Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': proxy_ip_port,
        'ftpProxy': proxy_ip_port,
        'sslProxy': proxy_ip_port,
        'noProxy': '' # set this value as desired
        })
        # TODO: try phantomJS instead, supposedly faster
        driver = webdriver.Firefox(proxy=proxy)
        driver.get(url)



    else:
        driver = webdriver.Firefox()
        driver.get(url)

    soup = BeautifulSoup(driver.page_source)
    driver.quit()

    # Grab the ip, which is bolded
    ip = str(soup.b.text)

    # Check if you are using tor
    tor_string = "Sorry. You are not using Tor."
    tor_site = soup.img
    tor_flg = tor_string in tor_site
    return ip, tor_flg

def check_ip_tor_requests(proxy_dict = None):
    """
    Goes to the site, using the python requests module
    Outputs:
    1. Your ip address, string
    2. Are you using tor, boolean
    """
    # Go to the site and read it
    url = 'https://check.torproject.org/'

    if proxy_dict is not None:

        #prox = urllib2.ProxyHandler(proxy_dict)
        #opener = urllib2.build_opener(prox, urllib2.HTTPHandler(debuglevel=1))
        #urllib2.install_opener(opener)
        #response = opener.open(url)
        #reponse = requests.get(url, proxies=({"http":"http://200.52.172.115:8080"}))
        response = requests.get(url, proxies=(proxy_dict))
    else:
        #response = urllib2.urlopen(url)
        response = requests.get(url)

    html = response.content
    soup = BeautifulSoup(html)

    # Grab the ip, which is bolded
    ip = str(soup.b.text)

    # Check if you are using tor
    tor_string = "Sorry. You are not using Tor."
    tor_site = soup.img
    tor_flg = tor_string in tor_site
    return ip, tor_flg
    
def verify_ip_simple(proxy_dict = None):
    """
    Verifies IP on another site
    """
    url = 'http://ip-addr.es//'

    if proxy_dict is not None:

        response = requests.get(url, proxies=(proxy_dict))
    else:

        response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html)
    # Grab the ip, which is bolded
    ip = str(soup.text).replace('\n', '')
    return ip
    

if __name__ == "__main__":
    '''
    print check_ip_tor()
    #proxy_dict = {"http":"http://127.0.0.1:8118"}
    proxy_dict = {"http":"http://200.52.172.115:8080"}
    print check_ip_tor_requests(proxy_dict)
    '''


    
    # Test selenium
    proxy_ip_port = '173.213.113.111:7808'
    print check_ip_tor(proxy_ip_port)
    
    

