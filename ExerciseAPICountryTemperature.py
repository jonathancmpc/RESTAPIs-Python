import requests
import xmltodict
import ApiKeys

api_key = ApiKeys.api_key_openweathermap

def get_country_info(country, api_key=api_key):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={country},us&mode=xml&appid={api_key}'
    response = requests.get(url)
    content = xmltodict.parse(response.content)
    
    forecasts = content['weatherdata']['forecast']['time']

    results = []
    for forecast in forecasts:
        array = [
            content['weatherdata']['location']['name'],',',
            forecast['@from'],',',
            forecast['temperature']['@value'],',',
            forecast['symbol']['@name']
        ]
        results.append(array)    
    return results

def write_file(info_country):
    with open("data_country_temperature.txt", 'a') as file:
      for info in info_country:
          item = (' '.join(info).replace(' , ', ',')).replace('T', ' ')
          file.write('\n' + item)

def main():
    # get information API
    info_country = get_country_info('Brazil')

    # write at the file
    write_file(info_country)

main()