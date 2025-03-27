import json
import requests

kohde = input("Anna kaupungin nimi:")
apikey = input("Anna API key:")

pyynto_koord = f"http://api.openweathermap.org/geo/1.0/direct?q={kohde}&limit=1&appid={apikey}"
#söön text and asteet cels paikan nimi
try:
    vastaus = requests.get(pyynto_koord)
    if vastaus.status_code==200:
        json_vastaus = vastaus.json()
        for i in json_vastaus:
            lon = i["lon"]
            lat = i["lat"]


except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa")

pyynto_saa = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={apikey}"

try:
    vastaus2 = requests.get(pyynto_saa)
    if vastaus2.status_code==200:
        json_vastaus2 = vastaus2.json()
        print(f'City name: {json_vastaus2['name']}\nTemperature: {json_vastaus2["main"]["temp"]}°C\nDescription: {json_vastaus2["weather"][0]["description"]}')


except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa")