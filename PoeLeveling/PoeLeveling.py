from PyQt5 import QtCore, QtWidgets, uic
import sys
from ActsList import *

class PLconfig:
    progressCounter = 1




#MAIN WINDOW
class MainWindow(QtWidgets.QWidget, PLconfig):
    def __init__(self, parent=None):
        #Window Loading
        super(MainWindow, self).__init__()
        uic.loadUi("UiTemplates/MainWindow.ui", self)

        #Window Styles
        self.setStyleSheet("background-color: gray")
        self.textTitle.setStyleSheet("background-color: white; border-radius: 5px;")
        self.btnStart.setStyleSheet("background-color: green; border-radius: 5px;")
        self.btnOptions.setStyleSheet("background-color: white; border-radius: 5px;")
        self.btnResume.setStyleSheet("background-color: white; border-radius: 5px;")

        #Buttons Connects
        self.btnStart.clicked.connect(self.showWindow)
        self.btnStart.clicked.connect(self.close)

    #MYWINDOW DEFENITION
    def showWindow(self):
        """ Show navigate window """
        self.window = Navigate()
        self.window.show()



#NAVIGATE WINDOW
class Navigate(QtWidgets.QWidget, PLconfig):
    def __init__(self, parent=None):
        #Window Loading
        super(Navigate, self).__init__()
        uic.loadUi("UiTemplates/Navigate.ui", self)
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)

        #Variable
        self.counter = PLconfig.progressCounter

        #Window Styles
        self.setStyleSheet("background-color: gray")
        self.btnDone.setStyleSheet("background-color: white; border-radius: 5px;")
        self.btnBack.setStyleSheet("background-color: white; border-radius: 5px;")
        self.btnRecoil.setStyleSheet("background-color: white; border-radius: 5px;")
        self.progressBar.setStyleSheet("background-color: white; border-radius: 1.5px;")
        self.secondNaviText.setStyleSheet("color: green;")
        self.secondNaviText.setText(ActOne[self.counter])
        self.firstNaviText.setText(ActOne[self.counter-1])
        self.thirdNaviText.setText(ActOne[self.counter+1])
        
        #Button Connects
        self.btnDone.clicked.connect(self.NavigateDone)
        self.btnRecoil.clicked.connect(self.NavigateBack)
        self.btnBack.clicked.connect(self.showWindow)
        self.btnBack.clicked.connect(self.close)

    #WINDOW DEFENITION
    def NavigateDone(self):
        if self.counter < len(ActOne) - 2:#ADD ALGORYTHM  ##########################################################
            self.counter += 1
            self.firstNaviText.setText(ActOne[self.counter])
            self.secondNaviText.setText(ActOne[self.counter+1])
            self.secondNaviText.setStyleSheet("color: green;")
            self.thirdNaviText.setText(ActOne[self.counter+2])
        else:
            pass

    def NavigateBack(self):
        if self.counter > 0:
            self.counter -= 1
            self.firstNaviText.setText(ActOne[self.counter])
            self.secondNaviText.setText(ActOne[self.counter+1])
            self.thirdNaviText.setText(ActOne[self.counter+2])
        else:
            pass

    def showWindow(self):
        PLconfig.saveCounter = self.counter
        self.window = MainWindow()
        self.window.show()
    
#FOOTER
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

