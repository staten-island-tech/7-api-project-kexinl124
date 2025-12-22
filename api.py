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
    url = f"https://countriesnow.space/api/v0.1/countries/population/cities?country={country.lower()}"
    
    response = requests.get(url)
    if response.status_code != 200:
        print("ERROR")
        return None
        
    data = response.json()
    print(data)  
    # return {
    #         "city": data['city'],
    #         "country": data['country'],
    #         "populationCounts": data['populationCounts'],
    #         "value": data['value'],
    #         "year": data['year']
    #     }
countries = getCountries("Åland Islands")
print(countries)

import tkinter as tk 
window = tk.Tk()
window.title("City Population")
window.geometry("500x300") 
window.resizable(False, False)

prompt = tk.Label(window, text="Type a city:",
font=("Arial", 14))
prompt.pack(pady=10)

entry = tk.Entry(window, font=("Arial", 14), width=30)
entry.pack(pady=5)

result_label = tk.Label(window, text="", font=("Arial", 14, "bold"),
fg="blue")
result_label.pack(pady=15)

def citypopulation():
    if 
    text = entry.get() 
    reversed_text = text[::-1]
    result_label.config(text=f"Backwards: {reversed_text}")

reverse_button = tk.Button(window, text="City Population",
font=("Arial", 14),

command=reverse_message)

reverse_button.pack(pady=10)

window.mainloop()


    
