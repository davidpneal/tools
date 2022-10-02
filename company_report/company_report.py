# Tool to auto generate the company report

import requests
import yaml
from secrets import alphavantage_api_key
#import alpha_vantage



class report:

    def __init__(self):
        self.read_yaml()


    # def __str__(self):
        # Decide - is this the correct method to print the data to screeen?
        # output = loop over and show data in _tickers
        # return(output)


    def read_yaml(self):
        # Read in the ticker data we want to work with
        try:
            with open ('tickers.yaml', 'r') as file: # Might need to change this to rw later
                self._tickers = yaml.safe_load(file)
        except IOError:
            print ("Unable to read the ticker data from tickers.yaml")
            exit(1)


    def write_yaml(self):
        pass
        # write the data to tickers.yaml
    
    
    def update(self):
        pass
        # Calls API and requests the following data:   #### Is this a separate class?
            # Company Name (if needed)
            # Current Stock Price (last close)
            # Price from 1 month ago (do look this up each time)
            # 52 week high
            # 52 week low
            # latest earnings result, with date
            # Might need a time series for the past 3 months - genrate the graph with this data

        # Data is written to tickers dict
        # Set the report_last_run var to current timedate

        # Need logic to catch if the lookups failed
        # Also need some rate limiting since API is restricted to 5 calls/min


    def generate_docx(self):
        pass
        # outputs the reports, one docx per report
        # How does the template work?



if __name__ == '__main__':

    #Instantiate the report class
    cr = report()

    cr.update()
    cr.generate_docx()
    cr.write_yaml()

