"""
    API Call Functions  
"""

import time
import requests
from geopy.geocoders import Nominatim

#//////////////////////////////////////////////////////////////////

YOUTUBE_APIKEY = "YOUTUBE_APIKEY"
YOUTUBE_CHANNEL_ID = "YOUTUBE_CHANNEL_ID"

#//////////////////////////////////////////////////////////////////

#=========================================================================== Get Youtube Data
def youtubeData(YOUTUBE_APIKEY, YOUTUBE_CHANNEL_ID):

    baseurl = ("https://www.googleapis.com/youtube/v3/channels?part=statistics&" +
               "id=" + YOUTUBE_CHANNEL_ID + "&key=" + YOUTUBE_APIKEY)

    yt_results = requests.get(baseurl)
    yt_data = yt_results.json()
    # print(yt_data)

    # YoutubeData Dict
    youtubeEssentials = {}
    youtubeEssentials = {"ID": yt_data['items'][0]['id'],
                         "views": yt_data['items'][0]['statistics']['viewCount'],
                         "subscribers": yt_data['items'][0]['statistics']['subscriberCount'],
                         "videos": yt_data['items'][0]['statistics']['videoCount']}

    return youtubeEssentials

