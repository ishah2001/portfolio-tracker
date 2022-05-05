# portfolio-tracker


##Welcome

Welcome to the portfolio tracker application! This program was developed by Carmen Aizpurua Bernabe, Danny Morales, and Ishaan Shah
for our final project in OPIM 244.



## Setup

The first step to setting up this application for usage is to download the example.csv file (portfolio-tracker/data/example.csv)


Fill it our with your stocks

It gives a template of what it should look like

First Column: Put the Ticker all in caps

Second Column: Put the number of shares

Third column: Put the date purchased of that stock (month/day/year)


Install Packages:

```sh
pip install -r requirements.txt
```

## Configuration

Obtain a premium AlphaVantage API Key [here](https://www.alphavantage.co/).

Sign up for a [SendGrid Account](https://sendgrid.com/), verify single sender, then obtain a Sendgrid API Key. 



```sh
ALPHAVANTAGE_API_KEY="..."

SENDER_ADDRESS="example@gmail.com"
SENDGRID_API
```



## Usage  

Send the email:

```sh
python app/portfolio_tracker.py
```



