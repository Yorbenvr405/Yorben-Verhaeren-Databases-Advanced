# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# ---- importing imports ----

import requests
from bs4 import BeautifulSoup
import pandas as pd
import regex as re
import time
import pymongo as mongo

import pyarrow as pa
import redis
import pickle
import zlib

# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# ---- making the dataframe ----

# ask user how many minutes the tool must run
print('Enter how many min you want that the tool will run:')
#number_minutes = input() # asking user for the minutes
number_minutes = 2
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

    # making the dataframe
    result_df = pd.DataFrame (hash_bit, columns = ['Hash', 'Time', 'Amount (BTC)', 'Amount (USD)'])
    # setting the types of ech collumn
    result_df = result_df.astype({'Hash': str, 'Time': str, 'Amount (BTC)': float, 'Amount (USD)': str})

    # sorting the dataframe on Amount (BTC)
    result_df = result_df.sort_values(by=['Amount (BTC)'], ascending=False, ignore_index=True)


    # --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
    


    data_json = result_df[0:5].to_json()

    r = redis.StrictRedis(host='localhost', port=6380, db=0)

    if counter == 0:
        r.delete("data")
        r.append("data", data_json)
        rehydrated_df = r.get("data")
    else:
        r.append("data", data_json)
        rehydrated_df = r.get("data")

    print(rehydrated_df)
    
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------- #

    # wait 60 seconds for next scraping
    time.sleep(2)
    
    # going to next minute for scraper
    counter = counter + 1

    # --------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# ---- connecting to databese ----
    
client = mongo.MongoClient("mongodb://127.0.0.1:27017")
# Make new database
my_bit_database = client["Bitcoin_Database"]
# converting data to json
json_data_bit = result_df[0:5].to_dict("lines")
# setting the collumn
col_bitcoin = my_bit_database["Bitcoin"]
# inserting the data
insert_data = col_bitcoin.insert_one(json_data_bit)

# printing the dataframe
print(result_df[0:5])

# add a enter for next scraping
print()