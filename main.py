# UPDATED: 20/09/2024

from dotenv import load_dotenv
import os

from auth import twitter_login_v2
import tweepy



# Carga las variables de entorno del archivo .env
load_dotenv()

# API v2 Bearer Token
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

# Authenticate to Twitter API v2
client = twitter_login_v2(BEARER_TOKEN)


def get_my_info():
    """Fetch authenticated user's information."""
    try:
        response = client.get_me()
        if response.data:
            print(f"User Info for ME: {response.data}")
        else:
            print("No data returned for the authenticated user.")
    except Exception as e:
        print(f"An unexpected error occurred while getting user info: {e}")



def get_user_info(username):
    """Fetch user information using their username."""
    try:
        response = client.get_user(username=username)
        if response.data:
            print(f"User Info for {username}: {response.data}")
        else:
            print("User not found.")
    except Exception as e:
        print(f"Failed to get user info: {e}")



def post_tweet(content):
    """Post a tweet using the API v2."""
    try:
        response = client.create_tweet(text=content)
        print(f"Tweet posted successfully: {response.data}")
    except tweepy.TweepyException as e:
        print(f"Failed to post tweet: {e}")



# X Free Products: https://developer.x.com/en/portal/products

# Get my account info
# get_my_info()

# Replace 'username_here' with the username you want to look up
username = 'free_speech_ref'
get_user_info(username)

# Example tweet posting
tweet_content = "Hello World! This is a test tweet from my bot."
post_tweet(tweet_content)