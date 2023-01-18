import requests
from twilio.rest import Client 

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "your_api_key"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_API_KEY = "your_api_key"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

TWILIO_SID = "your_account_sid"
TWILIO_AUTH_TOKEN = "your_auth_token"


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

r = requests.get(STOCK_ENDPOINT, params=stock_params)
data = r.json()["Time Series (Daily)"]
#print(data)
data_list = [value for (key, value) in data.items()]
yesterday = data_list[0]
yesterday_closing_price = yesterday["4. close"]
#print(yesterday_closing_price)

# Get the data for the last day of the stock market and get the closing price
day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday["4. close"]

# Find the positive difference between 1 and 2.
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"


# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = round((difference / float(yesterday_closing_price)) * 100)

# if percentage is greater than 5 then print("Get News").
if abs(diff_percent) > 5:
    #print("Get News")
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }

    r = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = r.json()["articles"]

    #Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

    three_articles = articles[:3]
    print(three_articles)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    
    #Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    #Send each article as a separate message via Twilio. 
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
                body=article,
                from_='your_twilio_number',
                to='your_phone_number'
            )



