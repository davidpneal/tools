
import yaml


if __name__ == '__main__':

    try:
        with open ('tickers.yaml', 'r') as file:
            tickers = yaml.safe_load(file)
    except IOError:
        print ("Unable to read the ticker data from tickers.yaml")
        exit(1)

    keys = tickers.keys()

    for key in keys:
        print(key, tickers[key])

    #print(type(tickers))