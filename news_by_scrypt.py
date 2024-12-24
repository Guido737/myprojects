import requests
import argparse
#8345c95a63644a2f92b60f44ebaa5d3c
def get_news(api_key, query=None, category=None):
    try:
        params = {
            'apiKey': api_key,
            'language': 'en',
            'pageSize': 5,
            'q': query,
            'category': category
        }
        response = requests.get('https://newsapi.org/v2/top-headlines', params={k: v for k, v in params.items() if v})
        if response.status_code == 200:
            return response.json().get('articles', [])
        else:
            print(f"Error: Failed to fetch news.Status code: {response.status_code}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error: Request failed: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []

def save_to_file(news):
    try:
        with open('news_today.txt', 'w', encoding='utf-8') as f:
            for idx, article in enumerate(news, 1):
                f.write(f"{idx}. {article['title']}\nSource: {article['source']['name']}\nPublished: {article['publishedAt']}\nLink: {article['url']}\n\n")
        print("News saved to file.")
    except Exception as e:
        print(f"Error saving to file: {e}")

def get_arguments():
    parser = argparse.ArgumentParser(description="Fetch and save the top news articles.")
    parser.add_argument("api_key", help="API key for NewsAPI")
    parser.add_argument("-q", "--query", help="Keyword to search for in the news articles", default=None)
    parser.add_argument("-c", "--category", help="Category of the news(e.g. business,sports,technology)", default=None)
    return parser.parse_args()

def main():
    args = get_arguments()
    if not args.api_key:
        print("Error: API key is required.")
        return
    news = get_news(args.api_key,args.query,args.category)
    if news:
        save_to_file(news)
        for idx, article in enumerate(news, 1):
            print(f"{idx}. {article['title']}\n{article['source']['name']} - {article['publishedAt']}\n{article['url']}\n")
    else:
        print("No news found.")

if __name__ == "__main__":
    main()
