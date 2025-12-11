import requests

def getCharacters(characters):
    response = requests.get(f"https://hsr-api.vercel.app/api/v1/characters{hsr.lower()}")
    if response.status_code != 200:
        print("Error please wait")
        return None
    
    data = response.json()
    return {
        "name": data["name"],
        "element": data["element"],
        "rarity": data["rarity"],
        "types": [t["type"]["name"] for t in data["types"]]
    }

hsr = getCharacters("Trailblazer")
print(hsr)