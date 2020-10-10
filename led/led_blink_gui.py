import sys
import time
from gpiozero import LED
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        # GPIO 17 --> pin 11
        self.my_led_1 = LED(17)
        # GPIO 5 --> pin 29
        self.my_led_2 = LED(5)

        self.setMinimumSize(QSize(500, 500))    
        self.setWindowTitle('LED Blink PyQt5 GUI')
        
        on_btn = QPushButton('ON', self)
        on_btn.clicked.connect(self.led_on)
        on_btn.resize(100, 50)
        on_btn.move(50, 50)
        
        off_btn = QPushButton('OFF', self)
        off_btn.clicked.connect(self.led_off)
        off_btn.resize(100, 50)
        off_btn.move(150, 50)
        
        self.toggle_btn = QPushButton('Toggle', self)
        self.toggle_btn.setCheckable(True) 
        self.toggle_btn.clicked.connect(self.toggle_led)
        self.toggle_btn.resize(100, 50)
        self.toggle_btn.move(300, 50)
        self.toggle_btn.setStyleSheet("background-color : lightgrey")

    
    def led_on(self):
        print('LED 1: ON')
        self.my_led_1.on()
    
    def led_off(self):
        print('LED 1: OFF')
        self.my_led_1.off()
        
    
    def toggle_led(self):
        if self.toggle_btn.isChecked():
            print('LED 2: ON')
            self.my_led_2.on()
            
            self.toggle_btn.setStyleSheet("background-color : lightblue") 
  
        # if it is unchecked 
        else:
            print('LED 2: OFF')
            self.my_led_2.off()
            
            self.toggle_btn.setStyleSheet("background-color : lightgrey") 
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
