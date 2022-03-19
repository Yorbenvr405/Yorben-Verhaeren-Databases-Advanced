# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# ---- importing imports ----

import requests
from bs4 import BeautifulSoup
import pandas as pd
import regex as re
import time
import pymongo as mongo
import redis
import ast

# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# ---- making the dataframe ----

print('Enter how many min you want that the tool will run:') # ask user how many minutes the tool must run
number_minutes = input() # asking user for the minutes
min_input = int(number_minutes) # converting string to int
counter = 0 # setting the counter

while counter < min_input:

    # --- Scraping data ---
    url = "https://www.blockchain.com/btc/unconfirmed-transactions"
    bit_data = requests.get(url)
    bit_hash = BeautifulSoup(bit_data.text, features="html.parser")
    finddiv1 = bit_hash.findAll('div', attrs={"class" : "sc-1g6z4xm-0 hXyplo"})

    # --- Making the lists ---

    hash_list = [] # scraping whole line with hash, time and price

    hash_temp = [] # Making the hash
    hashes_list = [] # Adding all hashes

    time_list = [] # Adding all time
    BTC_list = [] # Adding all BTC
    USD_list = [] # Adding all USD

    # Scraping of 50 lines of hashing
    for i in range(0, 50):
        hash_line = finddiv1[i]

        hash_list.append(hash_line.text)

    for i in range(0 , 50):
        # Setting the hashes
        hash_temp = hash_list[i].split("Time") # keeping only the hash
        hash = hash_temp[0].split("Hash") # removing the word hash
        hashes_list.append(hash[1]) # adding the hashes to the list

        time_temp = hash_temp[1] # using the other half of the splitted text
        time_temp1 = time_temp.split("Amount") # splitting on amount (becouse splitting on amount btc and usd also splitted)
        time_list.append(time_temp1[0]) # adding the value to the list

        btc_temp = time_temp1[1] # using the other half of the splitted text
        btc_temp1 = btc_temp.split(')') # splitting to get the BTC
        btc = re.sub("BTC", "", btc_temp1[1]) # replace the BTC with nothing
        BTC_list.append(btc) # adding the BTC to the list

        USD_temp = time_temp1[2] # using the third half
        USD_temp1 = USD_temp.split(')') # splitting to get the USD
        USD_list.append(USD_temp1[1]) # adding to the list

    hash_bit = [] # making a list to put in an other list for the dataframe

    for i in range(0, 50):
        hash_bit_temp = [] # Ramaking the list and adding the values

        hash_bit_temp.append(hashes_list[i])
        hash_bit_temp.append(time_list[i])
        hash_bit_temp.append(BTC_list[i])
        hash_bit_temp.append(USD_list[i])

        hash_bit.append(hash_bit_temp) # adding the list to the other list

    result_df = pd.DataFrame (hash_bit, columns = ['Hash', 'Time', 'Amount (BTC)', 'Amount (USD)']) # making the dataframe
    result_df = result_df.astype({'Hash': str, 'Time': str, 'Amount (BTC)': float, 'Amount (USD)': str}) # setting the types of ech collumn

    result_df = result_df.sort_values(by=['Amount (BTC)'], ascending=False, ignore_index=True) # sorting the dataframe on Amount (BTC)


    # ----------------------------------------------------------------------------------------------------------------------------------------------------------- #
    # Adding data to Redis

    data_json = result_df[0:5].to_json() # converting data to json

    r = redis.StrictRedis(host='localhost', port=6380, db=0) # connecting to Redis server

    if counter == 0:
        r.delete("data") # if there is still data in the cache: remove it
        r.lpush("data", data_json) # adding new data to server

    else:
        r.lpush("data", data_json) # adding new data to server
    
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------- #
    # Preparing for next loop

    time.sleep(60) # wait 60 seconds for next scraping
    
    counter = counter + 1  # going to next minute for scraper

    print("Loop: " + str(counter)) # Logging that there has been looped a loop

# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# Getting data from Redis server

rehydrated_df = r.lrange("data", 0, min_input) # Getting all data from Redis server

for i in range(0, min_input): # converting byte to dict
    dict_str = rehydrated_df[i].decode("UTF-8") # decoding byte
    mydata = ast.literal_eval(dict_str) # setting the dict

    rehydrated_df[i] = mydata # replacing the byte with the dict

# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# ---- connecting to databese ----
    
client = mongo.MongoClient("mongodb://127.0.0.1:27017") # connecting to MongoDB server
my_bit_database = client["Bitcoin_Database"] # Make new database
col_bitcoin = my_bit_database["Bitcoin"] # setting the collumn
insert_data = col_bitcoin.insert_many(rehydrated_df) # inserting the data