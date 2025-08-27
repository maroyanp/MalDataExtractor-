import requests
import json
import pandas as pd

####################################################
#  this script fetches the user's anime list and saves it to a CSV file 
####################################################
with open('token.json', 'r') as f:
    token_data = json.load(f)

access_token = token_data['access_token']  # get access token

url = "https://api.myanimelist.net/v2/users/@me/animelist"

# want to grab only anime that has been finished and sorted by scores descending
headers = {
    'fields': 'list_status, score', 
    "limit": 500,  # max limit is 1000
}

response = requests.get(url, headers={"Authorization": f"Bearer {access_token}"}, params=headers)

if response.status_code == 200:
    data = response.json()
    # print(json.dumps(data, indent=2))  # pretty-print the result
else:
    print(f"Error: {response.status_code}")
    print(response.text)


anime_list = []
for entry in data['data']:
    anime_list.append({
        "title": entry["node"]["title"],
        "score": entry["list_status"]["score"]
    })

df = pd.DataFrame(anime_list)
df.to_csv("user_anime_list.csv", index=False)