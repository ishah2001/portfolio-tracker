# portfolio-tracker


## Welcome

Welcome to the portfolio tracker application! This program was developed by Carmen Aizpurua Bernabe, Danny Morales, and Ishaan Shah
for our final project in OPIM 244.



## Setup

1. The first step to setting up this application for usage is to download the example.csv file (portfolio-tracker/data/example.csv)
2. Now make a copy and name it "portfolio.csv". It is VERY IMPORTANT that this exact name is used.
3. Fill out your own stock data in this csv file based on the existing headings
4. Save the file to the data folder. The file path of this csv file should end up being "portfolio-tracker/data/portfolio.csv"




Now open up your terminal(or GitBash) and navigate to the project location. Then install neccessary packages through this command:

```sh
pip install -r requirements.txt
```

## Configuration


1. Sign up for a [SendGrid Account](https://sendgrid.com/), verify single sender, then obtain a Sendgrid API Key.
2. Then create a dynamic template in SendGrid, add a version, and obtain the key for that version
3. Then create a ".env" file at the root level in the "portfolio-tracker" repository
4. Input your SendGrid API Key, Dynamic Template Key, and Sender Address in the ".env" file in the following way.





```sh
SENDGRID_API_KEY="xxxxxxxxx"
SENDER_ADDRESS="email@example.com"
SENDGRID_TEMPLATE_ID ="xxxxxxxxxx"
```

5. After creating and naming the dynamic template version, input the following html code in there:

```sh

<h3>Hello this is your stock report for {{stock_ticker}}: </h3>

<p>Here is a Brief Summary of your current holding in {{stock_ticker}}: </p>

<p><strong> Number of Shares:</strong> {{share_count}} </p>
<p><strong> Current Price:</strong> {{current_stock_price}} </p>
<p><strong> Total Market Value:</strong> {{total_market_value}}</p>
<p>---------------------------------------------------------------------</p>


<p> Stock Performance of {{stock_ticker}}: </p>
<p><strong> 1 Week Return:</strong> {{weekly_return}} </p>
<p><strong> 1 Month Return:</strong> {{monthly_return}} </p>
<p><strong> 1 Year Return:</strong> {{yearly_return}} </p>
<p><strong> Return Since Purchase Date:</strong> {{purchase_return}}</p>
<p>---------------------------------------------------------------------</p>

<p> Relevant News:</p>


<ul>
{{#each news}}
	<li>{{this.title}}</li>
{{/each}}
</ul>


<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
  <div id="tradingview_47971"></div>
  <div class="tradingview-widget-copyright"><a href={{url}} rel="noopener" target="_blank"><span class="blue-text">{{stock_ticker}} Chart</span></a> by TradingView</div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget(
  {
  "autosize": true,
  "symbol": {{stock_ticker}},
  "interval": "D",
  "timezone": "Etc/UTC",
  "theme": "light",
  "style": "1",
  "locale": "en",
  "toolbar_bg": "#f1f3f6",
  "enable_publishing": false,
  "allow_symbol_change": true,
  "container_id": "tradingview_47971"
}
  );
  </script>
</div>
<!-- TradingView Widget END -->





```

6. Also in the subject line in SendGrid add the following:
```sh
Weekly Stock Report for {{stock_ticker}}
```





## Usage  

Send the email:

```sh
python app/portfolio_tracker.py
```

## Run tests 

To make sure that the code runs property follow these steps

Double check if pytest was downloaded to the terminal

```sh
pip install -r requirements.txt
```

then in the terminal run the pytest

```sh
pytest
```

if there are no issues with the code it will give you a passed message

However, if the message is red, then something is wrong with the code and 
adjustments will have to be made


