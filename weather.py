import requests

def get_weather(city):
    """Fetch and display weather information for a given city."""

    api_key = "YOUR_API_KEY"  # Replace with your OpenWeather API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use Celsius
    }

    try:
        response = requests.get(base_url, params=params, timeout=5)
        response.raise_for_status()  # Raise error if request failed
        data = response.json()

        print(f"\n🌍 Weather in {city}:\n")
        print(f"🌡 Temperature: {data['main']['temp']}°C")
        print(f"☁ Condition: {data['weather'][0]['description'].capitalize()}")
        print(f"💧 Humidity: {data['main']['humidity']}%")
        print(f"💨 Wind Speed: {data['wind']['speed']} m/s")

    except requests.exceptions.RequestException as e:
        print("⚠️ Error fetching weather:", e)
    except KeyError:
        print("⚠️ Could not read weather data. Check your API key or city name.")

# Example run
if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
