# Welkom to this page!
Here you can find my project for Bitcoin Scraper.
First I going to explain what you can see on this Github page and then I will explain how that you can use this scraper.

## Github
What in this Github page?

**Code**
Here you can find the code that I wrote.
**Projects**
Here you can find a to do list.
You can see step by step what I did in this tool
**Wiki**
Here you can find all the sources that helped me in making this tool.
- On page 1 you can find how that I got started with the tools.
- On page 2 I wrote the frequently used commands.


## What is this tool?
- First you have to fill in haw many munites you want that the tool will run.
- Than it wil scrape every minute 50 hashes and it will sort all the observation (highest bitcoin value above).
    I used BeautifulSoup for scraping the site and pandas and regex to edit the data (More info in "Import files").
- After that it will store the best 5 hashes in a cashe server of Redis
- If the tool has finiched, it will add alle the cashe data to MongoDB.

You can find all the sources in the wiki page in Github.

There is also an bash file that you can use to start the MongoDB server and the Redis server.
- Bash_File_Scraper_0.sh: Startup MongoDB server
- Bash_File_Scraper_1.sh: Startup Redis server

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

Bitcoin_Scraper 2.0: Cache data to Redis server and then to MongoDB server.

Bitcoin_Scraper 3.0: Adding txt file explaining what I did in Docker.