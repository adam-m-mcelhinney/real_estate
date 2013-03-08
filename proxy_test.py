### Test using a proxy to visit a site
# Also check out URLLIB2: http://docs.python.org/2/library/urllib2.html#examples
# list of proxies: http://www.hidemyass.com/proxy-list/

import urllib
import urllib2
from bs4 import BeautifulSoup



proxies = {'https': '2.135.237.186:9090'}
search_url='http://docs.python.org/2/library/urllib.html'
#site=urllib2.urlopen(search_url, proxies=proxies)
site=urllib.urlopen(search_url, proxies=proxies)
soup=BeautifulSoup(site.read())

print soup.prettify



