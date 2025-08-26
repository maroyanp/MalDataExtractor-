import json
import requests


# Step 1: Load the token from token.json
with open('token.json', 'r') as f:
    token_data = json.load(f)

access_token = token_data['access_token']  # get access token

# Step 2: Set up the API request
url = "https://api.myanimelist.net/v2/anime"
headers = {
    "Authorization": f"Bearer {access_token}"
}
params = {
    "q": "one",     # your search query
    "limit": 4      # number of results
}

# Step 3: Make the request
response = requests.get(url, headers=headers, params=params)

# Step 4: Handle response
if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=2))  # pretty-print the result
else:
    print(f"Error: {response.status_code}")
    print(response.text)
