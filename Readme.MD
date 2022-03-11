# What is this tool?
- First you will tu fill in haw many munites you want that the tool will run.
- Than it wil scrape every minute 50 hashes and it will sort all the observation (highest bitcoin value above).
- In the terminal you can see the top 5 hashes that were made that time (More info in "What you will get").
    I used BeautifulSoup for scraping the site and pandas and regex to edit the data (More info in "Import files").

## Import files
For running this tool i used these import files:

### For scraping the site
Scraping import files:
- Requests: for requesting the url.
- Bs4 (BeautifulSoup): Getting the site data.
### Data
For making the databese
- Pandas: Making databeses
- Regex: To delete and find words
### Helping for scraping
- Time: realtime scraping

## What you will get
A dataframe with all the 5 maximum observations in the terminal (highest bitcoin value above).

# Updates
Bitcoin_Scraper 0.0: Printing 50 sorted hashes (highest bitcoin value above).

Bitcoin_Scraper 0.1: Realtime printing (every minute) and printing top 5 hashes.

Bitcoin_Scraper 0.1.1: User input for haw long the tool will run.