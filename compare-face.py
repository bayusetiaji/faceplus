import requests
import json

url = 'https://api-us.faceplusplus.com/facepp/v3/compare' # API URL
api_k = '<your API Key>' # API Key
api_s = '<your API Secret' # API Secret

img1 = 'https://pict-a.sindonews.net/dyn/620/jatim/news/2019/03/02/1/7867/nama-soekarno-diabadikan-jadi-nama-tempat-dan-perangko-di-6-negara-ini-hew.jpg'
img2 = 'https://ewr1.vultrobjects.com/suarapapuaweb/2019/10/bung-hatta.jpg'

# setting parameter
payload = dict(api_key = api_k, api_secret = api_s, image_url1 = img1, image_url2 = img2)

# request
response = requests.post(url, data = payload)

# result
result = response.text

print(json.loads(result)['confidence'])
