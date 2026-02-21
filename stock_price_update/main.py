import requests
from datetime import date, timedelta
import os
import smtplib

my_email = os.environ.get("ETEST_EMAIL")
password = os.environ.get("ETEST_EMAIL_PWD")


COMPANY_NAME = "IBM"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
EMAIL = os.environ.get("EMAIL")
EMAIL_PWD = os.environ.get("EMAIL_PASSWORD")

yesterday = str(date.today() - timedelta(days=1))
dbyesterday = str(date.today() - timedelta(days=2))

stock_url = "https://www.alphavantage.co/query"
stock_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol": COMPANY_NAME,
    "apikey": STOCK_API_KEY
}
stock_response = requests.get(url=stock_url,params=stock_params)
stock_data = stock_response.json()
yesterday_price = float(stock_data['Time Series (Daily)'][yesterday]['4. close'])
dbyesterday_price = float(stock_data['Time Series (Daily)'][dbyesterday]['4. close'])

difference = abs(((dbyesterday_price - yesterday_price)/dbyesterday_price)*100)
print(difference)

if difference >= 5:
    news_url = "https://newsapi.org/v2/everything"
    news_params = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }

    news_response = requests.get(url=news_url, params=news_params)
    news_data = news_response.json()

    for article in (news_data['articles'][:3]):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=EMAIL_PWD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg=f"IBM stock price\n\n{article['title']}\n{article['description']}\n{article['url']}"
            )


