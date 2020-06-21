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

        # Setting platform icons
        self.labelYoutube.setPixmap(os.path.abspath("resources\\youtubeLogo.png"))
        self.labelInsta.setPixmap(os.path.abspath("resources\\instaLogo.png"))
        self.labelTwitter.setPixmap(os.path.abspath("resources\\twitterLogo.png"))

        # Setting LCD data
        self.lcdYoutube.display(getYoutubeSubscribers())
        self.lcdInsta.display(getInstaFollowerCount())
        self.lcdTwitter.display(getTwitterFollowerCount())


if __name__ == "__main__":
    # Create the Qt Application
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    # Create an instance and show the form
    ui = myApp(MainWindow)

    # show the window and start the app
    MainWindow.show()
    app.exec_()