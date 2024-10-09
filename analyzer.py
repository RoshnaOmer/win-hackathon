import pandas as pd
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import concurrent.futures
import logging
from tqdm import tqdm
import time
import random

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EthicalSocialMediaChecker:
    def __init__(self):
        self.social_media_patterns = {
            'sm_fb': ['facebook.com', 'fb.com'],
            'sm_linkedin': ['linkedin.com'],
            'sm_x': ['twitter.com', 'x.com'],
            'sm_insta': ['instagram.com'],
            'sm_tiktok': ['tiktok.com'],
            'sm_yt': ['youtube.com']
        }
        # Ethical user agent string
        self.headers = {
            'User-Agent': 'Ethical Web Scraper/1.0 (Educational Project; Contact: your@email.com)'
        }
        
    def check_url(self, row):
        url = row['url']
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        try:
            # Random delay between requests (1 to 3 seconds)
            time.sleep(random.uniform(1, 3))
            
            # First, check for robots.txt
            robots_url = urljoin(url, '/robots.txt')
            try:
                robots_response = requests.get(robots_url, headers=self.headers, timeout=5)
                if 'disallow: /' in robots_response.text.lower():
                    logging.info(f"Respecting robots.txt disallow for {url}")
                    return self.create_empty_result(row)
            except Exception:
                # If we can't check robots.txt, we'll proceed cautiously
                pass
            
            response = requests.get(url, headers=self.headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            results = {
                'id': row['id'],
                'url': row['url'],
                'country': row['country'],
                'ecommerce': row['ecommerce']
            }
            
            # Only look for social media links in the footer or header
            potential_sections = soup.find_all(['header', 'footer'])
            links = []
            for section in potential_sections:
                links.extend([a.get('href', '') for a in section.find_all('a', href=True)])
            
            # Check each social media platform
            for platform, patterns in self.social_media_patterns.items():
                found = 0
                for link in links:
                    if any(pattern in link.lower() for pattern in patterns):
                        found = 1
                        break
                results[platform] = found
                
            return results
            
        except Exception as e:
            logging.error(f"Error processing {url}: {str(e)}")
            return self.create_empty_result(row)

    def create_empty_result(self, row):
        return {
            'id': row['id'],
            'url': row['url'],
            'country': row['country'],
            'ecommerce': row['ecommerce'],
            **{platform: 0 for platform in self.social_media_patterns.keys()}
        }

def process_csv(input_file, output_file, max_workers=3):
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    checker = EthicalSocialMediaChecker()
    results = []
    
    # Limit the number of concurrent requests
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(checker.check_url, row) for _, row in df.iterrows()]
        
        for future in tqdm(concurrent.futures.as_completed(futures), total=len(futures)):
            result = future.result()
            if result:
                results.append(result)
    
    # Create results DataFrame and save to CSV
    results_df = pd.DataFrame(results)
    results_df.to_csv(output_file, index=False)
    logging.info(f"Results saved to {output_file}")

if __name__ == "__main__":
    input_file = 'input.csv'
    output_file = 'results.csv'
    process_csv(input_file, output_file)
