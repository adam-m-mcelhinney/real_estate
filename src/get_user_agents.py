# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:08:40 2013

@author: amcelhinney

Get popular user agents and verify a user agent string
"""
import urllib2
from bs4 import BeautifulSoup

def verify_user_agent(test_user_agent):
    """
    Verifies that a user agent provided to the function
    is correctly being seen by a website.
    Returns a tuple with:
        1. a boolean indicating whether or not the provided agent matches
           the website. True -> match, False -> no match
        2. the user agent actually being seen by the website
        3. the user agent that was tested

    """
    
    url = 'http://www.whatsmyuseragent.com/'
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', test_user_agent)]
    urllib2.install_opener(opener)
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html)
    
    # Get the user agent
    try:
        actual_agent = soup.span.text.encode('ascii', 'ignore')
    except:
        print "Error finding or coding the user agent"
        return None
    
    if actual_agent == test_user_agent:
        return True, actual_agent, test_user_agent
    else: 
        return False, actual_agent, test_user_agent
    
 def get_user_agents():
    """
    Gets  a list of the most popular user agents

    """
    url = 'http://techblog.willshouse.com/2012/01/03/most-common-user-agents/'
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)    
    # Get all user agents 
    user_agent_str_long = soup.find_all('textarea')[0].text
    user_agent_table_raw = user_agent_str_long.split('\n')    
    user_agent_table = []
    for i in user_agent_table_raw:
        # Check for throw-away records, such as "u''"
        # I arbitrarily defined with a length cutoff
        if len(i)< 10:
            pass
        else:
            row = i.encode('ascii', 'ignore').strip()
            user_agent_table.append(row)
    return user_agent_table


def get_user_agents_old():
    """
    NO LONGER USED!
    Gets  a list of the most popular user agents
    Cleans out search engine related user agents using the 
    agent_is_search function
    """
    url = 'http://www.whatsmyuseragent.com/CommonUserAgents'
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)    
    # Get all user agents
    table_raw = soup.find_all('td')    
    # Get the text only
    user_agents = []
    for i in table_raw:
        row = i.text.encode('ascii', 'ignore').strip()
        user_agents.append(row)
    return user_agents
    

if __name__ == "__main__":
    
    # Test case 1
    user_agent_str= 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36'
    print verify_user_agent(user_agent_str)
    
    # Test Case 2
    user_agents = get_user_agents()
    for i in user_agents:
        print verify_user_agent(i)
        