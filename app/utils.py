# file that defines all the functions of yfinance

from calendar import week
import pandas as pd 
import yfinance as yf
from yahoofinancials import YahooFinancials
from datetime import date # used to get a certain time

# formats the current value into a number format
def to_usd(value):
        return '${:,.2f}'.format(value)

# definition that is called to format any value into percent
def to_percent(value):
    return "{:.0%}".format(value)
    

# Gathers the current price of a stock given the symbol
def get_current_price(symbol):
   #built in yahoo finance that creates an object that can later be used to get more info
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]

# definition that generates the difference in market days so that it will be passed to the 
# get_purchased_priced 
def get_DifferenceInDay(userInputDate):
   today = date.today()

   # Changes the format of todays date to be able to split
   d1 = today.strftime("%d/%m/%Y")
   #splits the list to extract string values
   todayNew= d1.split('/')
   # string value for yeat
   todayYear= int(todayNew[2])
   # string value for month
   todayMonth= int(todayNew[1])
   #string value for day
   todayDay= int(todayNew[0])
 
   #based on the object that the user passes it will assing this value to datelist
   dateList= userInputDate
   # splits the date list
   token= dateList.split('/')
   #follows the assigning value
   year= int(token[2])
   month= int(token[0])
   day= int(token[1])

   f_date = date(year, month, day)
   l_date = date(todayYear, todayMonth, todayDay)
   # calculates the difference in dates from the current to when the stock was purcahses
   delta = l_date - f_date
   # Adjust for market days as weekends doesnt count
   numberOfWeeks= (delta.days/ 7) * 2
   differenceInDays= int(delta.days - numberOfWeeks)
   return (str(differenceInDays))

#Calculates how much the stock cost at a certain date 
# both the symbol and the date will be extracted from the user input 
def get_Purchased_price(symbol,userInputDate):
 
   ticker= yf.Ticker(symbol)
   date= get_DifferenceInDay(userInputDate) + 'd'
   todays_data = ticker.history(period=date)
   return todays_data['Close'][0]

# Calculates the weekly returns of a stock by subtracting the week-old price and the current price
def weekReturn(symbol):
   ticker1= yf.Ticker(symbol)
   week_data = ticker1.history(period='7d')
   weekStockPrice= week_data['Close'][0]
   totalPercentGain= (get_current_price(symbol) - weekStockPrice)/ weekStockPrice
   # call the to_percent function to change the format
   formatTotalPercent = str(to_percent(totalPercentGain))
   #retruns a percent value 
   return formatTotalPercent
weekReturn("AAPL")

#Similar to the weekly return but returns the monthly returns
def monthReturn(symbol):
   ticker2= yf.Ticker(symbol)
   month_data = ticker2.history(period='30d')
   monthStockPrice= month_data['Close'][0]
   totalPercentGain= (get_current_price(symbol) - monthStockPrice)/ monthStockPrice
   formatTotalPercent = str(to_percent(totalPercentGain))
   return formatTotalPercent

# Finally returns the yearly returns 
def yearReturn(symbol):
   ticker3= yf.Ticker(symbol)
   year_data = ticker3.history(period='365d')
   yearStockPrice= year_data['Close'][0]
   totalPercentGain= (get_current_price(symbol) - yearStockPrice)/ yearStockPrice
   formatTotalPercent = str(to_percent(totalPercentGain))
   return formatTotalPercent



# Function that returns the main articles of news for a particular stock
def get_news(symbol):
	ticker = yf.Ticker(symbol)
	news = []
	news = ticker.news
	headlines = []
   

	#for i in range(len(news)):
	#	    headlines.append(news[i]["title"])
	return news




















