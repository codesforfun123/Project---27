import requests
import logging
from bs4 import BeautifulSoup

class WikipediaScraper:
    def __init__(self):
        self.base_url = "https://en.wikipedia.org/wiki/"
        # Configure logging
        logging.basicConfig(filename='wikipedia_scraper.log', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def fetch_page_content(self, topic):
        url = self.base_url + topic
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            if response.status_code == 200:
                return response.text
            else:
                logging.error(f"Failed to fetch content for '{topic}'. Status code: {response.status_code}")
                return None
        except requests.RequestException as e:
            logging.error(f"Error occurred while fetching content for '{topic}': {str(e)}")
            return None

    def extract_paragraphs(self, html_content):
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            paragraphs = soup.find_all('p')
            extracted_paragraphs = [p.text.strip() for p in paragraphs]
            return extracted_paragraphs
        except Exception as e:
            logging.error(f"Error occurred while extracting paragraphs: {str(e)}")
            return []

    def extract_tables(self, html_content):
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            tables = soup.find_all('table')
            # Extract table data here
            return tables
        except Exception as e:
            logging.error(f"Error occurred while extracting tables: {str(e)}")
            return []

    def extract_images(self, html_content):
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            images = soup.find_all('img')
            # Extract image URLs here
            return images
        except Exception as e:
            logging.error(f"Error occurred while extracting images: {str(e)}")
            return []

    # Add more extraction methods as needed

if __name__ == "__main__":
    scraper = WikipediaScraper()
    topic = input("Enter the topic you want to scrape from Wikipedia: ")
    page_content = scraper.fetch_page_content(topic)
    if page_content:
        paragraphs = scraper.extract_paragraphs(page_content)
        tables = scraper.extract_tables(page_content)
        images = scraper.extract_images(page_content)
        # Process and utilize extracted data
