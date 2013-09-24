#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Adam
#
# Created:     22/09/2013
# Copyright:   (c) Adam 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def get_proxies(filePath):
    """
    Gets the proxies from the txt file located at the specified file path
    """
    openfile = open(filePath, 'r')
    t = openfile.read().split('\n')
    t = [i.replace('\r','') for i in t] # Get rid of formatting characters
    # Last element is just an empty string, so remove that
    return t[0:len(t)-1]

if __name__ == '__main__':
    filePath = 'C:\Users\Adam\Downloads\_reliable_list.txt'
    paths = get_proxies(filePath)
