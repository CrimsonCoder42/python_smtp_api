import requests
import os
import smtplib
from dotenv import load_dotenv
from newsapi import NewsApiClient

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
MY_PASSWORD = os.getenv("MY_PASSWORD")
MY_EMAIL = "python32testemail@gmail.com"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"



## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.

def get_article(start_date, end_date, company):

    newsapi = NewsApiClient(api_key=NEWS_API_KEY)

    news_info = newsapi.get_everything(q=company,
                                      from_param=start_date,
                                      to=end_date,
                                      language='en',
                                      sort_by='relevancy',
                                      )

    articles = news_info['articles'][:12]
    return articles

def extract_article_titles(information):
    titles = []
    for article in information:
        titles.append(article['title'])
    return titles

def calculate_date_ranges(data):
    dates = list(data.keys())
    closing_prices = list(data.values())

    date_ranges = {}
    for i in range(1, len(dates)):
        previous_date = dates[i - 1]
        current_date = dates[i]
        date_range = f"{previous_date[:10]}!{current_date[:10]}"

        previous_price = closing_prices[i - 1]
        current_price = closing_prices[i]
        percentage_difference = ((current_price - previous_price) / previous_price) * 100

        date_ranges[date_range] = round(percentage_difference, 2)

    return date_ranges

def extract_closing_prices(data):
    closing_prices = {}

    for date, values in data.items():
        if "19:00:00" in date:  # Check if the date contains "19:00:00"
            closing_price = float(values['4. close'])
            closing_prices[date] = closing_price

    return closing_prices

def get_significant_changes(data):
    significant_changes = []
    for key, value in data.items():
        if abs(value) > 5:
            significant_changes.append((key, value))
    return significant_changes

def send_email(titles):
    title_list = '\n'.join(titles)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        subject = "Article Titles"
        body = title_list.encode('utf-8')
        msg = f"Subject: {subject}\n\n{body.decode('utf-8')}"
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="nostro37@gmail.com",
            msg=msg.encode('utf-8')
        )
        print("Email sent successfully.")


stock_params = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": STOCK_API_KEY
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()
extracted_days_closing_diff = calculate_date_ranges(extract_closing_prices(data["Time Series (60min)"]))
days_greater_than_5 = get_significant_changes(extracted_days_closing_diff)

if len(days_greater_than_5) > 0:
    for date_range, _ in days_greater_than_5:
        date_split = date_range.split('!')
        start_date, end_date = date_range.split('!')
        article_info = get_article(start_date, end_date, "Tesla Inc")
        article_title = extract_article_titles(article_info)
        send_email(article_title)

else:
    print("No significant changes found.")




## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator






## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



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

