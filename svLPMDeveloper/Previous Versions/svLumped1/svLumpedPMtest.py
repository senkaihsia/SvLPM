#!/usr/bin/env python
#Lumped Parameter Circuit Model Creator GUI for Stanford CBCL and Simvascular


from PyQt4 import QtGui, QtCore
import sys 

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import Qt

import svLumpedGui
from drag2test import *



class MainWindow(QMainWindow, svLumpedGui.Ui_MainWindow):
    def __init__(self, parent=None):
       super(MainWindow, self).__init__(parent)
       self.setupUi(self)


class CustomButton(DragButton):
    def __init__(self):
        super(CustomButton, self).__init__()

        


    

app = QtGui.QApplication(sys.argv)
form = MainWindow()
form.show()
app.exec_()
