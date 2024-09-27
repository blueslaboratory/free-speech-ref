# UPDATED: 20/09/2024

from user import User
from datetime import datetime, timedelta


class Monitor:

    
    def __init__(self):
        # Dictionary of users and their warning states
        self.users = {}



    def monitor_tweet(self, tweet, username):
        """Monitor a tweet for infringements."""
        
        # Does the tweet infringe?
        if self.detect_infringement(tweet):
            
            if username not in self.users:
                self.users[username] = User(username)

            user = self.users[username]
            
            # this should not be current_time but x_post_time
            current_time = datetime.now() 
            
            if user.last_infringement_time is not None:
                time_since_last_infringement = (current_time - user.last_infringement_time).total_seconds()
                
                if time_since_last_infringement >= (24*60*60):
                    user.reset_warnings()
            
            msg, img = user.issue_warning()
            
            self.respond_to_infringement(username, msg, img)



    # Logic for infringement detection (LLM or keyword-based)
    def detect_infringement(self, tweet):
        
        # Use raw string or forward slashes for the file path: platform compatibility
        profanity_words = self.load_profanity_words(r'./profanity_words/en.txt')
        
        # Split tweet into words and convert to lowercase
        tweet_words = set(tweet.lower().split())
        
        # True if there's any overlap
        overlap = not tweet_words.isdisjoint(profanity_words)
        
        return overlap
        
        
    
    def load_profanity_words(file_path):
        
        with open(file_path, 'r', encoding='utf-8') as file:
            # Using set for faster lookups
            profanity_words = set(line.strip() for line in file if line.strip())  
            
        return profanity_words



    def respond_to_infringement(self, username, msg, img):
        
        print(f"Responding to {username} with {img}")
        print(f"Message: {msg}")



    def cleanup_inactive_users(self):
        current_time = datetime.now()
        
        # key, value --> username, user
        for username, user in list(self.users.items()):
            if (current_time - user.last_infringement_time).total_seconds() > 24*60*60:
                del self.users[username]