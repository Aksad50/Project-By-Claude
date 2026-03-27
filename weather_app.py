import requests

# ─────────────────────────────────────────────
#  🌦️  Weather App  |  Uses OpenWeatherMap API
# ─────────────────────────────────────────────

API_KEY = "b50ef49829b54bfdd1ac185968fd48dd"   # 👈 Replace with your free API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """Fetch weather data for a given city."""
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"   # Change to "imperial" for Fahrenheit
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.HTTPError:
        print(f"\n❌ City '{city}' not found. Please check the spelling and try again.")
        return None

    except requests.exceptions.ConnectionError:
        print("\n❌ No internet connection. Please check your network.")
        return None


def display_weather(data):
    """Display weather information in a readable format."""
    city        = data["name"]
    country     = data["sys"]["country"]
    temp        = data["main"]["temp"]
    feels_like  = data["main"]["feels_like"]
    humidity    = data["main"]["humidity"]
    condition   = data["weather"][0]["description"].capitalize()
    wind_speed  = data["wind"]["speed"]

    print("\n" + "=" * 40)
    print(f"  📍 {city}, {country}")
    print("=" * 40)
    print(f"  🌡️  Temperature  : {temp}°C")
    print(f"  🤔  Feels Like   : {feels_like}°C")
    print(f"  💧  Humidity     : {humidity}%")
    print(f"  🌤️  Condition    : {condition}")
    print(f"  💨  Wind Speed   : {wind_speed} m/s")
    print("=" * 40)


def main():
    print("\n🌦️  Welcome to Weather App!")
    print("   Type 'quit' to exit.\n")

    while True:
        city = input("Enter city name: ").strip()

        if city.lower() == "quit":
            print("\n👋 Goodbye!\n")
            break

        if not city:
            print("⚠️  Please enter a city name.")
            continue

        data = get_weather(city)
        if data:
            display_weather(data)


if __name__ == "__main__":
    main()