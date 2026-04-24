import feedparser
from bs4 import BeautifulSoup
import requests

RSS_URL = "https://news.google.com/rss/search?q=PlayStation+AND+(PS5+OR+Sony+OR+juegos)&hl=es-419&gl=AR&ceid=AR:es-419"

def fetch_latest_news():
    """Fetches the latest news from the RSS feed."""
    print("Buscando noticias en Google News...")
    feed = feedparser.parse(RSS_URL)
    
    articles = []
    for entry in feed.entries[:5]: # Get top 5 recent
        articles.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.published,
        })
    return articles

def extract_article_content(url):
    """Attempts to extract the main text content and image from a URL."""
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, timeout=10, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract text content
        paragraphs = soup.find_all('p')
        content = "\n".join([p.get_text() for p in paragraphs if len(p.get_text()) > 20])
        
        # Extract image
        image_url = ""
        og_image = soup.find("meta", property="og:image")
        if og_image and og_image.get("content"):
            image_url = og_image.get("content")
        elif soup.find("img"): # fallback to first image
            first_img = soup.find("img")
            if first_img.get("src") and first_img.get("src").startswith("http"):
                image_url = first_img.get("src")
                
        return content, image_url
    except Exception as e:
        print(f"Error extrayendo {url}: {e}")
        return "", ""
