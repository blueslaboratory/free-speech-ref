# UPDATED: 27/09/2024

from dotenv import load_dotenv
import os

from requests_oauthlib import OAuth1Session


def twitter_login_v1():
    # Load environment variables from .env file
    load_dotenv()
    
    # API Tokens
    API_KEY = os.getenv('API_KEY')
    API_KEY_SECRET = os.getenv('API_KEY_SECRET')
    ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
    ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
    
    # Create OAuth 1.0a session
    twitter = OAuth1Session(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    
    return twitter