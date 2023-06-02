import requests
import json
import os
from win10toast import ToastNotifier

API_KEY = "1ff72feb511f41a897a141756230206"
AYARLAR_FILE = "settings.json"
WEATHER_API_URL = "https://api.weatherapi.com/v1/current.json?key={}&q={}"

def save_settings(settings):
    with open(AYARLAR_FILE, "w") as file:
        json.dump(settings, file)

def load_settings():
    if os.path.exists(AYARLAR_FILE):
        with open(AYARLAR_FILE, "r") as file:
            return json.load(file)
    return {}

def get_weather(city):
    url = WEATHER_API_URL.format(API_KEY, city)
    response = requests.get(url)
    data = json.loads(response.text)
    weather = data["current"]["condition"]["text"]
    temperature = data["current"]["temp_c"]
    return weather, temperature

def show_notification(message):
    toaster = ToastNotifier()
    toaster.show_toast("Hava Durumu", message, duration=5)

def main():
    settings = load_settings()
    if "city" in settings:
        city = settings["city"]
        weather, temperature = get_weather(city)
        message = f"Hava Durumu: {weather}\nSıcaklık: {temperature}°C"
        show_notification(message)
    else:
        city = input("Şehir adını girin: ")
        settings["city"] = city
        save_settings(settings)
        print("Konum ayarlandı.")

if __name__ == "__main__":
    main()
