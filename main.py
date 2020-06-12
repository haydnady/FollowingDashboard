"""
    Dashboard Display of Data  
"""
from generalFunctions import formatN
from APICalls import youtubeData, instaData
import sys
import os
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2 import QtUiTools

# youtube = youtubeData()
# print("Subcribers", formatN(youtube["subscribers"]))

insta = instaData()
print("Insta followers", insta["followers"])




# The application class where all the functionality gets added to the Ui
class AppWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = QtUiTools.QUiLoader().load("mainwindow.ui")
        self.show()

        # __________________________________________________________________ Added Ui functionalities 
        # MainWindow.setWindowIcon( QtGui.QIcon( os.path.abspath("resources\\instaLogo.png") ) )


def main():
    app = QApplication(sys.argv)
    window = QtUiTools.QUiLoader().load("mainwindow.ui")
    window .show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()