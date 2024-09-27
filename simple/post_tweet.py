# 27/09/2024
# MINIMAL VERSION WORKING

from auth import twitter_login_v1

# Authenticate the session
twitter = twitter_login_v1()

# Endpoints URL:
url = "https://api.twitter.com/2/tweets"

# The content of the tweet
tweet_data = {
    "text": (
        "Testing, testing, again..."
        "\nHello Maracana! This is my ? automated X post via API."
    )
}

# POST petition to the Twitter/X API
response = twitter.post(url, json=tweet_data)

# Verify if petition successful
if response.status_code == 200:
    print("Posted successfully!")
    
    tweet_response = response.json()
    print(tweet_response)
    
else:
    print(f"Error: {response.status_code} - {response.text}")