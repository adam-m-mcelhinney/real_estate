# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 18:59:31 2013

@author: amcelhinney

Description:
"""

import sys
sys.path.append('/home/amcelhinney/Documents/github_personal/real_estate/src')
sys.path.append('/home/amcelhinney/Documents/github_personal/real_estate/src/selenium')
from seleniumHelpers import getHTML, createDriver
from verifyIP import verifyIP
from pandas import DataFrame, read_csv
from random import choice, randint

from get_proxies import get_proxies

# Step 1, bring in the addresses
addresses = read_csv(addressFilePath)

# Step 2, add the required extra columns
addresses['html'] = None
addresses['searchURL'] = None
addresses['attempted'] = False
addresses['attemptDate'] = None

# Step 3, bring in the proxies
proxies = get_proxies(proxyFilePath)
proxies = [i.replace('\r', '') for i in proxies]

# Step 4, Grab one proxy and verify it
myIP = verifyIP(createDriver())
headLess = True
proxyPort = choice(proxies)
driver = createDriver(proxyPort, headLess)
ip = verifyIP(driver, siteNum = 0)
myIP != ip # Verifies the IP
proxyPort == ip # Verifies the IP

# Step 5, get some addresses that do not have html
mn_addresses = 6
mx_addresses = 24
numAddresses = randint(mn_addresses, mx_addresses)
searchAddresses = addresses.irow(range(numAddresses))

# Step 6
for i in range(numAddresses):
    










if __name__ == "__main__":
    
    #addressFilePath = 'C:/Users/Adam/Documents/NewLine_Addresses.csv'
    addressFilePath = '/home/amcelhinney/Documents/testData.csv'    
    
    proxyFilePath = '/home/amcelhinney/Documents/_full_list.txt'
    
    headLess = True
    proxyPort = '173.213.113.111:7808'
    driver = createDriver(proxyPort, headLess)
    ip1 = verifyIP(driver, siteNum = 0)
