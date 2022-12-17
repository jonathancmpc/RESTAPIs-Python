import requests
import ApiKeyFacebook
import json

api_key_facebook = ApiKeyFacebook.api_key_facebook
url = f"https://graph.facebook.com/v15.0/3630020367224237?fields=link%2Cimages&access_token={api_key_facebook}"

response = requests.get(url)
data = response.text

data = json.loads(data)
image_url = data['images'][0]['source']

image_bytes = requests.get(image_url).content

with open('image.jpg', 'wb') as file:
    file.write(image_bytes)