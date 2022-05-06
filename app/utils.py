# file that defines all the functions of yfinance

import pandas as pd 
import yfinance as yf
from yahoofinancials import YahooFinancials
from datetime import date # used to get a certain time


def to_usd(value):
        return '${:,.2f}'.format(value)

def to_percent(value):
    return "{:.0%}".format(value)
    


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


def weekReturn(symbol):
   ticker1= yf.Ticker(symbol)
   week_data = ticker1.history(period='7d')
   weekStockPrice= week_data['Close'][0]
   totalPercentGain= (get_current_price(symbol) - weekStockPrice)/ weekStockPrice
   return totalPercentGain

def monthReturn(symbol):
   ticker2= yf.Ticker(symbol)
   month_data = ticker2.history(period='30d')
   monthStockPrice= month_data['Close'][0]
   totalPercentGain= (get_current_price(symbol) - monthStockPrice)/ monthStockPrice
   return totalPercentGain

def yearReturn(symbol):
   ticker3= yf.Ticker(symbol)
   year_data = ticker3.history(period='365d')
   yearStockPrice= year_data['Close'][0]
   totalPercentGain= (get_current_price(symbol) - yearStockPrice)/ yearStockPrice
   return totalPercentGain



def get_news(symbol):
	ticker = yf.Ticker(symbol)
	news = []
	news = ticker.news
	headlines = []
   

	#for i in range(len(news)):
	#	    headlines.append(news[i]["title"])
	return news



    

#print(get_recommendations("MSFT"))
















