"""
    API Call Functions
"""

import requests
import tweepy  # An easy-to-use Python library for accessing the Twitter API.
import time
import re

################################################################################
#________________________________________________YouTube API key/ID
YOUTUBE_APIKEY = "YOUTUBE_APIKEY"
YOUTUBE_CHANNEL_ID = "YOUTUBE_CHANNEL_ID"

#________________________________________________Twitter API keys/username
TWITTER_API_KEY = "TWITTER_API_KEY"
TWITTER_API_SECRET_KEY = "TWITTER_API_SECRET_KEY"
TWITTER_ACCESS_TOKEN = "TWITTER_ACCESS_TOKEN"
TWITTER_TOKEN_SECRET = "TWITTER_TOKEN_SECRET"
TWITTER_USERNAME = "TWITTER_USERNAME"

#________________________________________________Instagram API key/username
INSTA_USERNAME = "INSTA_USERNAME"

################################################################################

YOUTUBE_BASE_URL = ("https://www.googleapis.com/youtube/v3/channels?part=statistics&" +
                    "id=" + YOUTUBE_CHANNEL_ID + "&key=" + YOUTUBE_APIKEY)

INSTA_BASE_URL = "https://www.instagram.com/" + INSTA_USERNAME


#=============================================================================Functions↴
def getYoutubeSubscribers():

    requestResult = requests.get(YOUTUBE_BASE_URL)
    youtubeJsonData = requestResult.json()

    youtubeSubscriberCount = int(
        youtubeJsonData['items'][0]['statistics']['subscriberCount'])

    return youtubeSubscriberCount


def getTwitterFollowerCount():

    auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_TOKEN_SECRET)

    api = tweepy.API(auth)
    user = api.get_user(TWITTER_USERNAME)  # Get the User object.

    twitterFollowerCount = user.followers_count

    return twitterFollowerCount


def getInstaFollowerCount():

    intaResult = requests.get(INSTA_BASE_URL)
    # Regex search for 3 defferent possibles types of subscriber count values (i.e. 100, 1,234, 54.1m).
    m = re.search("([0-9],[0-9]+ F)|([0-9]+[.][0-9]+[a-z] [F]|([0-9]+ [F]))",
                  str(intaResult.content))

    instaFollowerCount = str(m.group()[0:-2]).upper()

    return instaFollowerCount
