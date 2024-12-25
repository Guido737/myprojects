import requests
import argparse
API_KEY = '40e151f43a8da63402abb3c21eaeabbb'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
AVAILABLE_OPTIONS = {
    'temperature': 'Temperature (in Celsius)',
    'humidity': 'Humidity (%)',
    'wind_speed': 'Wind Speed (m/s)',
}


def fetch_weather_data(city):
    try:
        url = f'{BASE_URL}?q={city}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None

def display_weather_conditions(weather, wind, option):
    try:
        if option == 'temperature':
            print(f"Temperature: {weather.get('temp', 'N/A')} °C")
        elif option == 'humidity':
            print(f"Humidity: {weather.get('humidity', 'N/A')} %")
        elif option == 'wind_speed':
            print(f"Wind Speed: {wind.get('speed', 'N/A')} m/s")
        else:
            print("Invalid option. Please choose either 'temperature', 'humidity', or 'wind_speed'.")
    except Exception as e:
        print(f"Error displaying weather conditions: {e}")

def display_weather(data,option):
    try:
        if not data:
            print("Error: No data received.")
            return
            
        weather = data.get('main', {})
        wind = data.get('wind', {})
        if not wind:
            print("Error: Wind data is missing.")
            return
        display_weather_conditions(weather, wind, option)
        
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except KeyError as e:
        print(f"Key error: Missing key {e} in the weather data.")
    except TypeError as e:
        print(f"Type error: Incorect data format encountered. {e}")
    except ValueError as e:
        print(f"Value error: {e}")
    except Exception as e:
        print(f"An unexcpected error occurred: {e}")

def get_arguments():
    parser = argparse.ArgumentParser(description="Get weather data for a specified city.")
    parser.add_argument("city", type=str, help="The name of the city to get weather information for.")
    parser.add_argument(
        "option",
        choices=AVAILABLE_OPTIONS.keys(),
        help="The weather parameter to fetch ('temperature', 'humidity', or 'wind_speed')."
    )
    return parser.parse_args()

def main():
    args = get_arguments()
    if not args.city.strip():
        print("City name cannot be empty.")
        return
    data = fetch_weather_data(args.city)
    if data:
        display_weather(data, args.option)
    
if __name__ == '__main__':
    main()
