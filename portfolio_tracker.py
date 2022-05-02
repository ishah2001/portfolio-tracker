import pandas as pd 
import yfinance as yf
import os
from yahoofinancials import YahooFinancials



#Taking in user input

file_path = os.path.join(os.path.dirname(__file__), "..", "data", "example.csv")



user_data = pd.read_csv(file_path)
user_data.head()

tickers = []
share_counts = []

for i in range(len(user_data)):
	tickers.append(user_data.iloc[i,0])
	share_counts.append(user_data.iloc[i,1])


#def getReturnSincePurchase(ticker, purchase_date):

print(tickers)









