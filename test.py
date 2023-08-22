import requests

# API endpoint URL
url = 'https://data.usajobs.gov/api/search'
headers = {
    'Host': 'data.usajobs.gov',
    'User-Agent': 'aagiraldohe@gmail.com',
    'Authorization-Key': ""
}

# Parameters to be included in the URL
params = {
    'Keyword': 'Software Development',
}

# Send the GET request
response = requests.get(url, params=params, headers=headers)

# Parse the JSON response
data = response.json()

# Now you can work with the 'data' variable containing the parsed JSON response
print(data)
