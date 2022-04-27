import pandas as pd 
import yfinance as yf
from yahoofinancials import YahooFinancials

msft = yf.Ticker("PENN")

hist = msft.history(period="max")

rec = msft.recommendations

calendar = msft.news

print(calendar)

#print(rec)