#!/bin/bash

# clearing the window
clear

# Starting the script
echo "Starting shell script"

# Starting MongoDB server
mongod
# Starting the shell
mongo

echo "Ending shell script"

# Printing whats in the bash file
cat bash_file_scraper.sh