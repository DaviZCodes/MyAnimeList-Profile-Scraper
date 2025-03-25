import requests
import os
from dotenv import load_dotenv

# getting the client_id from the env 
load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID") 

# initializing global variables 
USER = "Xinil"

# get user mangalist  
def getMangaList(user, limit, sort="anime_title", offset=0, status=None, nsfw=True): 
    '''
    status can be reading, completed, on_hold, dropped, and plan_to_read
    important status parameters for me are plan_to_read and list_updated_at

    sort can be list_score, list_updated_at, manga_title, and manga_start_date
    '''

    url = f"https://api.myanimelist.net/v2/users/{user}/mangalist?sort={sort}&limit={limit}&offset={offset}&fields=list_status&nsfw={str(nsfw).lower()}"

    if status: 
        url = url + f"&status={status}"

    response = requests.get(url, headers = {
        "X-MAL-CLIENT-ID": CLIENT_ID 
    })

    response.raise_for_status()
    mangalist = response.json()
    response.close()
    data = mangalist["data"]

    return data

def getUserTop20MangaList(user): 
    # dictionary to store {manga_title: {completed, score, num_episodes_watched, is_rewatching, updated_at}}
    top20_manga_dict = {}

    # top 20 user mangalist sorted by list_score 
    top20_mangalist = getMangaList(user, 20, "list_score")

    # top 20 manga 
    for i in range(len(top20_mangalist)): 
        manga_title = top20_mangalist[i]["node"]["title"]
        manga_list_status = top20_mangalist[i]["list_status"]
        manga_score = manga_list_status["score"]

        if manga_score != 0: 
            top20_manga_dict[manga_title] = manga_list_status

    return top20_manga_dict 

def getUserBottom20MangaList(user): 
    bottom10_manga_dict = {} # given that the max limit is 1000, the bottom 10 might be inaccurate if the user's list exceeds 1000 manga 
    # 1000 user mangalist 
    user_mangalist_sorted_by_list_score = getMangaList(USER, 1000, sort="list_score")

    # bottom 10 manga 
    temp_index = len(user_mangalist_sorted_by_list_score) - 1
    bottom10_scored_manga = 0
    while temp_index != 0 and bottom10_scored_manga < 10:
        manga_title = user_mangalist_sorted_by_list_score[temp_index]["node"]["title"]
        manga_list_status = user_mangalist_sorted_by_list_score[temp_index]["list_status"]
        manga_score = manga_list_status["score"]

        if manga_score != 0: # score 0 means an unscored manga 
            bottom10_manga_dict[manga_title] = manga_list_status
            bottom10_scored_manga += 1

        temp_index -= 1 
    
    return bottom10_manga_dict