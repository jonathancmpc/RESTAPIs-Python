import requests
import ApiKey

api_key = ApiKey.api_key
url = f'https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2022-11-15&to=2022-11-15&sortBy=popularity&language=en&apiKey={api_key}'
r = requests.get(url)
content = r.json()

articles = content['articles']
#print(content['articles'][1]['source']['name'])
print(type(articles))

for article in articles:
    print('TITLE\n', article['title'], '\nDESCRIPTION\n', article['description'])