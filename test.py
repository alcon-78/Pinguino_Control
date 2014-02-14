import sys
import usb
import time
from PyQt4 import QtCore,QtGui
from test_ui import Ui_MainWindow

VENDOR = 0x04D8
PRODUCT = 0xFEAA

TIMEOUT = 100
INTERFACE = 0
ENDPOINT_OUT = 0x01

# if bootloader v4.x
CONFIGURATION = 0x01
ENDPOINT_IN = 0x81

# if bootloader v2.x
#CONFIGURATION = 0x03
#ENDPOINT_IN = 0x82

def read():
    return "".join(map(chr, dh.bulkRead (ENDPOINT_IN, 21, TIMEOUT)))

def write_command(command):
    dh.bulkWrite(ENDPOINT_OUT, command, TIMEOUT)

busses = usb.busses()

# Search pinguino between all the usb devices
for bus in busses:
    devices = bus.devices
    for dev in devices:
        if dev.idVendor==VENDOR and dev.idProduct==PRODUCT:
            pinguino = dev

assert pinguino

# Get a device handler for the usb device
dh = pinguino.open()
dh.setConfiguration(CONFIGURATION)
dh.claimInterface(INTERFACE)


class TestApp(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"),on)
        self.connect(self.ui.pushButton_2, QtCore.SIGNAL("clicked()"),off)
        
def on():
    write_command("digitalWrite(6,HIGH)")    

def off():
    write_command("digitalWrite(6,LOW)")


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = TestApp()
    window.show()
    sys.exit(app.exec_())
