import requests
import smtplib

my_email = "hisherhim2022@gmail.com"
my_pass = "fqhbljpavieykgoz"


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"


authorization = "349b17ac533e4f7986aecea1ab3ef9e6"
x_api_key = "349b17ac533e4f7986aecea1ab3ef9e6"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
ALPHA_API_KEY = "UKJ59NYBEO7FTKM2"


url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=UKJ59NYBEO7FTKM2"
r = requests.get(url)
data = r.json()


yest_closing = data["Time Series (Daily)"]['2022-06-30']['4. close']
yest_closing = float(yest_closing)
print(yest_closing)


day_bef_yest_closing = data["Time Series (Daily)"]['2022-06-29']['4. close']
day_bef_yest_closing = float(day_bef_yest_closing)
print(day_bef_yest_closing)

difference = abs(yest_closing - day_bef_yest_closing)
print(difference)


diff_percentage = (difference / day_bef_yest_closing) * 100
print(diff_percentage)


if diff_percentage > 1:

    news_params = {
        "apiKey": x_api_key,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()['articles']
    # print(articles)
    three_articles = articles[:3]
    # print(three_articles)


    formatted_articles = [f"Headline: {article['title']} \nBrief: {article['description']} \nContent: {article['content']}" for article in three_articles]
    # for article in formatted_articles:
        # print(article)

    for article in formatted_articles:
        print(article)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_pass)
            connection.sendmail(from_addr=my_email,
                                to_addrs="lakho75@yahoo.com",
                                msg=f"{article}")

print("Mail sent successfully!")