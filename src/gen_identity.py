# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 13:12:29 2013

@author: amcelhinney

Generates an "identity", which is a combo of user-agent, proxy
and behavior
"""
import sys
sys.path.append('/home/amcelhinney/Documents/github_personal/real_estate/src')
from get_user_agents import get_user_agents, verify_user_agent
from verify_ip import check_ip_tor
from random import choice
from get_proxies import get_proxies

class identity:


    def __init__(self):

      # User agents
      self.user_agents_table = None
      self.current_user_agent = None

      # Proxies
      self.proxy_table = None
      self.current_proxy = None

    # User agents
    def populate_user_agents(self):
        self.user_agents_table = get_user_agents()

    def change_user_agent(self):
        assert self.user_agents_table is not None, "Must call " \
        "populate_user_agents prior to running this method."
        self.current_user_agent = choice(self.user_agents_table)

    # Proxies
    def populate_proxies(self, filePath):
        self.proxy_table = get_proxies(filePath)

    def change_proxy(self):
        assert self.proxy_table is not None, "Must call " \
        "populate_proxies prior to running this method."
        self.current_proxy = choice(self.proxy_table)



    def change_identity(self):
        '''
        Helper function to change both proxy and user agent
        '''
        self.change_proxy()
        self.change_user_agent()



if __name__ == '__main__':

    i = identity()
    i.populate_user_agents()
    i.change_user_agent()
    print i.current_user_agent
    i.populate_proxies('C:\Users\Adam\Downloads\_reliable_list.txt')
    i.change_proxy()
    print i.current_proxy
    i.change_identity()
    print i.current_proxy
    print i.current_user_agent


