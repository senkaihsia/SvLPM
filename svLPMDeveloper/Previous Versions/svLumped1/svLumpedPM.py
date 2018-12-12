#!/usr/bin/env python
#Lumped Parameter Circuit Model Creator GUI for Stanford CBCL and Simvascular

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import Qt
import sys

import svLumpedGui
import SettingDialog

class SettingDialog(QDialog, SettingDialog.Ui_SettingDialog):
    def __init__(self, parent=None):
        super(SettingDialog, self).__init__(parent)
        self.setupUi(self) 
        
# Main Gui for svLumpedPM initialisation and button function
class MainWindow(QMainWindow, svLumpedGui.Ui_MainWindow):
    def __init__(self, parent=None):
       super(MainWindow, self).__init__(parent)
       self.setupUi(self)
       self.Resistor.clicked.connect(self.handlebutton)
       self.Capacitor.clicked.connect(self.handlebutton)
       self.Inductor.clicked.connect(self.handlebutton)
       self.Diode.clicked.connect(self.handlebutton)
       self.DCVoltageSource.clicked.connect(self.handlebutton)

    def handlebutton(self):
        form = SettingDialog(self)
        form.show() 
           
        
app = QtGui.QApplication(sys.argv)
form = MainWindow()
form.show()
app.exec_()
