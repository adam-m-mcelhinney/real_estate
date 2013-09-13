### Test using a proxy to visit a site
# Also check out URLLIB2: http://docs.python.org/2/library/urllib2.html#examples
# list of proxies: http://www.hidemyass.com/proxy-list/
import csv
import urllib
import urllib2
from bs4 import BeautifulSoup



proxies = {'https': '2.135.237.186:9090'}
search_url='http://docs.python.org/2/library/urllib.html'
search_url="https://check.torproject.org/"
#site=urllib2.urlopen(search_url, proxies=proxies)
site=urllib.urlopen(search_url, proxies=proxies)
soup=BeautifulSoup(site.read())

print soup.prettify


# File path to proxy list
#proxy_file='C:\Users\Adam\Documents\GitHub\real_estate\proxies.csv'
proxy_file='C:/Users/Adam/Documents/GitHub/real_estate/proxies.csv'
import csv
with open(proxy_file, 'rb') as csvfile:
	proxy = csv.reader(csvfile, delimiter=' ', quotechar='|')
	d=[]
	i=0
	for row in proxy:
            d.append(row)



def proxy_dict(proxy_list):
    """
    Creates the dictionary in the required form for the urlopener
    Needs to be in form:
    {'https': '2.135.237.186:9090'}
    """
    proxies=[]
    for i in range(len(proxy_list)):
        e = proxy_list[i][0].split(',')
        #proxy=[e[0].lower(),e[1]+':'+e[2]]
        proxy={e[0].lower(),e[1]+':'+e[2]}
        proxies.append(proxy)
    return proxies


# This is how I need to do it!!!

import urllib2
proxy= urllib2.ProxyHandler({'https': '2.135.237.186:9090'})
opener = urllib2.build_opener(proxy)
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib2.install_opener(opener)
y=opener.open(search_url)
# What happens if proxy is bad?
search_url = "https://check.torproject.org/"
proxy_site = {'https':'186.93.164.129:8080'}
proxy= urllib2.ProxyHandler(proxy_site)
opener = urllib2.build_opener(proxy)
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib2.install_opener(opener)
y = opener.open(search_url)
soup = BeautifulSoup(y.read())
print soup.prettify


# This way seems to work!
import requests
url = "http://www.whatsmyip.us/"
r = requests.get(url, proxies=({"http":"http://200.52.172.115:8080"}))
thedata = r.content
print thedata



