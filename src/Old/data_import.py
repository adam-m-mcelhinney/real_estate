# Python script to read in the csv file, dedupe and format for searching



# Function to create a unique list
# Taken from: http://xenocoder.wordpress.com/2008/07/07/finding-unique-values-in-a-list-with-python/
def uniq(inlist): 
    # order preserving
    uniques = []
    for item in inlist:
        if item not in uniques:
            uniques.append(item)
    return uniques
        

def import_clean(file):
    """
    Function to import the data, put it in the right format and dedupe
    """
    import csv

    # store the address
    address=[]
    with open(file, 'rb') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            #print row
            address.append(row[2]+' '+row[3])
    # Skip the first row
    return uniq(address)[1:]


if __name__ == "__main__":
    # Include full file name and path
    file='C:/Users/Adam/Documents/GitHub/real_estate/test_data.csv'
    print import_clean(file)
