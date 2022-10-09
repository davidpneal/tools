
import requests
from secret import alphavantage_api_key
#import alpha_vantage

#'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=alphavantage_api_key'


ticker = 'AAPL'

base_url = 'https://www.alphavantage.co/query?'
api_key = '&apikey=alphavantage_api_key'

symbol = '&symbol=' + ticker


# Still need:
# Price one month ago


#############################################################

# Earnings API
# Most recent quarterly earnings: data['quarterlyEarnings'][0]
# {'fiscalDateEnding': '2022-06-30', 
# 'reportedDate': '2022-07-28', 
# 'reportedEPS': '1.2', 
# 'estimatedEPS': '1.16', 
# 'surprise': '0.04', 
# 'surprisePercentage': '3.4483'}

if True:
# if False:
    function = 'function=EARNINGS'

    r = requests.get(base_url + function + symbol + api_key)
    data = r.json()

    # print(data.keys())
    # print(data.items())
    # print(data.values())

    latest_earnings = data['quarterlyEarnings'][0]

    # print(type(qearn))

    print(latest_earnings)
    # print('\n\n')
    # for item in qearn:
    #     print(item)


#############################################################

# Company Overview

# Name: Apple Inc
# LatestQuarter: 2022-06-30
# 52WeekHigh: 182.19
# 52WeekLow: 128.86
# DividendDate: 2022-08-11
# PERatio: 24.04
# EPS: 6.05

# PEGRatio: 2.62
# DividendPerShare: 0.89


# if True:
if False:
    function = 'function=OVERVIEW'

    r = requests.get(base_url + function + symbol + api_key)
    data = r.json()

    # print(data)
    # print(data.keys())

    for key in data.keys():
        print(key + ": " + data[key])
    
    #     #print(data[key].keys())
    #     print(data[key].values())



############################################################

# Data: Global Quote
# '01. symbol': 'AAPL', 
# '02. open': '145.8100', 
# '03. high': '147.5400',
# '04. low': '145.2200',
# '05. price': '145.4300',
# '06. volume': '68046940',
# '07. latest trading day': '2022-10-06', 
# '08. previous close': '146.4000', 
# '09. change': '-0.9700', 
# '10. change percent': '-0.6626%'

# if True:
if False:
    function = 'function=GLOBAL_QUOTE'

    r = requests.get(base_url + function + symbol + api_key)
    data = r.json()
    #print(data)

    print(list(data.keys()))
    print(data.items())

    #for key in data.keys():
    key = list(data.keys())[0] # Get the key name of the first (and only) dict entry
        # print(data[key])
    
        #print(data[key].keys())
        #print(data[key].values())

    # Get the closing price
    for k2 in data[key]:
        print(k2)
        print(data[key][k2])
        print('\n')


    index_vals = list(data[key].values()) # Save the dict values into a list

    print(index_vals[4]) # Closing price for the day - prce_last_close:

    #print(r.status_code)



#############################################################


# Data: Timeseries, high, low, volume per 5 min time slice

# if True:
if False:  ## DOES NOT WORK CURRENTLY
    function = 'function=TIME_SERIES_INTRADAY&interval=5min&outputsize=compact'

    r = requests.get(base_url + function + symbol + api_key)
    data = r.json()

    # print(data)
    print(data.keys)

    for key in data.keys():
        print(key)
        print(data.keys())
    
        #print(data[key].keys())
        # print(data[key].values())

        # for k2 in data[key]:
        #     print(k2)
        #     print(data[key][k2])
        #     print('\n')


        # Testing, NOTE - currently, need to rename secrets.py because it causes a library to not load
        import matplotlib.pyplot as plt

        #data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
        data.keys()['4. close'].plot()
        plt.title('Intraday Times Series for the MSFT stock (1 min)')
        plt.show()


#############################################################



# if True:
if False:
    function = 'function=NEWS_SENTIMENT'

    r = requests.get(base_url + function + symbol + api_key)
    data = r.json()

    print(data)
    print(data.keys())

