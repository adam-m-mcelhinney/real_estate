# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 16:46:47 2013

@author: amcelhinney

Provides walkscore.com an address and searches for the appropriate
walk-score page
"""
import urllib2
import re
from bs4 import BeautifulSoup

def search_ws(search_root, address):
    """
    Outputs the URL for the specific property's page on WalkScore
    TODO: modify to just return the full HTML of the site if found -- DONE
    """
    search_url=search_root+address.lower().replace(' ','-')
    try:
        # Open the url
        site=urllib2.urlopen(search_url)
    except:
        print 'Cannot open URL'
        return ('Cannot find URL', "NOT verified", None)
        
    # Read the html from the site and turn it into a soup object
    soup=BeautifulSoup(site.read())
    # Convert the site to text and make all lower case
    site_txt=str(soup).lower()
    
    # Verify the correct home was found
    # Split the elements
    add_split = address.split(' ')
    search_text = "".join([str(i) + '.*' for i in add_split])
    reg = re.compile(search_text.lower())
    exists=re.findall(reg,site_txt )

    # If it found nothing, then consider the url not verified
    if len(exists)==0:
        return (site.url, 'NOT verified', soup)
    else:
        return (site.url, 'Verified', soup)




if __name__ == "__main__":
    search_root='http://www.walkscore.com/score/'

    address='10982 N 5TH ST WINTHROP HARBOR'
    print search_ws(search_root,address)
    
    address='147 SHERIDAN RD WINTHROP HARBOR'
    print search_ws(search_root,address)
    
    address='1602 2ND ST WINTHROP HARBOR IL'
    print search_ws(search_root,address)
    
    address='200 W STATION ST BARRINGTON'
    j= search_ws(search_root,address)
    print j