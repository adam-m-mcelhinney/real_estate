import urllib2
from bs4 import BeautifulSoup

##class find_proxies:
##    """
##    Finds proxies that are currently active. Goes to website
##    http://hidemyass.com/, selects proxies that are http or https, that
##    are annoymity level medium or high and that have fast connection speeds.
##    """
## NOT WORKING!



if __name__ == '__main__':
    # Note the search parameters are coded in the url
    url = 'http://hidemyass.com/proxy-list/search-226724'
    opener = urllib2.build_opener()
    urllib2.install_opener(opener)
    y=opener.open(url)
    soup = BeautifulSoup(y.read())
    print soup.prettify
    soup.find_all('GftH')
    # The table is named "listtalbe"
    table = soup.find(lambda tag: tag.name=='table' and tag.has_key('id')
    and tag['id']=="listtable")
    rows = table.find_all(lambda tag: tag.name=='tr')
    # First element stored as <span class="24">190</span>
    <span class="jDaS">153</span>
    <span style="display: inline">97</span>
    <span style="display: inline">172</span>

