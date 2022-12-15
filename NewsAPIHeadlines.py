import requests
import ApiKey

api_key = ApiKey.api_key

def get_news(country,api_key_=api_key):
  url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key_}'
  r = requests.get(url)
  content = r.json()

  articles = content['articles']
  #print(content['articles'][1]['source']['name'])

  results = []

  for article in articles:
    results.append(f"TITLE\n' {article['title']}, '\nDESCRIPTION\n', {article['description']}")

  return results


def main():
  print(get_news(country='us'))

main()