# 24/09/2024 
# MINIMAL VERSION - NOT WORKING

from dotenv import load_dotenv
import os

import tweepy


# Carga las variables de entorno del archivo .env
load_dotenv()

# API v2 Bearer Token
BEARER_TOKEN = os.getenv('BEARER_TOKEN')



# Authenticate to Twitter API v2
try:
    client = tweepy.Client(bearer_token=BEARER_TOKEN)
    print("Client authenticated successfully!")
except Exception as e:
    print(f"Authentication failed: {e}")



# Fetching my info
try:
    response = client.get_me()
    if response.data:
        print(f"My Info: {response.data}")
    else:
        print("No data returned for the authenticated user.")
except Exception as e:
    print(f"Error occurred: {e}")