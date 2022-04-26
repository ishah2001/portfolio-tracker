import pandas as pd 
import yfinance as yf
from yahoofinancials import YahooFinancials

msft = yf.Ticker("MSFT")

hist = msft.history(period="max")

print(hist)