import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "4QTE68AWECJFOMH9"


COMPANY_NAME = "Tesla Inc"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "N/A"


TWILIO_SID = "Get your own account_sid from Twilio"
TWILIO_AUTH_KEY = "Get your own auth_token from Twilio"



stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

stock = requests.get(url=STOCK_ENDPOINT, params=stock_params)
stock_data = stock.json()["Time Series (Daily)"]
data_list = [value for (key,value) in stock_data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference_between_prices = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
up_down = "UP_EMOJI" if difference_between_prices > 0 else "DOWN_EMOJI"


diff_percent = round((difference_between_prices / float(yesterday_closing_price)) * 100)
if abs(diff_percent) > 5:
    news_param = {
        "qInTitle": COMPANY_NAME,
        "apiKey": "API_KEY",
    }
    news = requests.get(url=NEWS_ENDPOINT, params=news_param)
    news_articles = news.json()["articles"]
    three_articles = news_articles[:3]
    formatted_articles = []
    for elements in three_articles:
        formatted_articles.append(f"{STOCK_NAME}: {up_down}{diff_percent}% \nHeadline: {elements['title']}\n Brief {elements['description']}")
    print(formatted_articles)

    client = Client(TWILIO_SID, TWILIO_AUTH_KEY)
    for articles in news_articles:
        message = client.messages \
            .create(
            body=articles,
            from_="My phone number!",
            to="To whom am I sending the message to?"
        )
        print(message.status)






#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""