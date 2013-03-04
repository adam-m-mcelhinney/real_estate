from data_import import import_clean
from zillow import search_prop
from zillow_2 import get_info
import time
import random

# Get the file
file='C:/Users/Adam/Documents/GitHub/real_estate/test_data.csv'
nav_root='http://www.zillow.com/'
search_root='http://www.zillow.com/homes/'

data=import_clean(file)
#data=data[:5]

# loop through the addresses and get the search urls
search=[]
for i in range(len(data)):
    #print i
    # Dont hit the server too fast
    #pause=random.random()+random.randint(0,1)
    #time.sleep(pause)
    
    search.append(search_prop(nav_root,search_root,data[i]))

# Name the columns in the output file
out=[['Address','Baths','Beds','Zestimate','Rental Estimate','Year Built','Lot Size','House Size','Property URL']]
# loop through the search urls and get the variables

for i in range(len(data)):
    # Dont hit the server too fast
    #pause=random.random()+random.randint(0,1)
    #time.sleep(pause)
    #print search[i]
    try:
        row=get_info(search[i])
        row.insert(0,data[i])
        
    except:
        row=[data[i],search[i]]
        out.append(row)


import csv
with open('C:/Users/Adam/Documents/GitHub/real_estate/out_data.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(out)
        


    

