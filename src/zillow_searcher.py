#from BeautifulSoup import BeautifulSoup
#from BeautifulSoup import *
from bs4 import BeautifulSoup
import urllib2
import re

'''
Steps:
1. Take the address and format it into a url for zillow to search. 
   It should be of the form:
    http://www.zillow.com/homes/275-Thistle-Lake-Zurich-IL_rb/
    Note: Zip codes will screw it up

2. Parse the resulting page for something similar to the address in step on. 
   Then find the resulting url for that specific property.
   It should be of the form:
    http://www.zillow.com/homedetails/275-Thistle-Ln-Lake-Zurich-IL-60047/4871709_zpid/

3. Parse number 2 for all the elements that you want


'''

def search_prop(nav_root, search_root,address):
    """
    Searches Zillow and returns the url of the property specific page, if found
    1. nav_root: the root url that the specific property info is appended to. Found by selecting a specific property on Zillow. Example full url:
    http://www.zillow.com/homedetails/1602-2nd-St-Winthrop-Harbor-IL-60096/4747609_zpid/
    --> nav_root='http://www.zillow.com/'
    2. search_root: the root url that is used for the searches
    http://www.zillow.com/homes/275-Thistle-Lake-Zurich-IL_rb/
    --> search_root='http://www.zillow.com/homes/'
    3. Address: formatted as street number, street name, town, state. NO ZIP CODE!
    address='1602 2ND ST WINTHROP HARBOR IL'
    """
    # Prepare the url
    # TODO: Add functionality to pass in a "webuser" combination of
    # proxy and user agent. Ensure that the scraper uses those
    # to open the site.
    search_url=search_root+address.lower().replace(' ','-')+'_rb/'
    try:
        # Open the url
        site=urllib2.urlopen(search_url)
    except:
        print 'Cannot open URL'

    # Read the html from the site and turn it into a soup object
    soup=BeautifulSoup(site.read())

    # Convert the site to text and make all lower case
    site_txt=str(soup).lower()

    # Check to see if the home was found
    exists_reg=re.compile('no matching homes found')
    exists=re.findall(exists_reg,site_txt )
    #print exists
    if len(exists)>0:
        return('Not in Zillows db')

    # Sort of works
    regex=re.compile('homedetails.*_zpid');
    r=re.findall(regex,site_txt )
    #;re.search(regex,site_txt );
    try:
        start=r[0].index('homedetails')
        end=r[0].index('_zpid')+len('_zpid')
        y=r[0][start:end]
        url=nav_root+y.replace('\\','')
        return url

    except:
        #return 'Searcher Error-01:'+site_txt
        return 'Searcher Error-01:'

    


    
if __name__ == "__main__":
    nav_root='http://www.zillow.com/'
    search_root='http://www.zillow.com/homes/'
    #address='1602 2ND ST WINTHROP HARBOR IL'
    address='10982 N 5TH ST WINTHROP HARBOR'
    #address='147 SHERIDAN RD WINTHROP HARBOR'
    #address='1602 2ND '
    print search_prop(nav_root,search_root,address)
    
