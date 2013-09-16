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


class identity:
    
    
    def __init__(self):
      
      # User agents
      self.user_agents_table = None    
      self.current_user_agent = None
      
      # Proxies
      self.proxy_table = None
      self.current_proxy = None

    
    def populate_user_agents(self):
        self.user_agents_table = get_user_agents()
        
    def change_user_agent(self):
        assert self.user_agents_table is not None, "Must call " \
        "populate_user_agents prior to running this method."
        self.current_user_agent = choice(self.user_agents_table)
        
        
    






if __name__ == '__main__':
    
    i = identity()
    i.populate_user_agents()
    i.change_user_agent()
    
    
    
    