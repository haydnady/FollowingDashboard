"""
    Dashboard Display of Data  
"""
from generalFunctions import formatN
from APICalls import youtubeData, instaData

youtube = youtubeData()
print("Subcribers", formatN(youtube["subscribers"]))

insta = instaData()
print("Insta followers", insta["followers"])