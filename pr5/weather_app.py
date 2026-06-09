import requests
import sys

API_KEY = "5e3a255461cf801815a9fe25e6ee456c"

def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "ru"
    }
    
    try:
        response = requests.get(url, params=params, timeout=5)
        if response.status_code == 401:
            print("Ошибка 401: Неверный API-ключ")
            return None
        if response.status_code == 404:
            print(f"Ошибка 404: Город '{city}' не найден")
            return None
        response.raise_for_status()
        data = response.json()
        city_name = data["name"]
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        return city_name, temperature, description, humidity, wind

    except requests.exceptions.Timeout:
        print("Ошибка: Таймаут 5 сек")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Ошибка: {e}")
        return None

def main():
    if len(sys.argv) > 1:
        city = " ".join(sys.argv[1:])
    else:
        city = input("Введите город: ").strip()
        if not city:
            print("Город не введен")
            return
    
    result = get_weather(city)
    if result:
        city_name, temp, description, humidity, wind = result
        print(f"\nГород: {city_name}")
        print(f"Температура: {temp} 'C")
        print(f"Описание: {description}")
        print(f"Влажность: {humidity} %")
        print(f"Ветер: {wind} м/с")

if __name__ == "__main__":
    main()