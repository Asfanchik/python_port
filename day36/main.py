import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

SOCK_API_KEY = "7ZEULHWMPD4SSDPB"
NEWS_AP_KEY =  "58439db14a844533a3f9abb4efeac2fb"
TWILIO_SID = "1234"
TWILIO_AUTH_TOKEN = " 1234"


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME ,
    "apikey" : SOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]# It give us starting from this point (Time Series (Daily))
data_list = [value for (key, value) in data.items()] # it give us list of value only
yesterday_data = data_list[0]
yesterday_data_closing = yesterday_data["4. close"]
print(yesterday_data_closing)


#Get the day before yesterday's closing stock price
the_day_before_yesterday_data = data_list[1]
the_day_before_yesterday_closing_price = the_day_before_yesterday_data["4. close"]
print(the_day_before_yesterday_closing_price)


#Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = float(yesterday_data_closing) - float(the_day_before_yesterday_closing_price)
up_down = None
if difference >0:
    up_down = "⬆️"
else:
    up_down = "⬇️"

#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_pro = round((difference / float(yesterday_data_closing))*100)
print(diff_pro)


#If TODO4 percentage is greater than 5 then print("Get News").
if abs(diff_pro) > 4:
    news_params = {
        "apiKey": NEWS_AP_KEY,
        "qInTitle" : COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

# Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]
    print(three_articles)


#Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"Headline: {articles['title']}. \nBrief: {articles['description']}" for articles in three_articles]

#Send each article as a separate message via Twilio.

    client= Client(TWILIO_SID, TWILIO_AUTH_TOKEN)


    for articles in formatted_articles:
        message = client.messages.create(
            body=articles,
            from_="+15167306982",
            to = "your number",
        )

#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

