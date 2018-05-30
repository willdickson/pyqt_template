from __future__ import print_function
import sys
from PyQt5 import QtCore
from PyQt5 import QtGui 
from PyQt5 import QtWidgets
from main_window_ui import Ui_MainWindow


class AppMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(AppMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.initialize()
        self.connectActions()

    def initialize(self):
        self.actionSave.setShortcut('Ctrl+S')
        self.actionLoad.setShortcut('Ctrl+L')
        self.timer = QtCore.QTimer()
        self.timerCounter = 0
        self.timerPeriod = 10
        self.setCountLabel(self.timerCounter)

    def connectActions(self):
        self.mainTabWidget.currentChanged.connect(self.onMainTabChanged)
        self.startPushButton.clicked.connect(self.onStartButtonClicked)
        self.stopPushButton.clicked.connect(self.onStopButtonClicked)
        self.actionSave.triggered.connect(self.onFileSave)
        self.actionLoad.triggered.connect(self.onFileLoad)
        self.timer.timeout.connect(self.onTimer)

    def onMainTabChanged(self,index):
        print('tab changed to {}'.format(index))

    def onStartButtonClicked(self):
        print('start button clicked')
        self.timerCounter = 0
        self.timer.start(self.timerPeriod)

    def onStopButtonClicked(self):
        print('stop button clicked')
        self.timer.stop()

    def onFileSave(self):
        print('save file')

    def onFileLoad(self):
        print('load file')

    def onTimer(self):
        self.timerCounter += 1
        print('count = {}'.format(self.timerCounter))
        self.setCountLabel(self.timerCounter)

    def setCountLabel(self,value):
        self.countLabel.setText('{}'.format(self.timerCounter))


def appMain():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = AppMainWindow()
    mainWindow.show()
    app.exec_()


# -------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    appMain()


