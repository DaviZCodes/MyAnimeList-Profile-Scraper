# attempt to fetch user data using the API but it's not possible without OAuth2

import requests
import os
from dotenv import load_dotenv

load_dotenv()

# getting the client_id from the env 
CLIENT_ID = os.getenv("CLIENT_ID")

# initializing global variables 
USER = "Xinil"

def getUser(): 
    '''
    status can be reading, completed, on_hold, dropped, and plan_to_read
    important status parameters for me are plan_to_read and list_updated_at

    sort can be list_score, list_updated_at, manga_title, and manga_start_date
    '''

    # get user profile information 
    url = f"https://api.myanimelist.net/v2/users/@me"

    response = requests.get(url, headers = {
        "X-MAL-CLIENT-ID": CLIENT_ID 
    })

    response.raise_for_status()
    user_profile = response.json()
    response.close()

    return user_profile