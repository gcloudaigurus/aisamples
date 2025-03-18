import requests
from bs4 import BeautifulSoup
from typing import Dict, List
import logging

class WebCrawler:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def crawl_page(self, url: str) -> Dict[str, str]:
        """
        Crawl a webpage and extract its content.
        
        Args:
            url (str): The URL to crawl
            
        Returns:
            Dict[str, str]: Dictionary containing title and content
        """
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'lxml')
            
            # Remove script and style elements
            for script in soup(['script', 'style']):
                script.decompose()
            
            # Get title
            title = soup.title.string if soup.title else url
            
            # Get main content (focusing on p, h1-h6, li tags)
            content_tags = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li'])
            content = ' '.join([tag.get_text().strip() for tag in content_tags])
            
            return {
                'url': url,
                'title': title,
                'content': content
            }
            
        except Exception as e:
            self.logger.error(f"Error crawling {url}: {str(e)}")
            return {
                'url': url,
                'title': 'Error',
                'content': f'Failed to crawl page: {str(e)}'
            }

    def crawl_multiple_pages(self, urls: List[str]) -> List[Dict[str, str]]:
        """
        Crawl multiple webpages.
        
        Args:
            urls (List[str]): List of URLs to crawl
            
        Returns:
            List[Dict[str, str]]: List of dictionaries containing crawled content
        """
        return [self.crawl_page(url) for url in urls] 