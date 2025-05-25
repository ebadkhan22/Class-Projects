import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        weather_desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        print(f"Weather in {city}:")
        print(f"Description: {weather_desc}")
        print(f"Temperature: {temp} °C")
        print(f"Humidity: {humidity}%")
    else:
        print("City not found or API request failed.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    api_key = "YOUR_API_KEY_HERE"  # Replace with your actual OpenWeatherMap API key
    get_weather(city, api_key)
