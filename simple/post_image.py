# 27/09/2024
# MINIMAL VERSION WORKING

from auth import twitter_login_v1

# Authenticate the session
twitter = twitter_login_v1()



# Step 1: Upload the image
def upload_image(image_path):
    
    media_url = "https://upload.twitter.com/1.1/media/upload.json"
    
    # r: read, b: binary
    with open(image_path, 'rb') as image_file:
        files = {"media": image_file}
        response = twitter.post(media_url, files=files)
    
    if response.status_code == 200:
        media_id = response.json()["media_id_string"]
        print(f"Image uploaded successfully, media_id: {media_id}")
        return media_id
    else:
        print(f"Error uploading image: {response.status_code} - {response.text}")
        return None



# Step 2: Post tweet with the uploaded image
def post_tweet_with_image(media_id, tweet_text):
    tweet_url = "https://api.twitter.com/2/tweets"
    
    payload = {
        "text": tweet_text,
        "media": {
            "media_ids": [media_id]
        }
    }
    
    response = twitter.post(tweet_url, json=payload)
    
    if response.status_code == 201:
        print("Tweet posted successfully!")
        print(response.json())
    else:
        print(f"Error posting tweet: {response.status_code} - {response.text}")



# Main execution
# image_path = "./img/warning/warning_2.jpg"
image_path = "./img/coin_toss.jpg"
tweet_text = "LET THE MATCH BEGIN"

# Upload the image and post the tweet
media_id = upload_image(image_path)

if media_id:
    post_tweet_with_image(media_id, tweet_text)