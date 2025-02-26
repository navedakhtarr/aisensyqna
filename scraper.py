import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    """Fetches and extracts text from a given webpage URL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract text from paragraphs
        paragraphs = soup.find_all("p")
        text = "\n".join([p.get_text() for p in paragraphs if p.get_text()])

        return text if text else "No readable content found."
    except Exception as e:
        return f"Error fetching content: {str(e)}"
