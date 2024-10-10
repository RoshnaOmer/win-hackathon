# Enhanced Social Media and E-commerce Detector aka ([WIN, the Hackathon!](https://cros.ec.europa.eu/book-page/win-hackathon))
*Created on October 9, 2024*

## Overview
This project is a submission for the Web Intelligence Network (WIN) Hackathon, which aims to improve Official Statistics by automatically detecting E-commerce and Social Media presence on business websites from four different countries. Our solution provides comprehensive analysis while adhering to ethical web scraping principles.

## Disclaimer
This project was developed with the assistance of Claude 3.5 Sonnet, an AI language model by Anthropic. The conversation that led to this implementation is summarized using Claude Sonnet in [CONVERSATION.md](CONVERSATION.md) and a human (me) took a screenshot of the whole convo, it is available in [this file](screencapture-claude-ai-chat-2024-10-09.pdf).

## Features
- Ethical web scraping following industry best practices
- Advanced e-commerce detection using multiple indicators
- Validation of seven social media platforms with URL unshortening
- Country-specific analysis and insights
- Correlation analysis between e-commerce and social media presence
- Comprehensive visualization of results

## Hackathon Context
The Web Intelligence Network has developed this challenge to identify E-commerce and Social Media use from publicly available web data. The goal is to create open-source software that can automatically derive Online Business Enterprise Characteristics (OBEC) while adhering to the highest ethical standards.

### The result of the 2nd version of the code which includes e-commerce is:
![image](https://github.com/user-attachments/assets/e4885ee1-03de-49eb-9c33-63cce0e8b0d9)

### The result of the 1nd version of the code which did not include e-commerce is:
![image](https://github.com/user-attachments/assets/8048d88a-cce2-4339-b9bc-1393293235df)

## Implementation Details

### E-commerce Detection
Our solution identifies e-commerce activity using multiple indicators:
1. Payment options (credit card, PayPal, etc.)
2. Shopping elements (cart, checkout, etc.)
3. Pricing patterns (currency symbols, price lists)
4. E-commerce platforms (Shopify, WooCommerce, etc.)
5. Booking services (travel, accommodation)
6. Subscription services (digital subscriptions, streaming)

We also handle "unusual" online shops as specified in the hackathon guidelines:
- Insurance websites
- Accommodation booking
- Food delivery services
- Subscription services
- Transport service providers

### Social Media Detection
Our approach:
1. Identifies social media links using pattern matching
2. Unshortens URLs (handles bit.ly, TinyURL, etc.)
3. Validates social media profiles to ensure they belong to the company
4. Handles various URL formats for each platform

Supported platforms:
- Facebook
- LinkedIn
- X (Twitter)
- Instagram
- TikTok
- YouTube

### Technical Approach
1. **Ethical Web Scraping**:
   - Clear User Agent string with contact information
   - Rate limiting with random delays
   - Respects robots.txt
   - Minimal data collection

2. **URL Processing**:
   - Handles relative URLs
   - Unshortens shortened URLs
   - Validates social media profile existence

3. **Analysis**:
   - Country-specific insights
   - Correlation between e-commerce and social media
   - Comprehensive visualizations

## Dependencies
```
pandas
requests
beautifulsoup4
tqdm
matplotlib
seaborn
```

## Installation
```bash
pip install pandas requests beautifulsoup4 tqdm matplotlib seaborn
```

## Usage

### 1. Input File
The script uses the provided `input.csv` file with columns:
- id: Unique identifier
- url: Website URL
- country: Country code
- ecommerce: E-commerce indicator (updated by script)
- sm_fb, sm_linkedin, sm_x, sm_insta, sm_tiktok, sm_yt: Social media indicators

### 2. Run the Scraper
```bash
python scraper.py
```

### 3. Analyze Results
```bash
python analyzer.py
```

## Output
1. **results.csv**: Contains original columns updated with:
   - ecommerce: [0,1] for e-commerce activities
   - Social media indicators: [0,1] for each platform

2. **Analysis**:
   - Console output with detailed statistics
   - Visualizations:
     1. Social Media Platform Popularity
     2. E-commerce Presence by Country
     3. Average Social Media Platforms by Country
     4. Correlation Heatmap

## Pros and Cons

### Pros:
1. Highly ethical implementation following best practices
2. Comprehensive e-commerce detection using multiple indicators
3. Handles URL shorteners and various URL formats
4. Provides country-specific insights
5. Correlation analysis between e-commerce and social media

### Cons:
1. Rate limiting means slower processing
2. Cannot handle JavaScript-rendered content
3. May miss some indicators due to ethical constraints
4. Limited to publicly accessible pages
5. Dependency on external services for URL unshortening

## License
[MIT License](LICENSE)

