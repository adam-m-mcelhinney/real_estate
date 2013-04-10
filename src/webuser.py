import csv


class webuser:
    """
    Creates a web identity by obtaining a proxy and a user
    """
    def __init__(self, proxy_file_path_name):
        
        self.proxy_file_path_name = proxy_file_path_name
        self.proxy_list = self.read_proxy_file(proxy_file_path_name)

    def read_proxy_file(self, path):
        """
        Reads the csv containing the list of proxies
        """
        with open(path, 'rb') as csvfile:
            proxy = csv.reader(csvfile, delimiter=' ', quotechar='|')
            d=[]
            i=0
            for row in proxy:
                d.append(row)
        return d

    def format_proxy_list(self,proxy_list):
        proxy_list_clean = []
        for i in proxy_list:
            
            
            
            
        
        
    






if __name__ == "__main__":
    proxy_file_path_name = 'C:/Users/Adam/Documents/GitHub/real_estate/data/proxies.csv'
    y = webuser(proxy_file_path_name)
    
    
