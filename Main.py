from forex_python.converter import CurrencyRates
import requests


currencies={'US':'USD','CA':'CAD','IN':'INR','AU':'AUD','GB':'GBP','IT':'ITL','ES':'EUR','FR':'EUR','JP':'JPY','CN':'CNY'}
print("WELCOME TO GLOBALEX!")
print("Please enter the following details: ")
l=[]
l.append(input("Enter the items:"))
choice=input("Press 1 to enter next item. Press any other key to stop.")
while choice == '1':
    l.append(input("Enter the next item:"))
    choice = input("Press 1 to enter next item. Press any other key to stop.")
loc_des=input("Enter the region where you would like to search")
loc_cur=input("Enter your current region")

def get_price(keywrd,mkt):
    prices=[]
    url = "https://amon-price1.p.rapidapi.com/search"

    querystring = {"keywords": keywrd, "marketplace": mkt}

    headers = {
        'x-rapidapi-host': "amazon-price1.p.rapidapi.com",
        'x-rapidapi-key': "84d8a9b38bmsh118fd99edc71fbbp15d71ejsn24e82852e2f5"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    dumped = response.json()
    print(type(dumped))
    for i in dumped:
        prices.append(i['price'])
    return prices

def convert(base,final,amt):
    base_cur=currencies[base]
    final_cur=currencies[final]
    c=CurrencyRates()
    return c.convert(base_cur,final_cur,amt)

def main():
