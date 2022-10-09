# Tool to auto generate the company report

import requests
import yaml
from secret import alphavantage_api_key
#import alpha_vantage



class report:

    def __init__(self):
        self.read_yaml()


    def __str__(self):
        output = ""
        for ticker in self._tickers.keys():
            output += ticker + '\n'
            for key in self._tickers[ticker]:
                output += key + ': ' + str(self._tickers[ticker][key]) + '\n'
            output += '\n'
        return(output)


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
        # Calls API and requests the following data
        # Need logic to catch if the lookups failed

        # Loop through the tickers and add additional data
        for ticker in self._tickers.keys():
            self._tickers[ticker]['report_last_run'] = "10/8/2022"

            # company_name: (if None)
            # price_last_close: 
            # price_1mo_ago:
            # price_52wk_high:
            # price_52wk_low:
            # last_earnings:
            # last_earnings_date:

  
            # Might need a time series for the past 3 months - generate the graph with this data
            # Pause for 1 minute since API is restricted to 5 calls/min


    def generate_docx(self):
        pass
        # outputs the reports, one docx per report
        # How does the template work?


if __name__ == '__main__':

    #Instantiate the report class
    cr = report()

    cr.update()

    print(cr)

    # cr.generate_docx()
    # cr.write_snapshot_yaml()

