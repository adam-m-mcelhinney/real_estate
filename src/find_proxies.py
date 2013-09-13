import urllib2
from bs4 import BeautifulSoup
import re

##class find_proxies:
##    """
##    Finds proxies that are currently active. Goes to website
##    http://hidemyass.com/, selects proxies that are http or https, that
##    are annoymity level medium or high and that have fast connection speeds.
##    """
## NOT WORKING!
def get_update_time(row_txt): 
    """
    Obtains the last update column
    """       
    rawstr = '.* hours and .* minutes'
    last_update_re = re.compile(rawstr,  re.IGNORECASE)
    result = re.findall(last_update_re, row_txt)
    return result
    
def get_port(row_txt):
    # Identify the string of text containing the port
    rawstr = r'</span></td>\n<td>\n.*</td>\n<td'
    port = re.compile(rawstr,  re.IGNORECASE)
    port_str = re.findall(port, row_txt)
    # Extract the specific port
    port_re = re.compile(r'[0-9]+', re.IGNORECASE)
    port = re.findall(port_re, port_str[0])
    return port
    
def get_ip(row_txt):
    rawstr = '   </style>\n   <span style="display: inline">\n.*\n  </span>\n </td>\n <td>'
    # Identify the block containing the IP
    ip_block_re = re.compile(rawstr,  re.IGNORECASE| re.DOTALL)
    ip_block = re.findall(ip_block_re, row_txt)
    # Get the first octect
    ip_first_str = '   </style>\n   <span style="display: inline">\n    [0-9]*\n   </span>\n   <span class="aqkO">\n    .\n   </span>\n'
    
    


if __name__ == '__main__':
    # Note the search parameters are coded in the url

    
    url = 'http://hidemyass.com/proxy-list/search-227955'
    opener = urllib2.build_opener()
    y=opener.open(url)
    soup = BeautifulSoup(y.read())
    all_rows = soup.findAll("tr")
    print all_rows[1].prettify()
    
    row_txt = str(all_rows)
    

        
    r = get_update_time(row_txt)
        
    
