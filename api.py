import requests

def getCountries(country):
    response = requests.get(f"https://countriesnow.space/api/v0.1/countries/population/cities{country.lower()}")
    if response.status_code != 200:
        print("Sorry, error fetching data!")
        return None
    
    data = response.json()
    return {
        "city": data["city"],
        "country": data["country"],
        "populationCounts": data["populationCounts"],
        "types": [c["type"]["city"] for c in data["types"]]
    }

countries = getCountries("Åland Islands")
print(countries)


def COuntries():
    countrIes = input("Which countries do you want to know the population from?")