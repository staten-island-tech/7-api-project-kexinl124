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

import requests

url = "https://countriesnow.space/api/v0.1/countries/population/cities"

def getCountries(country):
    response = requests.get(url, params={"country": country})

    if response.status_code != 200:
        print("ERROR")
        return None

    data = response.json()

    if data.get("error"):
        print("API ERROR:", data.get("msg"))
        return None

    return data["data"]  

countries = getCountries("Åland Islands")

user_city=input("What city do you want to know the population for?").lower()

for city_data in countries:
    if city_data["city"].lower() == user_city:
        print("City:", city_data["city"])
        print("Population records:", city_data["populationCounts"])
        break

if user_city not in city_data["city"]:
   print("we don't got that")
    


# import requests
# import tkinter as tk
# from tkinter import messagebox


# def get_cities_population(country):
#     url = "https://countriesnow.space/api/v0.1/countries/population/cities"
#     response = requests.get(url, params={"country": country})

#     if response.status_code != 200:
#         messagebox.showerror("Error", "Failed to fetch data from API")
#         return {}

#     data = response.json()

#     if data.get("error"):
#         messagebox.showerror("API Error", data.get("msg"))
#         return {}

#     city_dict = {}

#     for city in data["data"]:
#         if not city.get("populationCounts"):
#             print("sorry no data")

#         latest = city["populationCounts"][-1].get("value")

#         if latest is None:
#             continue

#         try:
#             city_dict[city["city"].lower()] = int(float(latest))
#         except ValueError:
#             continue

#     return city_dict

# city_population = get_cities_population("Åland Islands")


# def get_population():
#     city = city_name_entry.get().strip().lower()

#     if not city:
#         messagebox.showwarning("Input Error", "Please enter a city name.")
#         return

#     if city in city_population:
#         population = city_population[city]
#         messagebox.showinfo(
#             "City Population",
#             f"The population of {city.title()} is {population:,}."
#         )
#     else:
#         messagebox.showerror(
#             "City Not Found",
#             "Sorry, we don't have data for that city."
#         )


# root = tk.Tk()
# root.title("City Population Finder")

# city_name_label = tk.Label(root, text="Enter a city name:")
# city_name_label.pack(pady=10)

# city_name_entry = tk.Entry(root)
# city_name_entry.pack(pady=5)

# search_button = tk.Button(root, text="Get Population", command=get_population)
# search_button.pack(pady=10)

# root.mainloop()
