# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 18:40:17 2013

@author: amcelhinney

Description:
"""
import sys
sys.path.append('/home/amcelhinney/Documents/github_personal/real_estate/src')
sys.path.append('/home/amcelhinney/Documents/github_personal/real_estate/src/selenium')
from seleniumHelpers import getHTML, createDriver

def verifyIP(driver, siteNum = 0):
    """
    Verifies the IP Address using a given site siteNum
    """
    if siteNum == 0:
        url = 'http://ip-addr.es' #significantly faster
        html = getHTML(driver, url)
         #IP is wrapped in this tag
        ip = str(html.pre).replace('<pre>','').replace('</pre>','')\
        .replace('\n','')
        
    elif siteNum == 1:
        url = 'https://check.torproject.org/'
        html = getHTML(driver, url)
        # Grab the ip, which is bolded
        ip = str(html.b.text)
    else:
        raise BaseException, "Improper siteNum specified"
    
    return ip
    
        


if __name__ == "__main__":
    headLess = True
    proxyPort = '173.213.113.111:7808'
    driver = createDriver(proxyPort, headLess)
    ip1 = verifyIP(driver, siteNum = 0)
    ip2 = verifyIP(driver, siteNum = 1)
    
    # Should throw exception
    verifyIP(driver, siteNum = 999)
