from bs4 import BeautifulSoup
import urllib2
import urlparse
import re
#from BeautifulSoup import BeautifulSoup


def parser(name,site,big_regex,little_regex):
    """
    This function parses the data by first using the big regex expression to find the tag, then extracting via the little regex expression.
    1. name: just a name of the item you're looking for: eg. "beds"
    2. site: the text of the site
    3. big_regex: the string of the regex to extract the tag
    4. little_regex: the string of the regex to extract the actual piece of info
    """
    try:
        regex=re.compile(big_regex,re.IGNORECASE)
    except:
        return 'invalid_big_regex'

    try:
        raw=re.findall(regex, site)
        # Ths is broke for now for the house size piece
        #if len(raw)>1:
        #    return 'warning: multiple values for '+name+' found!'
    except:
        return 'raw_failed!'

    try:
        fact=re.findall(little_regex, raw[0],re.IGNORECASE)
    except:
        return 'value for '+name+' not found!'

    return fact[0]
        
    
    



def get_info(property_url):
    """
    Gets the property info from the page provided in the property_url
    Notes:
    1. Missing values may show up as zeros!
    2. Bed and bathrooms are limited to single digits

    """
    site=urllib2.urlopen(property_url)

    # Read the html from the site and turn it into a soup object
    soup=BeautifulSoup(site.read())
    site=str(soup)

    bath=parser('baths',site,'<meta content="." property="zillow_fb:baths"/>','[0-9]')
    beds=parser('beds',site,'<meta content="." property="zillow_fb:beds"/>','[0-9]')
    zest=parser('zestimate',site,'<td class="zestimate">[0-9$,]+</td>','\$[0-9,]+')
    rent=parser('rent',site,'<td class="zestimate">[0-9$,]+/mo<','\$[0-9,]+')
    year=parser('year',site,'Year Built:</strong><span class="prop-facts-value">[0-9]+<','[0-9]+')
    lot=parser('lot',site,'Lot:</strong><span class="prop-facts-value">[0-9,]+ sq ft<','[0-9,]+')
    # THIS ONE IS WEIRD. IT PULLS BOTH THE LOT AND THE HOUSE SQ FT, BUT RELIES ON THE FACT THAT THE HOUSE SQ FT IS FIST
    house=parser('house',site,'</strong><span class="prop-facts-value">[0-9,]+ sq ft<','[0-9,]+')

##    bath=parser('baths',site,'<meta content="." property="zillow_fb:baths"/>','[0-9]')
##    beds=parser('beds',site,'<meta content="." property="zillow_fb:beds"/>','[0-9]')
##    zest=parser('zestimate',site,'<td class="zestimate">[0-9$,]*</td>','\$[0-9,]*')
##    rent=parser('rent',site,'<td class="zestimate">[0-9$,]*/mo<','\$[0-9,]*')
##    #year=parser('year',site,'Year Built:</strong><span class="prop-facts-value">[0-9]*<','[0-9]+')
##    year=parser('year',site,'Year Built:</strong><span class="prop-facts-value">[0-9]+<','[0-9]+')
##    lot=parser('lot',site,'Lot:</strong><span class="prop-facts-value">[0-9,]* sq ft<','[0-9,]+')
##    # THIS ONE IS WEIRD. IT PULLS BOTH THE LOT AND THE HOUSE SQ FT, BUT RELIES ON THE FACT THAT THE HOUSE SQ FT IS FIST
##    house=parser('house',site,'</strong><span class="prop-facts-value">[0-9,]* sq ft<','[0-9,]+')

    # Compile the results into a list
    #facts=[bath[0],beds[0],zest[0],rent[0],year[0],lot[0],house[0],property_url]
    facts=[bath,beds,zest,rent,year,lot,house,property_url]
    
    return facts

##    # Baths
##    bath_reg=re.compile('<meta content="." property="zillow_fb:baths"/>',re.IGNORECASE)
##    bath_raw=re.findall(bath_reg, site)
##    bath=re.findall('[0-9]', bath_raw[0],re.IGNORECASE)
##
##    # Beds
##    beds_reg=re.compile('<meta content="." property="zillow_fb:beds"/>',re.IGNORECASE)
##    beds_raw=re.findall(beds_reg, site)
##    beds=re.findall('[0-9]', beds_raw[0],re.IGNORECASE)
##
##    # Zestimate
##    zest_reg=re.compile('<td class="zestimate">[0-9$,]*</td>',re.IGNORECASE)
##    zest_raw=re.findall(zest_reg, site)
##    zest=re.findall('\$[0-9,]*', zest_raw[0],re.IGNORECASE)
##
##    # Rent Zestimate
##    rent_reg=re.compile('<td class="zestimate">[0-9$,]*/mo<',re.IGNORECASE)
##    rent_raw=re.findall(rent_reg, site)
##    rent=re.findall('\$[0-9,]*', rent_raw[0],re.IGNORECASE)
##
##    # Year Built
##    # Note the +
##    year_reg=re.compile('Year Built:</strong><span class="prop-facts-value">[0-9]*<',re.IGNORECASE)
##    year_raw=re.findall(year_reg, site)
##    year=re.findall('[0-9]+', year_raw[0],re.IGNORECASE)
##
##    # Lot Sq Ft
##    # Note the +
##    lot_reg=re.compile('Lot:</strong><span class="prop-facts-value">[0-9,]* sq ft<',re.IGNORECASE)
##    lot_raw=re.findall(lot_reg, site)
##    lot=re.findall('[0-9,]+', lot_raw[0],re.IGNORECASE)
##
##    # House Sq Ft
##    # Note the +
##    # THIS ONE IS WEIRD. IT PULLS BOTH THE LOT AND THE HOUSE SQ FT, BUT RELIES ON THE FACT THAT THE HOUSE SQ FT IS FIST
##    house_reg=re.compile('</strong><span class="prop-facts-value">[0-9,]* sq ft<',re.IGNORECASE)
##    house_raw=re.findall(house_reg, site)
##    house=re.findall('[0-9,]+', house_raw[0],re.IGNORECASE)   
##
##    # Compile the results into a list
##    facts=[bath[0],beds[0],zest[0],rent[0],year[0],lot[0],house[0],property_url]
##
##    return facts

    

if __name__ == "__main__":
    property_url='http://www.zillow.com/homedetails/1021-Mary-Ave-Winthrop-Harbor-IL-60096/4749534_zpid/'
    test1=get_info(property_url)
    print test1

    property_url='http://www.zillow.com/homedetails/1602-2nd-St-Winthrop-Harbor-IL-60096/4747609_zpid/'
    test2=get_info(property_url)
    print test2

    property_url='http://www.zillow.com/homedetails/10982-N-5th-St-Winthrop-Harbor-IL-60096/2124067832_zpid/'
    test3=get_info(property_url)
    print test3

