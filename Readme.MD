# Welkom to this page!
Here you can find my project for Bitcoin Scraper.
First I going to explain what you can see on this Github page and then I will explain how that you can use this scraper.

## Github

#### Code:
Here you can find the code that I wrote.

#### Projects:
Here you can find a to do list.
You can see step by step what I did in this tool.

#### Wiki:
Here you can find all the sources that helped me in making this tool.
- On page 1: you can find how that I got started with the tools.
- On page 2: I wrote the frequently used commands.

#### Releases:
Here you can find all the updates.
You can find also the update here under.


# What is this tool?
As you have probably already read, this tool is a scraper that scrape the first 50 hashes and then it will keep the best 5 hashes in MongoDB.

These are the steps that the tool will make if you run it.

1) Input how many minutes you want the tool to run (fe: 1 = 1 minute).

2) Scraping 50 hashes.

3) Putting 50 hashes in a dataframe and sorting it.

4) Adding the 5 first(= highest bitcoin value) hashes to redis (caching all the data because the next run of the tool the dataframe will be resseted).

5) The tool will now 60 seconds wait.

6) If the tool has ran all the loops, it will add it then to MongoDB.

There is also an bash file that you can use to start the MongoDB server and the Redis server.
- Bash_File_Scraper_0.sh: Startup MongoDB server.
- Bash_File_Scraper_1.sh: Startup Redis server.

## Import files
For running this tool i used these import files:

#### For scraping the site
Scraping import files:
- Requests: for requesting the url.
- Bs4 (BeautifulSoup): Getting the site data.
#### Data
For making the databese
- Pandas: Making databeses
- Regex: To delete and find words
- Pymongo: Connecting to MongoDB server
- Redis: Connecting to Redis server
- Ast: Converting byte to dict
#### Helping for scraping
- Time: realtime scraping

# Updates
Bitcoin_Scraper 0.0: Printing 50 sorted hashes (highest bitcoin value above).

Bitcoin_Scraper 0.1: Realtime printing (every minute) and printing top 5 hashes.

Bitcoin_Scraper 0.1.1: User input for haw long the tool will run.

Bitcoin_Scraper 1.0: Adding bash file for helping startup server MongoDB.

Bitcoin_Scraper 1.1: Adding data to database in MongoDB.

Bitcoin_Scraper 2.0: Cache data to Redis server and then to MongoDB server.

Bitcoin_Scraper 3.0: Adding txt file explaining what I did in Docker.