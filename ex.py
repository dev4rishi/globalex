import requests
url = "https://amon-price1.p.rapidapi.com/search"

querystring = {"keywords":"laptop","marketplace":"IN"}

headers = {
    'x-rapidapi-host': "amazon-price1.p.rapidapi.com",
    'x-rapidapi-key': "84d8a9b38bmsh118fd99edc71fbbp15d71ejsn24e82852e2f5"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
dumped=response.json()
print(type(dumped))
for i in dumped:
    print(i['price'])
