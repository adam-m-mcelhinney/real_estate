import requests
import urllib2
from bs4 import BeautifulSoup
import time

# Using requests module
proxy_dict = {"http":"http://192.30.86.148:3128"}
url = 'https://check.torproject.org/'
response = requests.get(url, proxies=(proxy_dict))
html = response.content
soup = BeautifulSoup(html)
ip = str(soup.b.text)
print 'your ip is: \n' + str(ip)
time.sleep(5)
