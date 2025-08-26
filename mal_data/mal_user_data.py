import requests
import json

with open('token.json', 'r') as f:
    token_data = json.load(f)

access_token = token_data['access_token']  # get access token

url = "https://api.myanimelist.net/v2/users/@me/animelist"

# want to grab only anime that has been finished and sorted by scores descending
headers = {
    "status" : "completed", 
    "sort": "list_score",
    "limit": 500,  # max limit is 1000
}

response = requests.get(url, headers={"Authorization": f"Bearer {access_token}"}, params=headers)

if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=2))  # pretty-print the result
else:
    print(f"Error: {response.status_code}")
    print(response.text)
