import requests
import json

def search():
    parameters = {
        "s": s,
        "apikey": ## Insert your api key
    }
    response = requests.get("https://www.omdbapi.com/", params=parameters)
    data = response.json()
    if 'Search' in data:
        theMovie = data['Search'][0]
        print(f"Released in {theMovie['Year']}")
    else:
        print("No results found for the movie.")

s = input("Enter: ")
search()
