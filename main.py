"""
    Main  
"""

from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2 import QtUiTools, QtGui
from generalFunctions import formatN
from form import Ui_MainWindow
from APICalls import *
import sys
import os

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)





if __name__ == "__main__":
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    window = MainWindow()
    window.show()
    # Run the main Qt loop
    sys.exit(app.exec_())


# For testing purposes.
# print("---------------------------------")
# print("Subcribers: {0:>20}".format(formatN(getYoutubeSubscribers())))
# print("Twitter followers: {0:>13}".format(getTwitterFollowerCount()))
# print("Insta followers: {0:>15}".format(getInstaFollowerCount()))
# print("---------------------------------")