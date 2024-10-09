import pandas as pd
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import concurrent.futures
import logging
from tqdm import tqdm

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SocialMediaChecker:
    def __init__(self):
        self.social_media_patterns = {
            'sm_fb': ['facebook.com', 'fb.com'],
            'sm_linkedin': ['linkedin.com'],
            'sm_x': ['twitter.com', 'x.com'],
            'sm_insta': ['instagram.com'],
            'sm_tiktok': ['tiktok.com'],
            'sm_yt': ['youtube.com']
        }
        
    def check_url(self, row):
        url = row['url']
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            results = {
                'id': row['id'],
                'url': row['url'],
                'country': row['country'],
                'ecommerce': row['ecommerce']
            }
            
            # Find all links
            links = [a.get('href', '') for a in soup.find_all('a', href=True)]
            
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
            return None

def process_csv(input_file, output_file, max_workers=5):
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    checker = SocialMediaChecker()
    results = []
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Create a list of futures
        futures = [executor.submit(checker.check_url, row) for _, row in df.iterrows()]
        
        # Process results as they complete
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
