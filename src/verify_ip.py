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
        
        urllib2.ProxyHandler(proxy_dict)
        opener = urllib2.build_opener(proxy_dict)
        response = opener.open(url)
    else:
        response = urllib2.urlopen(url)
        
    html = response.read()
    soup = BeautifulSoup(html)
    
    # Grab the ip, which is bolded
    ip = str(soup.b.text)
        
    # Check if you are using tor
    tor_string = "Sorry. You are not using Tor."
    tor_site = soup.img
    tor_flg = tor_string in tor_site
    return ip, tor_flg

if __name__ == "__main__":
    print check_ip_tor()
    proxy_dict = {"http":"http://127.0.0.1:8118"}
    print check_ip_tor(proxy_dict)
    
    