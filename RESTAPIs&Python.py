import requests

r = requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2022-11-15&to=2022-11-15&sortBy=popularity&language=en&apiKey=50f4ac2844cc472896187cb982893609')
content = r.json()

articles = content['articles']
#print(content['articles'][1]['source']['name'])
print(type(articles))

for article in articles:
    print('TITLE\n', article['title'], '\nDESCRIPTION\n', article['description'])