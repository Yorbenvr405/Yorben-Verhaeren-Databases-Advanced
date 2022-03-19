# ---- This is the bash_file_scraper2.sh ----

# clearing the window
clear

# Starting the script
echo "Starting shell script";

# Starting Redis server
redis-server --port 6380;

# Testing if server works
redis-cli ping;

echo "Ending shell script";

# Printing whats in the bash file
cat bash_file_scraper2.sh