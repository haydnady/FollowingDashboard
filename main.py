"""
    Main  
"""

from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2 import QtUiTools, QtGui, QtWidgets
from generalFunctions import formatN
from form import Ui_MainWindow
from APICalls import *
import sys
import os

class myApp(Ui_MainWindow):

     def __init__(self, window):
        self.setupUi(window)

        self.labelYoutube.setPixmap(os.path.abspath("resources\\youtubeLogo.png"))
        self.labelInsta.setPixmap(os.path.abspath("resources\\instaLogo.png"))
        self.labelTwitter.setPixmap(os.path.abspath("resources\\twitterLogo.png"))







if __name__ == "__main__":
    # Create the Qt Application
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    # Create an instance and show the form
    ui = myApp(MainWindow)

    # show the window and start the app
    MainWindow.show()
    app.exec_()


# For testing purposes.
# print("---------------------------------")
# print("Subcribers: {0:>20}".format(formatN(getYoutubeSubscribers())))
# print("Twitter followers: {0:>13}".format(getTwitterFollowerCount()))
# print("Insta followers: {0:>15}".format(getInstaFollowerCount()))
# print("---------------------------------")