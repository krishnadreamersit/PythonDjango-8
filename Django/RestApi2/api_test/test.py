import requests
url = 'http://127.0.0.1:8000/api/v1'
headers = {'Authorization': 'Token 749ddd5b6b256a39a1370ac68c360cf5c69b73e5'}
r = requests.get(url, headers=headers)
print(r.text)