from bs4 import BeautifulSoup
import urllib2
import urlparse
import re
#from BeautifulSoup import BeautifulSoup

#property_url='http://www.zillow.com/homedetails/1602-2nd-St-Winthrop-Harbor-IL-60096/4747609_zpid/'
#property_url='http://www.zillow.com/homedetails/109-Chesapeake-Bay-Winthrop-Harbor-IL-60096/4747751_zpid/'
# test a foreclosure
property_url='http://www.zillow.com/homedetails/1021-Mary-Ave-Winthrop-Harbor-IL-60096/4749534_zpid/'

site=urllib2.urlopen(property_url)

# Read the html from the site and turn it into a soup object
soup=BeautifulSoup(site.read())
# Sort of works
#print soup.find_all('meta')
# Does not work
#print soup.find_all('itemprop')
# Does not work
#print soup.find_all('meta content')


content=str(soup.find_all('meta'))
#reg=re.compile('zestimate')
reg=re.compile('zestimate',re.IGNORECASE)
e=re.findall(reg, content)


bath=re.compile('<meta content="." property="zillow_fb:baths"/>',re.IGNORECASE)
beds=re.compile('<meta content="." property="zillow_fb:beds"/>',re.IGNORECASE)
e=re.findall(bath, content)
f=re.findall(beds, content)

print e
print f



content=str(soup.find_all('span class=\"prop-facts-value\"'))
# This pulls the zestimate and previous sale prices
soup.find_all('td')



# works
year=re.compile('Year Built:</strong><span class="prop-facts-value">[0-9]*<',re.IGNORECASE)
g=re.findall(year, str(soup))
print g

#house=re.compile('<span class="prop-facts-value">840 sq ft<',re.IGNORECASE)
# Note the commas!
house=re.compile('<span class="prop-facts-value">[0-9,]* sq ft<',re.IGNORECASE)
h=re.findall(house, str(soup))
print h

#lot=re.compile('Lot:</strong><span class="prop-facts-value">14,900 sq ft<',re.IGNORECASE)
lot=re.compile('Lot:</strong><span class="prop-facts-value">[0-9,]* sq ft<',re.IGNORECASE)
i=re.findall(lot, str(soup))
print i
