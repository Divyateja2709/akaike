import requests

def fetch_news(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except Exception as e:
        print(f"Error fetching news: {e}")
        return None

def clean_text(text):
    text = text.replace('\n', ' ').strip()
    return text
