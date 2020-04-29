"""
    General functions to accomplish things 
    like number formating, etc.
"""

# This function is to format numbers to abreviated style (i.e. 3005 = 3K)
# See this page for resons why/guide --> https://support.google.com/youtube/thread/6543166?hl=en
def formatN(number):

    if (number > 1000 and number < 10001):
        formattedN = ("%0.2f" % (number / 1000) + "K")  # i.e. 1234 = 1.23K
    elif (number > 10000 and number < 100001):
        formattedN = ("%0.1f" % (number / 1000) + "K")  # i.e. 12345 = 12.3K
    elif (number > 100000 and number < 1000001):
        formattedN = ("%0.0f" % (number / 1000) + "K")  # i.e. 123456 = 123K
    elif (number > 1000000 and number < 10000001):
        formattedN = ("%0.2f" % (number / 1000000) + "M")  # i.e. 1234567 = 1.23M
    elif (number > 10000000 and number < 100000001):
        formattedN = ("%0.1f" % (number / 1000000) + "M")  # i.e. 12345678 = 12.3M
    elif (number > 100000000 and number < 1000000001):
        formattedN = ("%0.0f" % (number / 1000000) + "M")  # i.e. 123456789 = 12.3M
    else:
        formattedN = number

    return formattedN
