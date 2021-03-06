import sys
import time

from pynguino.pusb import PynguinoUSB
from PyQt4 import QtCore,QtGui
from test_ui import Ui_MainWindow


pinguino = PynguinoUSB(vboot="v4")
pinguino.pinMode(6, 0)


class TestApp(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"),on)
        self.connect(self.ui.pushButton_2, QtCore.SIGNAL("clicked()"),off)
        
def on():
    pinguino.digitalWrite(6, 1)    

def off():
    pinguino.digitalWrite(6, 0)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = TestApp()
    window.show()
    sys.exit(app.exec_())
