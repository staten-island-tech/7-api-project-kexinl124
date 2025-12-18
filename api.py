# import requests

# def getCountries(country):
#     response = requests.get(f"https://countriesnow.space/api/v0.1/countries/population/cities{country.lower()}")
#     if response.status_code != 200:
#         print("ERROR")
#         return None
    
#     data = response.json()
#     return {
#         "city": data["city"],
#         "country": data["country"],
#         "populationCounts": data["populationCounts"],
#         "MSG": [c["type"]["city"] for c in data["types"]]
#     }

# countries = getCountries("Åland Islands")
# print(countries)


# def COuntries():
#     countrIes = input("Which countries do you want to know the population from?")
import requests

def getCountries(country):
    # Correct the URL format by adding a slash before the country
    url = f"https://countriesnow.space/api/v0.1/countries/population/cities?country={country.lower()}"
    
    response = requests.get(url)
    if response.status_code != 200:
        print("ERROR")
        return None
        
    data = response.json()
    print(data)  
    try:
        return {
            "city": data["city"],
            "country": data["country"],
            "populationCounts": data["populationCounts"],
            "MSG": [c["type"]["city"] for c in data["types"]]
        }
    except KeyError as e:
        print(f"Missing key: {e}")
        return None

# Test with the 'Åland Islands' country
countries = getCountries("Åland Islands")
print(countries)