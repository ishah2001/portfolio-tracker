import pandas as pd 
import yfinance as yf
from yahoofinancials import YahooFinancials



#Taking in user input

user_data = pd.read_csv("C:/Users/17819/Desktop/UserInputs.csv")
user_data.head()

tickers = []
share_counts = []

for i in range(len(user_data)):
	tickers.append(user_data.iloc[i,0])
	#share_counts.append(user_data[i,1])


#def getReturnSincePurchase(ticker, purchase_date):

print(tickers)









