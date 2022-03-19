# What is this tool?
- First you have to fill in haw many munites you want that the tool will run.
- Than it wil scrape every minute 50 hashes and it will sort all the observation (highest bitcoin value above).
    I used BeautifulSoup for scraping the site and pandas and regex to edit the data (More info in "Import files").
- After that it will store the best 5 hashes in a cashe server of Redis
- If the tool has finiched, it will add alle the cashe data to MongoDB.

You can find all the sources in the wiki page in Github.

There is also an bash file that you can use to start the MongoDB server and the Redis server.
- Bash_File_Scraper.sh: Startup MongoDB server
- Bash_File_Scraper2.sh: Startup Redis server

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
- Pymongo: Connecting to MongoDB server
- Redis: Connecting to Redis server
- Ast: Converting byte to dict
### Helping for scraping
- Time: realtime scraping

# Updates
Bitcoin_Scraper 0.0: Printing 50 sorted hashes (highest bitcoin value above).

Bitcoin_Scraper 0.1: Realtime printing (every minute) and printing top 5 hashes.

Bitcoin_Scraper 0.1.1: User input for haw long the tool will run.

Bitcoin_Scraper 1.0: Adding bash file for helping startup server MongoDB.

Bitcoin_Scraper 1.1: Adding data to database in MongoDB.

Bitcoin_Scraper 2.0: Cache data to Redis server and then to MongoDB server