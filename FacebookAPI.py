import requests
import ApiKeys

api_key_facebook = ApiKeys.api_key_facebook
url = f"https://graph.facebook.com/v15.0/me?fields=id%2Cname&access_token={api_key_facebook}"

response = requests.get(url)
print(response)