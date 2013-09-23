import requests
import urllib2
from bs4 import BeautifulSoup
#Code to verify my IP address
# http://chisflorinel.blogspot.com/2008/10/fetch-urls-anonymously-with-python.html
# Unix install instructions
# https://www.torproject.org/docs/debian.html.en#ubuntu

def check_ip_tor(proxy_dict = None):
    """
    Goes to the site
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
    print check_ip_tor()
    #proxy_dict = {"http":"http://127.0.0.1:8118"}
    proxy_dict = {"http":"http://200.52.172.115:8080"}
    print check_ip_tor(proxy_dict)

    # tried this thing too
    # http://www.youtube.com/watch?v=KDsmVH7eJCs
#
#    import socket
#    import socks
#    import httplib
#
#    def connectTor():
#        #socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9050, True)
#        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9051, True)
#        socket.socket = socks.socksocket
#
#    def main():
#        connectTor()
#        print ('Connected to Tor')
#        #conn = httplib.HTTPConnection("my-ip.heroku.com")
##        conn = httplib.HTTPConnection('https://check.torproject.org/')
#        conn = httplib.HTTPConnection('check.torproject.org')
#        conn.request("GET", "/")
#        response = conn.getresponse()
#        print response.read
#
#    main()
    import requests
    url = 'http://www.whatismyip.com/'
    #proxy_dict = {'http:':'http://86.111.144.194:3128'}
    proxy_dict = {'http:':'86.111.144.194:3128'}
    r = requests.get(url, proxies=proxy_dict)
    page = r.content
    print page.prettify()
    

