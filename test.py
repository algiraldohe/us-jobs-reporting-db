import requests
import json


# API endpoint URL
url = 'https://data.usajobs.gov/api/search'
headers = {
    'Host': 'data.usajobs.gov',
    'User-Agent': 'aagiraldohe@gmail.com',
    'Authorization-Key': "gh3jLR00nD4jPbv2Z4GUEwkWfGtyQvz96Kc3JeHTDa0="
}

# Parameters to be included in the URL
params = {
    "Keyword": 'data engineering',
    "DatePosted": 3,
    "LocationName": ["Chicago, Illinois"],

}

# Send the GET request
response = requests.get(url, params=params, headers=headers)

# Parse the JSON response
data = response.json()

# Now you can work with the 'data' variable containing the parsed JSON response
with open("response.json", "w") as json_file:
            json.dump(data, json_file, indent=4)  # Save JSON data to a file with indentation

