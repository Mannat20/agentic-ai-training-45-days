
import requests
import json

api_key = '0f46691e74c24a3882f5f7e46c108717'
newsapi_url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
response = requests.get(newsapi_url)
news_json = response.text
news_dictionary = json.loads(news_json)
# print(news_dictionary)

articles = news_dictionary['articles']
for article in articles:
    print(article['title'])
    print(article['description'])
    print('~'*30)