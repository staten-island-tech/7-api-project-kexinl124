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
# import requests

# def getCountries(country):
#     url = f"https://countriesnow.space/api/v0.1/countries/population/cities?country={country.lower()}"
    
#     response = requests.get(url)
#     if response.status_code != 200:
#         print("ERROR")
#         return None
        
#     data = response.json()
#     print(data)  
#     return {
#             "country": data['country'],
#             "populationCounts": data['populationCounts'],
#             "value": data['value'],
#             "year": data['year']
#         }
# countries = getCountries("Åland Islands")
# print(countries)

import requests
url = "https://countriesnow.space/api/v0.1/countries/population/cities"

def get_cities_population(country):
    url = "https://countriesnow.space/api/v0.1/countries/population/cities"
    response = requests.get(url, params={"country": country})

    if response.status_code != 200:
        print("Sorry, error fetching data!")
        return None

    data = response.json()

    if data.get("error"):
        print("API ERROR:", data.get("msg"))
        return None

    return data["data"] 

cities = get_cities_population("Åland Islands")

for city in cities:
    print(city["city"], city["populationCounts"])

import tkinter as tk
from tkinter import messagebox

city_population = {
    "New York": 8419600,
    "Los Angeles": 3980400,
    "Chicago": 2716000,
    "Houston": 2328000,
    "Phoenix": 1690000,
    "San Francisco": 883305,
    "Boston": 694583
}
def get_population():
    city = city_name_entry.get().strip()

    if city in "data":
        population = data[city]
        messagebox.showinfo("City Population", f"The population of {city} is {population}.")
    else:
        messagebox.showerror("City Not Found", "Sorry, we don't have data for that city.")

root = tk.Tk()
root.title("City Population Finder")

city_name_label = tk.Label(root, text="Enter a city name:")
city_name_label.pack(pady=10)

city_name_entry = tk.Entry(root)
city_name_entry.pack(pady=5)

search_button = tk.Button(root, text="Get Population", command=get_population)
search_button.pack(pady=10)

root.mainloop()