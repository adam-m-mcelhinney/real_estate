import csv
import time
import random
from pandas import read_csv
from gen_identity import identity
from zillow_searcher import search_prop
from verify_ip import check_ip_tor

class scraper(identity):


    def __init__(self, addressFilePath, proxyFilePath
    , trackingFrame = DataFrame, addressTable = None):
        
        identity.__init__(self)
        
        # File containing all of the addresses
        self.addressFilePath = addressFilePath
        self.addressTable = addressTable
        self.proxyFilePath = proxyFilePath
        self.trackingFrame = trackingFrame #Pandas DataFrame used to store everything
        self.myIP = check_ip_tor()[0]

        
    def importAddresses(self):
        """
        Import the addresses, output the table
        """
        self.addressTable = read_csv(self.addressFilePath, header = 0)
        
    def populateIdentities(self):
        """
        Populates the user agents and proxies from the identity class
        """
        self.populate_proxies(self.proxyFilePath)
        self.populate_user_agents()
        
    def createTrackingFrame(self):
        """
        Creates a new trackingFrame from the addressTable
        """
        # if no addressTable, need to have one
        if self.addressTable is None:
            self.importAddresses()
        
        t = self.addressTable
        t['html'] = None
        t['attempted'] = False
        self.trackingFrame = t
        
    def getHTML(self):
        """
        Gets one record
        Steps:
        1. Grab an address that does not have html
        2. Format the address accordingly
        3. Create an identity
        4. Verify the IP
        5. Verify the user agent
        6. Get the html
        """
        
        
    def scrape(self, mx_records = 5000):
        """
        Main scraping method. 
        Steps:
        1. Grab an address that does not have html
        2. Format the address accordingly
        3. Create an identity
        4. Verify the IP
        5. Verify the user agent
        6. Get the html
        """
        i = 0
        while True:
            
            # Decide to continue
            recordsNotAttempted = len(self.trackingFrame['attempted']==False)
            if i > mx_records: #Put a cap on max num records per session
                break
            if recordsNotAttempted == 0: #Ensure records exist
                break
            
            # Step 1
            record = self.trackingFrame[self.trackingFrame['attempted']==\
            False].irow(0)
            
            # Step 2
            address = (record['address_line1'] + ' ' + record['address_city'])\
            .title()
            
            # Step 3
            identity.change_identity()
            proxy = {"http":"http://" + identity.current_proxy}
            #proxy2 = {"https":"https://" + identity.current_proxy}
            user_agent = identity.current_user_agent
            
            # Step 4
            actualIP = check_ip_tor(proxy)[0]
            
            
            
        
        
        
        

        
if __name__ == '__main__':
    addressFilePath = 'C:/Users/Adam/Documents/NewLine_Addresses.csv'
    proxyFilePath = 'C:\Users\Adam\Downloads\ir.txt'
    s = scraper(addressFilePath, proxyFilePath)
    s.populateIdentities()
    print s.myIP
    s.createTrackingFrame()
    print s.trackingFrame


    

