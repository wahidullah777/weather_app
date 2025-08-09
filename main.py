import requests

API_KEY = "4a57e3044107ecef94d275a43dcfb063"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"\n🌤️ Weather in {data['name']}, {data['sys']['country']}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Feels Like: {data['main']['feels_like']}°C")
        print(f"Weather: {data['weather'][0]['description'].title()}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("❌ City not found or API error.")

def main():
    print("=== 🌦️ Weather App ===")
    city = input("Enter city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()
