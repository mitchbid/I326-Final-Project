""" Mitchell Biderberg, Nasir Zaidi, Nkunim Antwi, Nur Mulugeta"""
from argparse import ArgumentParser

"""Final Project: Resturant Ratings Generator  """

class Yelp_Data: 
    """ A class that reads datafile and iterates through
    data types """
    def __init__(self,filename,url):
        """ 
        (Nur) a function to initialize our variables and reads in our data,
        creates two dataframes
            Args:
                Url (rss) - url path containing our dataset
                Side effects: 
                    Sets attribute for Yelp Data dictionary
        """
        self.Yelp_Dict = {}
        
    def df_merge(self):
        """
        (Nasir) A function that reads in aggr
            Args: 
                Filename - refrence to file being utilized 
            Returns:
                data_yelp (dict) - new dictionary with matched key value pairs
        """   
        #data_yelp = {}
        #for i in Yelp_Data:
            #if x in yelp_data:
                #x.append(data_yelp)
                
    def input_rating(self):
        """
        (Nasir) A function that takes input from the user based off specifications set
        then validates each of these values (calling input_parser after each input)
            Args:
                Location (list) - input varible taking in the user's location prefrence
                Cuisine (list) - input varibale taking in the users cuisine prefrences
                Price (list) - input variable taking in the users price range prefence  
                
        """
    
    def input_parser():
        """
        (Nkunim) Function that takes the input values recieved from the user, parses through each list 
        and validates each value (location,Price, Cuisine) ---> Each has its own function
            Args:
                arglist (list of str): list of arguments from the command line.
            Returns:
                            (tuple) - of all specifications
                input_yelp (df) - dictionary with user's input values for Location(key), Cuisine(key), Price(key)
        """
    def df_match():
        """
        Function that takes the key value pairs from data_yelp and input_yelp and compares them, searching for any and all matches
            Returns:
                match_list (str) - list of data matches between the data_yelp and input_yelp dictionaries 
        """ 
        
    def data_visualizer():
        """
        Using Pandas print out the df produced in df_match()
        """
        
        
def main():
    """
    (Mitch) Instansiate class and invoke methods listed above
    """"
    
def parse_args(arglist):
    """
    (Nkunim) Parses command line arguments 
    """
    parser = ArgumentParser()
    parser.add_argument("filename", help="the name of the file that has the Yelp data")
    return parser.parse_args(arglist)
if __name__ == "__main__":
