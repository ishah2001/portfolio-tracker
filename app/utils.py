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


def summary_stats(symbol):
    ticker= yf.Ticker(symbol)
    end_date = pd.Timestamp.today()
    start_date = end_date - pd.Timedelta(days=10*365) # Get past 10 years worth of data
    ticker_history=ticker.history(start=start_date, end=end_date)
    ticker_history = ticker_history.drop(columns=['Dividends', 'Stock Splits']) # Delete unnecessary columns
    # Create a new column as Close 200 days moving average
    ticker_history['Close_200ma'] = ticker_history['Close'].rolling(200).mean()
    # This is the summary statistics table
    ticker_history_summary = ticker_history.describe()
    return ticker_history_summary



def get_news(ticker):
	ticker = yf.Ticker(ticker)
	news = []
	news = ticker.news
	headlines = []

	for i in range(len(news)):
		headlines.append(news[i]["title"])

	return(headlines)


print(get_news())





