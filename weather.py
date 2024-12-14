import requests
import sys
API_KEY = '40e151f43a8da63402abb3c21eaeabbb'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
AVAILABLE_OPTIONS = {
    'temperature': 'Temperature (in Celsius)',
    'humidity': 'Humidity (%)',
    'wind_speed': 'Wind Speed (m/s)',
}


def get_weather(city, option=None):
    url = f'{BASE_URL}?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: Unable to get data for city '{city}'.")
        sys.exit(1)
    data = response.json()
    if data.get('cod') != 200:
        print(f"Error: City '{city}' not found.")
        sys.exit(1)
    weather = data['main']
    wind = data['wind']
    if option == 'temperature':
        print(f"Temperature: {weather['temp']} °C")
    elif option == 'humidity':
        print(f"Humidity: {weather['humidity']} %")
    elif option == 'wind_speed':
        print(f"Wind Speed: {wind['speed']} m/s")
    else:
        print("Invalid option. Please choose either 'temperature', 'humidity', or 'wind_speed'.")


def main():
    city = input("Enter the city name to get the weather forecast: ")
    print("\nAvailable weather options:")
    for option in AVAILABLE_OPTIONS.keys():
        print(option)
    option = input("\nEnter the weather parameter you want ('temperature', 'humidity', 'wind_speed'): ").lower()
    if option not in AVAILABLE_OPTIONS:
        print("Invalid option. Please choose from 'temperature', 'humidity', or 'wind_speed'.")
        return
    get_weather(city, option)


if __name__ == '__main__':
    main()
