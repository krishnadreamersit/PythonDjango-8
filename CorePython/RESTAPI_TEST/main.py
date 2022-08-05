import json
import requests # pip install requests

api_url = "http://127.0.0.1:8000/customers/"

response = requests.get(api_url)
print(response.status_code); # 200
print(response.content)
print(json.loads(response.content))

# test crud task
