import requests

def weather_details(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        feels_like = data["main"]["feels_like"]
        description = data["weather"][0]["description"]

        print(f"\nWeather in {city}:")
        print(f"Temperature: {temperature} C (feels like: {feels_like} C)")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description.capitalize()}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather: {e}")

api_key = "a2e6f80850be661dfec45124c6e8baf1"
city = input("Enter city name: ")

weather_details(city, api_key)

