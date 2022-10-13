
import requests
from secret import alphavantage_api_key
#import alpha_vantage

#'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=alphavantage_api_key'


ticker = 'AAPL'

base_url = 'https://www.alphavantage.co/query?'
api_key = '&apikey=alphavantage_api_key'

symbol = '&symbol=' + ticker


#############################################################

# Earnings API
# Most recent quarterly earnings: data['quarterlyEarnings'][0]
# {'fiscalDateEnding': '2022-06-30', 
# 'reportedDate': '2022-07-28', 
# 'reportedEPS': '1.2', 
# 'estimatedEPS': '1.16', 
# 'surprise': '0.04', 
# 'surprisePercentage': '3.4483'}

# if True:
if False:
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
# 52WeekHigh: 182.19
# 52WeekLow: 128.86

# LatestQuarter: 2022-06-30
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
    print(data.keys())

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

    # print(data.keys())
    print("values")
    print(data.values())


    index_vals = list(data[key].values()) # Save the dict values into a list

    print(index_vals[4]) # Closing price for the day - prce_last_close:

    #print(r.status_code)



#############################################################


# Data: Timeseries, high, low, volume per 5 min time slice

if True:
# if False:  ## DOES NOT WORK CURRENTLY
    function = 'function=TIME_SERIES_INTRADAY&interval=15min&outputsize=full'

    # This series only goes back 1-2mo, prob need to switch to extended api
    # Note that that API is queried 1 month at a time, need 3 calls
    # Need to set adjusted to true

    # Can probably get the 1mo ago price from here too

    r = requests.get(base_url + function + symbol + api_key)
    data = r.json()

    # print(data)
    print(data.keys())
    # print(data['Meta Data'])  ### Note -- times are EST
    # print(data['Time Series (5min)'])
    # print('\n')
    # print(data['Time Series (5min)'].values()) # Returns a set of dicts, the keys for these are timestamps
    # print('\n')

    series_list = list(data['Time Series (15min)'].values()) #Convert the values of the timeseries (dicts) to a list
    
    # print(series_list[0])
    # print(series_list[0]['4. close'])

    price_series = [val['4. close'] for val in series_list] # Extract the closing price from each data point
    print(len(price_series))

    # for key in data.keys():
    #     print(key)
    #     print(data.keys())
    

    # Testing, NOTE - currently, need to rename secrets.py because it causes a library to not load
    import matplotlib.pyplot as plt

    # price_series.plot() ## Plot needs more data -- what inputs can this task?
    plt.plot(price_series)
    #plt.title('Intraday Times Series (5 min)')
    plt.show()

    # import matplotlib.pyplot as plt
    # plt.plot([1, 2, 3, 4])
    # plt.ylabel('some numbers')
    # plt.show()


#############################################################



# if True:
if False:
    function = 'function=NEWS_SENTIMENT'

    r = requests.get(base_url + function + symbol + api_key)
    data = r.json()

    print(data)
    print(data.keys())

