# portfolio-tracker


## Welcome

Welcome to the portfolio tracker application! This program was developed by Carmen Aizpurua Bernabe, Danny Morales, and Ishaan Shah
for our final project in OPIM 244.



## Setup

1. The first step to setting up this application for usage is to download the example.csv file (portfolio-tracker/data/example.csv)
2. Now make a copy and name it "portfolio.csv". It is VERY IMPORTANT that this exact name is used.
3. Fill out your own stock data in this csv file based on the existing headings
4. Save the file to the data folder. The file path of this csv file should end up being "portfolio-tracker/data/portfolio.csv"




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



