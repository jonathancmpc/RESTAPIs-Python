import requests
import ApiKey

api_key = ApiKey.api_key

def get_news(topic,from_date,to_date,language='en',api_key_=api_key):
  url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key_}'
  r = requests.get(url)
  content = r.json()

  articles = content['articles']
  #print(content['articles'][1]['source']['name'])

  results = []

  for article in articles:
    results.append(f"TITLE\n' {article['title']}, '\nDESCRIPTION\n', {article['description']}")

  return results


def main():
  print(get_news(topic='united states', from_date='2022-12-14', to_date='2022-12-15'))

main()