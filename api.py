import requests

def getCountries(country):
    response = requests.get(f"https://countriesnow.space/api/v0.1/countries/population/cities{country.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
        "country": data["country"],
        "city": data["city"],
        "population": data["populationCounts"],
        "reliablity":data["reliablity"],
        
    }

countries = getCountries("Åland Islands")
print(countries)