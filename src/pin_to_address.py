# Gets the addresses for a given pin numberc
# http://blog.dispatched.ch/2009/03/15/webscraping-with-python-and-beautifulsoup/
# http://wolfprojects.altervista.org/changeua.php

import urllib
import urllib2
import string
import sys
from bs4 import BeautifulSoup
from random import choice


# text file storing the possible user-agents
# take list from here: http://techblog.willshouse.com/2012/01/03/most-common-user-agents/
user_agent_file='C:/Local Files/real_estate-master/real_estate-master/user_agents.txt'
out_file='C:/Local Files/real_estate-master/real_estate-master/test.html'
f=open(user_agent_file,'r').read()

# Split into a list, remove null
user_agents=f.split('\n')
user_agents=user_agents[0:len(user_agents)-1]

# Pick one randomly
#user_agent=choice(user_agents)
user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.152 Safari/537.22'

headers = { 'User-Agent' : user_agent }
site='http://www.dupageco.org/PropertyInfo/PropertyLookup.aspx'
# No hyphens in the pin
pin='0101100011'
#values={'ctl00$pageContent$ctl00$txtParcel' : pin}
values={'ctl00pageContent$ctl00txtParcel' : pin}
values='ctl00$pageContent$ctl00$txtParcel='+pin
data = urllib.urlencode(values)
request = urllib2.Request(site, data, headers)
response = urllib2.urlopen(request)
the_page = response.read()
# Save html
file = open(out_file,"wb")
file.writelines(the_page)
file.close()
pool = BeautifulSoup(the_page)
