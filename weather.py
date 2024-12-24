import requests
import argparse
API_KEY = '40e151f43a8da63402abb3c21eaeabbb'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
AVAILABLE_OPTIONS = {
    'temperature': 'Temperature (in Celsius)',
    'humidity': 'Humidity (%)',
    'wind_speed': 'Wind Speed (m/s)',
}


def get_weather(city, option=None):
    try:
        url = f'{BASE_URL}?q={city}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Error: Unable to get data for city '{city}',Status code: {response.status_code}")
            return
        data = response.json()
        if data.get('cod') != 200:
            print(f"Error: City '{city}' not found.")
            return
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
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except ValueError as e:
        print(f"Value error: {e}")
    except KeyError as e:
        print(f"Key error: {e}")
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
    if not args.city:
        print("City name cannot be empty.")
        return
    get_weather(args.city,args.option)
    
if __name__ == '__main__':
    main()
