# UPDATED: 20/09/2024

import tweepy


# USE: twitter_login_v2
def twitter_login_v2(bearer_token):
    """
    Authenticate to Twitter using the API v2 and return the Client object.
    
    Args:
    - bearer_token: Twitter API v2 Bearer Token.
    
    Returns:
    - client: tweepy Client object for interacting with Twitter API v2.
    """
    # Create and return the Tweepy Client object
    client = tweepy.Client(bearer_token=bearer_token)
    
    return client