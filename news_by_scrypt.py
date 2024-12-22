import requests

def get_news(api_key, query=None, category=None):
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
    print(f"Error: {response.status_code}")
    return []

def save_to_file(news):
    with open('news_today.txt', 'w', encoding='utf-8') as f:
        for idx, article in enumerate(news, 1):
            f.write(f"{idx}. {article['title']}\nSource: {article['source']['name']}\nPublished: {article['publishedAt']}\nLink: {article['url']}\n\n")
    print("News saved to file.")

def main():
    api_key = '8345c95a63644a2f92b60f44ebaa5d3c'
    query = input("Enter keyword or press Enter to skip: ")
    category = input("Enter category or press Enter to skip: ").lower()
    
    if not query and not category:
        print("Enter at least a keyword or category.")
        return
    
    news = get_news(api_key, query if query else None, category if category else None)
    if news:
        save_to_file(news)
        for idx, article in enumerate(news, 1):
            print(f"{idx}. {article['title']}\n{article['source']['name']} - {article['publishedAt']}\n{article['url']}\n")
    else:
        print("No news found.")

if __name__ == "__main__":
    main()
