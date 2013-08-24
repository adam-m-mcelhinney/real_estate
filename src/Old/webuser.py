import csv
from random import choice

class webuser:
    """
    Creates a web identity by obtaining a proxy and a user
    """
    def __init__(self, proxy_file_path_name, web_user_file_path_name):

        self.proxy_file_path_name = proxy_file_path_name
        self.proxy_list = self.read_file(proxy_file_path_name)
        self.proxies = self.proxy_string(self.proxy_list)
        self.user_agents = self.read_file(web_user_file_path_name)

    def read_file(self, path):
        """
        Reads the csv containing the list of proxies or webusers
        """
        with open(path, 'rb') as csvfile:
            proxy = csv.reader(csvfile, delimiter=' ', quotechar='|')
            d=[]
            i=0
            for row in proxy:
                d.append(row)
        return d

    def proxy_string(self, proxy_list):
        """
        Creates the string in the required form for the urlopener
        Needs to be in form:
        {'https': '2.135.237.186:9090'}
        """
        proxies=[]
        for i in range(len(proxy_list)):
            e = proxy_list[i][0].split(',')
            #proxy='{\'' + e[0].lower() + '\':\'' + e[1] + ':' + e[2] + '\'}'
            #proxy= e[0].lower() + ':' + e[1] + ':' + e[2]
            proxy= '\'' + e[0].lower() + '\':\'' + e[1] + ':' + e[2] + '\''

            proxies.append(proxy)
        return proxies

    def create_user(self):
        """
        Randomly select a proxy and user agent
        """
        proxy = choice(self.proxies)
        user_agent= choice(self.user_agents)
        return (proxy, user_agent)













if __name__ == "__main__":
    proxy_file_path_name='C:/Users/Adam/Documents/GitHub/real_estate/data/proxies.csv'
    web_user_file_path_name = 'C:/Users/Adam/Documents/GitHub/real_estate/data/user_agents.csv'
    y = webuser(proxy_file_path_name, web_user_file_path_name)
    #print y.proxy_list
    print y.proxies
    print y.user_agents


