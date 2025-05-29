import requests
import os


API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        print(f"{city}: {temp}°C, {desc}")
    else:
        print(f"Error: {data.get('message', 'Unknown error')}")


if __name__ == "__main__":
    city = input("Enter a city: ")
    get_weather(city)
