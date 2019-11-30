#### Program to plot spherical harmonics in a GUI #####

import sys
from PyQt5.QtWidgets import (
        QApplication, QWidget, QLabel, QPushButton, QSlider, QFrame, QAction, QMessageBox
    )
from PyQt5.QtCore import pyqtSlot, QRect, Qt
from sphericalharm import spherharm
from realspherharm import real
from onePlusReal import oneplusreal


class MainPage(QWidget):
    def __init__(self):
        """ Constructor """
        super().__init__() # inherit init of QWidget self.title = title
        self.left = 250
        self.top = 250
        self.width = 400
        self.height = 300
        self.widget()
    def widget(self): # window setup
        """ main window setup """
        self.setWindowTitle("Spherical Harmonics Example GUI")
        # self.setGeometry(self.left, self.top, self.width, self.height) ## use above line or below
        self.resize(self.width, self.height)
        self.move(self.left, self.top)
        # create frame for a set of checkbox
        self.frame1 = QFrame(self)
        self.frame1.setGeometry(QRect(40, 40, 250, 180))
        # create spin box
        self.slider1 = QSlider(self.frame1)
        self.slider1.setOrientation(Qt.Horizontal) # Horizontal / Vertical self.slider1.setTickInterval(1)
        self.slider1.setTickPosition(QSlider.TicksBelow)
        self.slider1.setTickInterval(1)
        self.slider1.setValue(1) # default value
        self.slider1.setMinimum(1) # minimum value
        self.slider1.setMaximum(10) # maximum value
        self.slider1.move(0, 50)
        self.slider1.valueChanged.connect(self.slider1_changed)
        #slider m
        self.slider2 = QSlider(self.frame1)
        self.slider2.setOrientation(Qt.Horizontal) # Horizontal / Vertical self.slider1.setTickInterval(1)
        self.slider2.setTickPosition(QSlider.TicksBelow)
        self.slider2.setTickInterval(1)
        self.slider2.setValue(1) # default value
        self.slider2.setMinimum(1) # minimum value
        self.slider2.setMaximum(10) # maximum value
        self.slider2.move(0, 120)
        self.slider2.valueChanged.connect(self.slider2_changed)
        # slider value will be displayed on label
        self.label1 = QLabel(self.frame1, text="Value of l = " + str(self.slider1.value()))
        self.label1.setGeometry(QRect(0, 20, 500, 20))
        self.label2 = QLabel(self.frame1, text="Value of m = " + str(self.slider2.value()))
        self.label2.setGeometry(QRect(0, 90, 500, 20))

        button = QPushButton('Plot Spherical Harmonics',self)
        button.clicked.connect(self.opengraph)
        button.resize(button.sizeHint())
        button.move(0,200)

        button2 = QPushButton('Plot the real part', self)
        button2.clicked.connect(self.opengraph2)
        button2.resize(button.sizeHint())
        button2.move(0,230)

        button3 = QPushButton('Plot 1 + the real part', self)
        button3.clicked.connect(self.opengraph3)
        button3.resize(button.sizeHint())
        button3.move(0,260)

        extractAction = QAction('&Quit', self)
        extractAction.setShortcut('Ctrl+Q')
        extractAction.setStatusTip('leave the app')
        extractAction.triggered.connect(self.close_application)
        btn = QPushButton('quit', self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.sizeHint())
        btn.move(0, 0)        
        self.show()
                
    @pyqtSlot()
    def slider1_changed(self):
        """ l slider changer """
        self.label1.setText("Value of l = "+str(self.slider1.value()))
    @pyqtSlot()
    def slider2_changed(self):
        """ m slider changer """
        self.label2.setText("Value of m = "+str(self.slider2.value()))
    def opengraph(self):
        """ plot spherical harmonics with error control"""
        if (self.slider2.value() < self.slider1.value()) | (self.slider2.value() == self.slider1.value()):
            self.store = spherharm(self.slider1.value(),self.slider2.value())
        elif self.slider2.value() > self.slider1.value():
            print("Please enter values of m that are not < l")
    def opengraph2(self):
        """ plot real part with error control"""
        if (self.slider2.value() < self.slider1.value()) | (self.slider2.value() == self.slider1.value()):
            self.store = real(self.slider1.value(),self.slider2.value())
        elif self.slider2.value() > self.slider1.value():
            print("Please enter values of m that are not < l")
    def opengraph3(self):
        """ plot real part with error control"""
        if (self.slider2.value() < self.slider1.value()) | (self.slider2.value() == self.slider1.value()):
            self.store = oneplusreal(self.slider1.value(),self.slider2.value())
        elif self.slider2.value() > self.slider1.value():
            print("Please enter values of m that are not < l")
    def close_application(self):
        """ Quit option for the user"""
        choice = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if choice == QMessageBox.Yes:
            sys.exit()
        else:
            pass


def main():
    app = QApplication(sys.argv)
    w = MainPage()
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__': main()
