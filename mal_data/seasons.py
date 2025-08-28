import json
import requests
import pandas as pd

# ##############################################
# This is a function that sets the url for the season and year
# ##############################################
# Returns: a string in the format "year/season"
def get_anime_season(year, season):
    return f"https://api.myanimelist.net/v2/anime/season/{year}/{season}"


seasons = ["winter", "spring", "summer", "fall"]
years = [2022, 2023, 2024, 2025]
urls = []

# Step 1: Load the token from token.json
with open('token.json', 'r') as f:
    token_data = json.load(f)
access_token = token_data['access_token']  # get access token

for year in years:
    for season in seasons:
        print(f"Fetching data for {year} {season} season...")
        urls.append(get_anime_season(2024, "summer"))

headers = {
        "fields": "id,title,mean,rank,popularity,num_list_users,media_type,status,start_season,genres,my_list_status",
        "limit": 100
    }
anime_list = []
for url in urls:
    response = requests.get(url, headers={"Authorization": f"Bearer {access_token}"}, params=headers)
    # Step 4: Handle response
    if response.status_code == 200:
        data = response.json()
        # print(json.dumps(data, indent=2))  # pretty-print the result
        
        for entry in data['data']:
            anime_list.append({
                "title": entry["node"]["title"],
                "id": entry["node"]["id"],
                "popularity": entry["node"]["popularity"],
                "score": entry["node"]["mean"],
                "generes": [genre["name"] for genre in entry["node"]["genres"]]
            })
        
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

df = pd.DataFrame(anime_list)
df.to_csv(f"data/seasonal_anime{years[0]}-{years[len(years) - 1]}.csv", index=False)