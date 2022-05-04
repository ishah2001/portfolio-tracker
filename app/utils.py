# file that defines all the functions of yfinance

import pandas as pd 
import yfinance as yf
from yahoofinancials import YahooFinancials
import datetime # used to get a certain time


def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]


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


def get_DifferenceInDay(userInputDate):
   today = date.today()
   d1 = today.strftime("%d/%m/%Y")
   todayNew= d1.split('/')
   todayYear= int(todayNew[2])
   todayMonth= int(todayNew[1])
   todayDay= int(todayNew[0])
 
   dateList= userInputDate
   token= dateList.split('/')
   year= int(token[2])
   month= int(token[0])
   day= int(token[1])
   f_date = date(year, month, day)
   l_date = date(todayYear, todayMonth, todayDay)
   delta = l_date - f_date
 
   numberOfWeeks= (delta.days/ 7) * 2
 
   differenceInDays= int(delta.days - numberOfWeeks)
   return (str(differenceInDays))
 
def get_Purchased_price(symbol,userInputDate):
 
   ticker= yf.Ticker(symbol)
   date= get_DifferenceInDay(userInputDate) + 'd'
   todays_data = ticker.history(period=date)
   return todays_data['Close'][0]

def get_news(ticker):
	ticker = yf.Ticker(ticker)
	news = []
	news = ticker.news
	headlines = []

	for i in range(len(news)):
		headlines.append(news[i]["title"])

	return(headlines)


print(get_news())





