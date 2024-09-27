# UPDATED: 20/09/2024

import random
from datetime import datetime

class User:
    
    def __init__(self, username):
        self.username = username
        self.warnings = 0
        self.last_infringement_time = None
        self.infringement_count = 0



    def issue_warning(self):
        self.warnings += 1
        self.infringement_count += 1
        self.last_infringement_time = datetime.now()
        
        if self.warnings <= 3:
            warning_messages = {
                1: "1st warning: ⚠️\nYou are not been very kind",
                2: "2nd warning: ⚠️⚠️\nWatch your mouth!",
                3: "3rd warning: ⚠️⚠️⚠️\nLast warning"
            }
            
            msg = warning_messages[self.warnings]
            img = f"warning_{self.warnings}.jpg"
        
        elif self.warnings == 4:
            msg = (
                "Yellow Card 🟨❕\n\n"
                "Please take some time to reflect on your language, you can make your point come across in a polite and respectful way.\n\n"
                "We are better than this, I believe in you."
            )
            img = f"yellow_card_{random.randint(1, 5)}.jpg"
        
        elif self.warnings == 5:
            msg = (
                "RED CARD 🟥‼️\n\n"
                "YOU ARE NOW EXPELLED FROM THE MATCH."
            )
            img = f"red_card_{random.randint(1, 4)}.jpg"
        
        elif self.warnings == 6:
            msg = (
                "What? WHAT? WHAAAT?\n\n"
                "I said be kind nicely.\n\n"
                "You are not being kind!!\n\n"
                "Out. OUT!!"
            )
            img = "what_what.jpg"
            
        else:
            msg = (
                "You want me to call the police?\n\n"
                "Is that what you want?\n"
                "Is that what YOU WANT?\n\n"
                "@X please look into it and consider suspending this entity account for 24h."
            )
            img = ""
        
        return msg, img



    def reset_warnings(self):
        self.warnings = 0