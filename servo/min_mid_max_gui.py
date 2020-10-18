import sys
import time
from gpiozero import Servo
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        # GPIO 17 --> pin 11
        self.servo = Servo(17)

        self.setMinimumSize(QSize(500, 500))    
        self.setWindowTitle('LED Blink PyQt5 GUI')
        
        min_btn = QPushButton('MIN', self)
        min_btn.clicked.connect(self.min)
        min_btn.resize(100, 50)
        min_btn.move(50, 50)
        
        mid_btn = QPushButton('MID', self)
        mid_btn.clicked.connect(self.mid)
        mid_btn.resize(100, 50)
        mid_btn.move(200, 50)
        
        max_btn = QPushButton('MAX', self)
        max_btn.clicked.connect(self.max)
        max_btn.resize(100, 50)
        max_btn.move(350, 50)
    
    def min(self):
        print('MIN')
        self.servo.min()
    
    def mid(self):
        print('MID')
        self.servo.mid()
    
    def max(self):
        print('MAX')
        self.servo.max()
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )

