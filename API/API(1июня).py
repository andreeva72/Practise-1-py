import requests
import sys
from config import API_KEY

def news(query='python', language='ru', page_size=15):
    url="https://newsapi.org/API2/everithing"
    params = {
        "q":query,
        "language":language,
        "sortBy": "publishedAt",
        "page_size": page_size,
        "apiKey": API_KEY,
    }
    try:
        responce = requests.get(url, params=params, timeout=10)
        responce.raise_for_status()
        data = responce.json()
        