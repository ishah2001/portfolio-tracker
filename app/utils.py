# file that defines all the functions of yfinance

import pandas as pd 
import yfinance as yf
from yahoofinancials import YahooFinancials
import datetime # used to get a certain time


def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]

'''
def get_Purchased_price(symbol):
    ticker= yf.Ticker(symbol)
    date= "1" & "d"
    todays_data = ticker.history(period=date)

    print(date)
    return todays_data['Close'][0]

get_Purchased_price("AAPL")

'''