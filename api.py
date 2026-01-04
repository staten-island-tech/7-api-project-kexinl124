# import requests

# url = "https://countriesnow.space/api/v0.1/countries/population/cities"

# def findpopulation():
#     response = requests.get(url)
#     if response.status_code != 200:
#         print("ERROR")
#         return []
#     return response.json()["data"]
# data = findpopulation()

# user_city = input("State a city:").lower()
# user_year = int(input("Give a specific year:"))

# findplace = False
# findyear = False

# for information in data:
#     if information["city"].lower() == user_city:
#         findplace = True
    
#         for i in information["populationCounts"]:
#             if str(user_year) == i["year"]:
#                 print("Data found!")
#                 print("Country", information["country"])
#                 print("City", information["city"])
#                 print("Year:", i["year"])
#                 print("Population:", i["value"])
#                 findyear = True
#         break
        
# if findplace == False:
#         print("Error, city not found. Try again!")
# elif findyear == False:
#      print("Error, no data for this year. Try again!")
# else:
#      print("Great!")

#Tkinter

import requests
import tkinter as tk
from tkinter import messagebox

def findpopulation():
    url = "https://countriesnow.space/api/v0.1/countries/population/cities"
    response = requests.get(url)
    if response.status_code != 200:
        messagebox.showerror("Error", "Failed to fetch data from API")
        return []
    return response.json()["data"]

data = findpopulation()

def search():
    user_city = city_entry.get().strip().lower()
    user_year = year_entry.get().strip()

    if not user_city or not user_year:
        messagebox.showwarning("Input Error", "Please enter both city and year.")
        return

    findplace = False
    findyear = False

    for information in data:
        if information["city"].lower() == user_city:
            findplace = True

            for record in information["populationCounts"]:
                if record["year"] == user_year:
                    result_text.set(
                        f"City: {information['city']}"
                        f"Year: {record['year']}"
                        f"Population: {record['value']}"
                    )
                    findyear = True      
            break  

    if findplace == False:
        messagebox.showerror("Error", "City not found. Try again!")
        result_text.set("")
    elif findyear == False:
        messagebox.showerror("Error", "No data for this year. Try again!")
        result_text.set("")


root = tk.Tk()
root.title("City Population Finder")
root.geometry("450x300")

tk.Label(root, text="Enter City:").pack(pady=5)
city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

tk.Label(root, text="Enter Year:").pack(pady=5)
year_entry = tk.Entry(root, width=30)
year_entry.pack(pady=5)

tk.Button(root, text="Search Population", command=search).pack(pady=10)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left")
result_label.pack(pady=10)

root.mainloop()