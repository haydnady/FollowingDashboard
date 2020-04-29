"""
    Dashboard Display of Data  
"""
from generalFunctions import formatN
from APICalls import youtubeData

youtube = youtubeData()
print("Subcribers", formatN(youtube["subscribers"]))