# Ethical Social Media Presence Checker
*Created on October 9, 2024*

## Overview
This project provides an ethical web scraping solution to analyze the social media presence of websites listed in a CSV file. The implementation follows ethical web scraping guidelines and provides comprehensive analysis of the results.

## Disclaimer
This project was developed with the assistance of Claude 3.5 Sonnet, an AI language model by Anthropic. The conversation that led to this implementation is available in [CONVERSATION.md](CONVERSATION.md).

## Features
- Ethical web scraping following industry best practices
- Concurrent processing with rate limiting
- Comprehensive results analysis with visualizations
- Respects robots.txt and implements delays between requests

## Components
1. Web Scraper (`scraper.py`)
2. Results Analyzer (`analyzer.py`)

## Ethical Considerations
This project adheres to ethical web scraping principles:
- Uses a clear User Agent string with contact information
- Implements rate limiting and random delays
- Respects robots.txt
- Minimizes data collection to only what's necessary
- Returns value through analysis and insights

## Dependencies
```
pandas
requests
beautifulsoup4
tqdm
matplotlib
```

## Installation
```bash
pip install pandas requests beautifulsoup4 tqdm matplotlib
```

## Usage

### 1. Prepare Input File
Ensure your input CSV file has the following columns:
- id
- url
- country
- ecommerce
- sm_fb
- sm_linkedin
- sm_x
- sm_insta
- sm_tiktok
- sm_yt

### 2. Run the Scraper
```bash
python scraper.py
```

### 3. Analyze Results
```bash
python analyzer.py
```

## Implementation Details

### Web Scraper
The scraper implements the following ethical practices:
- Respectful User Agent string
- Rate limiting (1-3 seconds between requests)
- Maximum 3 concurrent workers
- Robots.txt checking
- Minimal data collection
- Comprehensive error handling

### Results Analyzer
Provides:
- Detailed statistics on social media presence
- Visualization of platform distribution
- Analysis of platform popularity

## Output
The scraper generates a `results.csv` file with the following columns:
- All original columns
- Updated social media columns with 1 (present) or 0 (not found)

The analyzer provides:
- Console output with summary statistics
- Two visualizations:
  1. Distribution of social media platform count
  2. Platform popularity comparison

## Best Practices for Use
1. Update the User Agent string with your contact information
2. Consider running during off-peak hours
3. Adjust rate limiting based on target websites
4. Be prepared to respond to site owners' inquiries

## License
MIT

## Contributing
[Specify contribution guidelines if applicable]
