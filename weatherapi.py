
import requests


API_KEY = "" # É necessário por sua própria API key para que o código funcione
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Digite o nome de uma cidade: ")


request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)


if response.status_code == 200 :
    data = response.json()

    weather = data["weather"][0]["description"]
    temp = round(data["main"]["temp"] - 273.15, 2)

    translate = {
        "overcast clouds" : "nublado",
        "broken clouds" : "parcialmente nublado",
        "snow" : "nevando",
        "mist" : "névoa leve",
        "fog" : "névoa forte",
        "light rain" : "chuva leve"
    }

    if weather in translate.keys() :
        print(f"Clima: {translate[weather]}")
        

    else :
        print(f"Clima: {weather}")

    
    print(f"Temperatura: {temp} ºC")


else :
    print("Ocorreu um erro...")
