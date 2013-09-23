# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:03:09 2013

@author: amcelhinney

Description:
"""
import sys
sys.path.append('/home/amcelhinney/Documents/github_personal/real_estate/src')
from get_proxies import get_proxies
import pandas
from pandas import DataFrame
from pandas import pivot_table
from verify_ip import check_ip_tor
from verify_ip import verify_ip_simple


def verify_all_proxies(proxyFilePath, simple = False, mx_hits = 100):
    """
    Verifies all the proxies in the specified document
    """

    proxyList = get_proxies(proxyFilePath)
    proxyList = [i.replace('\r','') for i in proxyList]
    myIp = check_ip_tor()[0]
    results = DataFrame(columns = ['ip', 'actualIp', 'myIp', 'myIp_match_flg',
                                   'Ip_match_flg'])
                                   
    j = 0 
    for i in proxyList:
        if j > mx_hits:
            break
        try:
            # You have two options on which site to use
            if simple == False:
                actualIp = check_ip_tor({'http' : "http://" + i})[0]
            else:
                actualIp = verify_ip_simple({'http' : "http://" + i})
                
        except:
            actualIp = 'error'
        
        # Need to strip off the port
        testIp = i[0:i.find(':')]
        myIp_match_flg = actualIp == myIp
        Ip_match_flg = i == myIp
        row = DataFrame([(testIp, actualIp, myIp
        ,myIp_match_flg,Ip_match_flg)], columns = ['ip', 'actualIp', 'myIp'
        ,'myIp_match_flg', 'Ip_match_flg'])
        #print row
        results = results.append(row)
        j += 1
    
    return results
        
            
        
        
    



if __name__ == "__main__":
    proxyFilePath = '/home/amcelhinney/Documents/_full_list.txt'
    results = verify_all_proxies(proxyFilePath)
    print results.irow(0)
    print 'Pct IPs wrong:\n' + str(len(results['myIp_match_flg']==True)
    /len(results['myIp_match_flg'])*100)
    print hist(results['myIp_match_flg'])
    
    # Use the other site
    results = verify_all_proxies(proxyFilePath, simple = True)
    print results.irow(0)
    print 'Pct IPs wrong:\n' + str(len(results['myIp_match_flg']==True)
    /len(results['myIp_match_flg'])*100)
    print hist(results['myIp_match_flg'])