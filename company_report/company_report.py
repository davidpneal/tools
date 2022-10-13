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
            # Output data about the ticker
            for key in self._tickers[ticker]:
                output += key + ': ' + str(self._tickers[ticker][key]) + '\n'
            output += '\n'
        return(output)


    def read_yaml(self):
        # Read in the ticker data we want to work with
        try:
            with open ('tickers.yaml', 'r') as file:
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
        # Specifically - catch when the API sent a nak

        base_url = 'https://www.alphavantage.co/query?'
        api_key = '&apikey=alphavantage_api_key'
        

        # Loop through the tickers and add additional data
        for ticker in self._tickers.keys():
            symbol = '&symbol=' + ticker
            self._tickers[ticker]['report_last_run'] = "10/8/2022"   #### Update
            

            # Company Overview API
            function = 'function=OVERVIEW'
            r = requests.get(base_url + function + symbol + api_key)
            data = r.json()

            if self._tickers[ticker]['company_name'] is None:
                self._tickers[ticker]['company_name'] = data['Name']
            self._tickers[ticker]['price_52wk_high'] = data['52WeekHigh']
            self._tickers[ticker]['price_52wk_low'] = data['52WeekLow']
            

            # Earnings API
            function = 'function=EARNINGS'
            r = requests.get(base_url + function + symbol + api_key)
            data = r.json()

            latest_earnings = data['quarterlyEarnings'][0]
            self._tickers[ticker]['last_earnings_date'] = latest_earnings['fiscalDateEnding']
            self._tickers[ticker]['last_earnings_reported'] = latest_earnings['reportedEPS']        
            self._tickers[ticker]['last_earnings_consensus'] = latest_earnings['estimatedEPS']


            # Global Quote API
            function = 'function=GLOBAL_QUOTE'
            r = requests.get(base_url + function + symbol + api_key)
            data = r.json()
            
            self._tickers[ticker]['price_last_close'] = data['Global Quote']['05. price']


            #index_vals = list(data[key].values()) # Save the dict values into a list
            #print(index_vals[4]) # Closing price for the day - prce_last_close:

            #----
            # data = None

            # price_1mo_ago
  
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

