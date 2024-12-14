import requests
import json
import time

def get_data():
    url = "https://api.coincap.io/v2/assets"
    params = {"limit": 20}  
    try:
        response = requests.get(url, params=params)
        datas = response.json()
        if response.status_code == 200:
            return datas['data']
    except Exception as e:
        print(f"Error fetching data: {e}")
        exit()

def filter_name(datas, name):
    return [i for i in datas if name.lower() in i["name"].lower()]

def filter_value(datas, value):
    return [i for i in datas if float(i["priceUsd"]) > value]

def output_data(datas):
    for data in datas:
        name = data['name']
        symbol = data['symbol']
        price = data['priceUsd']
        market_cap = data['marketCapUsd']
        volume = data['volumeUsd24Hr']
        change_percent = data['changePercent24Hr']
        
        print(f"Name: {name}")
        print(f"Symbol: {symbol}")
        print(f"Current Price: ${price}")
        print(f"Market Cap: ${market_cap}")
        print(f"Total Volume: ${volume}")
        print(f"Price Change (24h): {change_percent}%")
        print("------------------------------------")

def main():
    while True:
        datas = get_data()
        print("Select filter options:")
        print("1. Filter by name")
        print("2. Filter by value (price > XXX)")
        print("3. No filter, show all")
        choice = input("Enter your choice (1, 2, or 3): ")
        if choice == "1":
            name = input("Enter the name of the cryptocurrency to search for (e.g., Bitcoin): ")
            if name:
                data = filter_name(datas, name)
                output_data(data)
        elif choice == "2":
            value = input("Enter the price value to filter by (e.g., 1000): ")
            if value.isdigit():
                data = filter_value(datas, float(value))
                output_data(data)
        elif choice == "3":
            output_data(datas)
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")
        time.sleep(5)

if __name__ == "__main__":
    main()
