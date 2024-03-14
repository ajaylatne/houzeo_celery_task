import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
api_key = os.getenv("API_KEY")

def current_news():
    data = requests.get(f'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={api_key}')
    return data.json()['articles']
