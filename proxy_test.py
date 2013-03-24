### Test using a proxy to visit a site
# Also check out URLLIB2: http://docs.python.org/2/library/urllib2.html#examples
# list of proxies: http://www.hidemyass.com/proxy-list/
# Should use Tor. Use this site to check fi youre on TOR: https://check.torproject.org/


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
        proxy=[e[0].lower(),e[1]+':'+e[2]]
        proxies.append(proxy)
    return proxies


# This is how I need to do it!!!

import urllib2
#opener = urllib2.build_opener()
#proxy= urllib2.ProxyHandler({'https': 'http://127.0.0.1:8080/'})
proxy= urllib2.ProxyHandler({'https': '2.135.237.186:9090'})

opener = urllib2.build_opener(proxy)
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib2.install_opener(opener)
y=opener.open(search_url)

# What happens if proxy is bad?

proxy= urllib2.ProxyHandler({'https': '2.135.237.186:444444444'})
opener = urllib2.build_opener(proxy)
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib2.install_opener(opener)
y=opener.open(search_url)
        
        
        
        
    
# Tor
# http://stackoverflow.com/questions/9870182/running-python-script-with-tor?rq=1
import sys
sys.path.append("C:\\Python27\\Scripts")
import socks
import socket
#socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 8080)
socket.socket = socks.socksocket
import urllib2
try:
    print(urllib2.urlopen("https://check.torproject.org/").read())
except urllib2.unwrap:
    print
"""
URLError: <urlopen error [Errno 10061] No connection could be made because the target machine actively refused it>
Could be UIC's network
"""
	 
proxy_support = urllib2.ProxyHandler({"https" : "49.212.129.130:3128"})
#proxy_support = urllib2.ProxyHandler({"http" : "127.0.0.1:8118"})
proxy_support = urllib2.ProxyHandler({"http" : "127.0.0.1:8123"})
opener = urllib2.build_opener(proxy_support)
urllib2.install_opener(opener)
print(opener.open("https://check.torproject.org/").read())
print(opener.open("http://www.whatsmyip.us/").read())

proxy = "http://localhost:8118/"
proxy_handler = urllib2.ProxyHandler({'http': proxy})
opener = urllib2.build_opener(proxy_handler)

