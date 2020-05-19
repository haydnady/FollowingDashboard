"""
    API Call Functions
"""

import time
import requests
import re

#//////////////////////////////////////////////////////////////////

YOUTUBE_APIKEY = "YOUTUBE_APIKEY"
YOUTUBE_CHANNEL_ID = "YOUTUBE_CHANNEL_ID"

INSTA_USERNAME = "INSTA_USERNAME"

#//////////////////////////////////////////////////////////////////

#=========================================================================== Get Youtube Data
def youtubeData():

    baseurl = ("https://www.googleapis.com/youtube/v3/channels?part=statistics&" +
               "id=" + YOUTUBE_CHANNEL_ID + "&key=" + YOUTUBE_APIKEY)

    ytResults = requests.get(baseurl)
    ytData = ytResults.json()
    # print(ytData)

    # YoutubeData Dict
    youtubeEssentials = {"ID": ytData['items'][0]['id'],
                         "views": int(ytData['items'][0]['statistics']['viewCount']),
                         "subscribers": int(ytData['items'][0]['statistics']['subscriberCount']),
                         "videos": int(ytData['items'][0]['statistics']['videoCount'])}

    return youtubeEssentials


def instaData():

    baseurl = "https://www.instagram.com/" + INSTA_USERNAME

    intaResult = requests.get(baseurl)
    # Regex search for 3 defferent possibles types of subscriber count values (i.e. 100, 1,234, 54.1m).
    m = re.search("([0-9],[0-9]+ F)|([0-9]+[.][0-9]+[a-z] [F]|([0-9]+ [F]))",
                  str(intaResult.content))
    # print(m.group()[0:-2])

    instaEssentials = {"followers": str(m.group()[0:-2])} # Insta data dict.

    return instaEssentials