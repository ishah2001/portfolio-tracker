import pandas as pd 
import yfinance as yf
import os
from yahoofinancials import YahooFinancials
from utils import get_current_price
from utils import get_news
from utils import summary_stats
from utils import get_DifferenceInDay
from utils import get_Purchased_price
from utils import to_usd
from utils import to_percent
from utils import weekReturn
from utils import monthReturn
from utils import yearReturn
import matplotlib.pyplot as plt
import seaborn as sns
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)
import base64






#Taking in user input

#file_path = os.path.join(os.path.dirname(__file__), "..", "data", "example.csv")
file_path = os.path.join(os.path.dirname(__file__), "..", "data", "portfolio.csv")

user_data = pd.read_csv(file_path)
user_data.head()

for i in range(len(user_data)):

	#gathering ticker, share count, and date purchased data for each stock
		temp_ticker = user_data.iloc[i,0]
		temp_share_count = user_data.iloc[i,1]
		temp_date_purchased = user_data.iloc[i,2]

	#higher level caluclations using yfinance and methods from utils.py

		current_price = get_current_price(temp_ticker)

		current_market_value = current_price * temp_share_count

		news= get_news(temp_ticker)

		historical_summary_stats = summary_stats(temp_ticker)

		purchase_date_price = get_Purchased_price(temp_ticker, temp_date_purchased)

		return_since_purchase = (current_price - purchase_date_price)/purchase_date_price

		weekly_return = weekReturn(temp_ticker)
		monthly_return = monthReturn(temp_ticker)
		yearly_return = yearReturn(temp_ticker)

		chart_url = "https://www.tradingview.com/symbols/"+temp_ticker+"/"
		

		
		load_dotenv()

		SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
		SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")
		SENDGRID_TEMPLATE_ID = os.getenv("SENDGRID_TEMPLATE_ID", default="OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'")


		template_data = {
			"stock_ticker": temp_ticker,
			"purchase_date": temp_date_purchased,
			"share_count": str(temp_share_count),
			"current_stock_price": str(to_usd(current_price)),
			"total_market_value": str(to_usd(current_market_value)),
			"purchase_return": str(to_percent(return_since_purchase)),
			#"monthly_return":str(to_percent(monthly_return)),
			#"weekly_return": str(to_percent(weekly_return)),
			#"yearly_return": str(to_percent(yearly_return)),
			"monthly_return":monthly_return,
			"weekly_return": weekly_return,
			"yearly_return": yearly_return,
		    "news": news,
		    "url":chart_url
		    
		    
		}


		client = SendGridAPIClient(SENDGRID_API_KEY)
		print("CLIENT:", type(client))

		message = Mail(from_email=SENDER_ADDRESS, to_emails=SENDER_ADDRESS)
		message.template_id = SENDGRID_TEMPLATE_ID
		message.dynamic_template_data = template_data
		print("MESSAGE:", type(message))

		try:
		    response = client.send(message)
		    print("RESPONSE:", type(response))
		    print(response.status_code)
		    print(response.body)
		    print(response.headers)

		except Exception as err:
		    print(type(err))
		    print(err)








	#more functions and making the graph and pdf










