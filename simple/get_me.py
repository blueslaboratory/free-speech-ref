# 27/09/2024
# MINIMAL V2 WORKING

from auth import twitter_login_v1

# Authenticate the session
twitter = twitter_login_v1()

# Endpoint URL:
url = "https://api.twitter.com/2/users/me"

# GET petition to the Twitter/X API
response = twitter.get(url)

# Verify if petition successful
if response.status_code == 200:
    user_data = response.json()
    
    print("User data:")
    for k,v in user_data['data'].items():
        print(k, v)
    
else:
    print(f"Error: {response.status_code} - {response.text}")