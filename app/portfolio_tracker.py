import pandas as pd 
import yfinance as yf
import os
from yahoofinancials import YahooFinancials
from utils import get_current_price
from utils import get_news
from utils import summary_stats
from utils import get_DifferenceInDay
from utils import get_Purchased_price




#Taking in user input

file_path = os.path.join(os.path.dirname(__file__), "..", "data", "example.csv")

user_data = pd.read_csv(file_path)
user_data.head()

for i in range(len(user_data)):

	temp_ticker = user_data.iloc[i,0]
	temp_share_count = user_data.iloc[i,1]
	temp_date_purchased = user_data.iloc[i,2]

	current_price = get_current_price(temp_ticker)

	current_market_value = current_price * temp_share_count

	news_headlines= get_news(temp_ticker)

	historical_summary_stats = summary_stats(temp_ticker)

	purchase_date_price = get_Purchased_price(temp_ticker, temp_date_purchased)

	








	#more functions and making the graph and pdf










