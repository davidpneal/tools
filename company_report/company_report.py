# Tool to auto generate the company report

import requests
import yaml
from secret import alphavantage_api_key
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


    def write_snapshot_yaml(self):
        pass
        # write the data to tickers_snapshot_YYYYMMDD.yaml

    
    def update(self):
        pass
        # Calls API and requests the following data:   #### Is this a separate class?
            # Fields to map ~ lookup:
            # company_name: (if None)
            # price_last_close: 
            # price_1mo_ago:
            # price_52wk_high:
            # price_52wk_low:
            # last_earnings:
            # last_earnings_date:

            # report_last_run:
            # Might need a time series for the past 3 months - generate the graph with this data


        # Data is written to tickers dict - need to add the key/pair for most itemss
        # Set the report_last_run var to current timedate

        # Need logic to catch if the lookups failed
        # Also need some rate limiting since API is restricted to 5 calls/min
        # Might not need separate calls for all of the above items, the API returns collections of data


    def generate_docx(self):
        pass
        # outputs the reports, one docx per report
        # How does the template work?



if __name__ == '__main__':

    #Instantiate the report class
    cr = report()

    cr.update()
    cr.generate_docx()
    cr.write_snapshot_yaml()

