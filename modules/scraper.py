import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import re
import json

class WebScraper:
    def __init__(self):
        self.ua = UserAgent()
        self.session = requests.Session()
        
    def setup_driver(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument(f'user-agent={self.ua.random}')
        return webdriver.Chrome(options=options)
    
    def search(self, query):
        results = []
        
        # Google dorks
        dorks = [
            f'site:facebook.com "{query}"',
            f'site:twitter.com "{query}"',
            f'site:linkedin.com "{query}"',
            f'site:instagram.com "{query}"',
            f'site:github.com "{query}"',
            f'site:pinterest.com "{query}"',
            f'"{query}" filetype:pdf',
            f'"{query}" filetype:doc',
            f'"{query}" site:pastebin.com',
            f'"{query}" site:haveibeenpwned.com'
        ]
        
        for dork in dorks:
            try:
                data = self.google_search(dork)
                results.extend(data)
            except:
                continue
                
        return results
    
    def google_search(self, query):
        url = f"https://www.google.com/search?q={query}"
        headers = {'User-Agent': self.ua.random}
        response = self.session.get(url, headers=headers)
        
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []
        
        for g in soup.find_all('div', class_='g'):
            anchors = g.find_all('a')
            if anchors:
                link = anchors[0]['href']
                title = g.find('h3').text if g.find('h3') else ''
                snippet = g.find('span', class_='aCOpRe').text if g.find('span', class_='aCOpRe') else ''
                results.append({
                    'title': title,
                    'url': link,
                    'snippet': snippet
                })
        
        return results
    
    def get_metadata(self, target):
        # Extraction de metadata depuis différentes sources
        metadata = {
            'emails': self.extract_emails(target),
            'phones': self.extract_phones(target),
            'addresses': self.extract_addresses(target),
            'user_ids': self.extract_user_ids(target)
        }
        return metadata
    
    def extract_emails(self, text):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.findall(pattern, text)
    
    def extract_phones(self, text):
        pattern = r'(\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
        return re.findall(pattern, text)
    
    def extract_addresses(self, text):
        # Patterns pour adresses
        return []
    
    def extract_user_ids(self, text):
        # Patterns pour IDs
        return []
