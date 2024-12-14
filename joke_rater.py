import requests
import random
import time
import json

def fetch_joke(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        return response.json()  
    except requests.exceptions.RequestException as e:
        print(f"Error request: {e}")
        return None

def get_jokes(url, num_jokes=10):
    jokes = []
    for i in range(num_jokes):
        joke_data = fetch_joke(url)
        if joke_data:
            joke = joke_data.get('setup') + " " + joke_data.get('punchline')  
            if joke:
                jokes.append(joke)
        time.sleep(1) 
    return jokes

def rate_jokes(jokes):
    ratings = random.sample(range(1, 11), len(jokes)) 
    rated_jokes = []
    for joke, rating in zip(jokes, ratings):
        rated_jokes.append({"joke": joke, "rating": rating})
    return rated_jokes

def save_jokes_to_file(rated_jokes, filename='top_jokes.txt'):
    rated_jokes.sort(key=lambda x: x['rating'], reverse=True)
    with open(filename, 'w', encoding='utf-8') as f:
        for joke in rated_jokes:
            f.write(f"Joke: {joke['joke']}\nRating: {joke['rating']}\n")
    print(f"Jokes alredy ratered in {filename}.")

def main():
    url = "https://official-joke-api.appspot.com/random_joke"  
    filename = "top_jokes.txt" 
    jokes = get_jokes(url, num_jokes=10)  
    rated_jokes = rate_jokes(jokes)  
    save_jokes_to_file(rated_jokes, filename)

if __name__ == "__main__":
    main()
