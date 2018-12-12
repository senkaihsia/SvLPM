from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QPushButton
from PyQt4.QtGui import QPainter
from PyQt4.QtGui import QColor
from PyQt4.QtCore import Qt

import sys

import svLumpedGui2
from dragbutton import DragButton
import SettingDialog
from wirewidget import wireWidget


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class MainWindow(QMainWindow, svLumpedGui2.Ui_MainWindow):
    
    
    def __init__(self, parent=None,):
       super(MainWindow, self).__init__(parent)
       self.setupUi(self)
       self.Resistor.clicked.connect(self.addResistorButton)
       self.Capacitor.clicked.connect(self.addCapacitorButton)

       self.Inductor.clicked.connect(self.addInductorButton)
       self.Diode.clicked.connect(self.addDiodeButton)
       self.DCVoltageSource.clicked.connect(self.addVoltageButton)

    def mousePressEvent(self, event):
       self.__mousePressPos = None
       if event.button() == QtCore.Qt.RightButton:
          self.x1 = event.globalPos().x()
          self.y1 = event.globalPos().y()
          self.__mousePressPos = None
          if event.button() == QtCore.Qt.RightButton:
           QtGui.QPushButton.mousePressEvent = self.getPos2
   
           
    def getPos2(self, event):
        self.x2 = event.globalPos().x()
        self.y2 = event.globalPos().y()
        print self.x1, self.y1, self.x2, self.y2

##    def paintEvent(self, e):
##
##        qp = QtGui.QPainter()
##        qp.begin(self)
##        self.drawLines(qp)
##        qp.end()
##        
##    def drawLines(self, qp):
##      
##        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
##
##        qp.setPen(pen)
##        qp.drawLine(self.x1, self.y1, self.x2, self.y2)

    
        



        
    def addResistorButton(self):
        self.Resistor2 = DragButton('', self)
        self.Resistor2.setGeometry(QtCore.QRect(40, 30, 131, 61))
        self.Resistor2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Resistor2.setAcceptDrops(False)
        self.Resistor2.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Resistor.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Resistor2.setIcon(icon)
        self.Resistor2.setIconSize(QtCore.QSize(130, 67))
        self.Resistor2.setFlat(True)
        self.Resistor2.setObjectName(_fromUtf8("Resistor"))
        self.Resistor2.setCheckable(True)
        self.Resistor2.setChecked(False)
        self.Resistor2.show()
        self.Resistor2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.Resistor2.customContextMenuRequested.connect(self.handlebutton)
        
    def addCapacitorButton(self):
        self.Capacitor2 = DragButton('', self)
        self.Capacitor2.setGeometry(QtCore.QRect(80, 120, 51, 51))
        self.Capacitor2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Capacitor2.setAcceptDrops(False)
        self.Capacitor2.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("capacitor.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Capacitor2.setIcon(icon1)
        self.Capacitor2.setIconSize(QtCore.QSize(150, 60))
        self.Capacitor2.setFlat(True)
        self.Capacitor2.setObjectName(_fromUtf8("Capacitor"))
        self.Capacitor2.setCheckable(True)
        self.Capacitor2.setChecked(False)
        self.Capacitor2.show()
        self.Capacitor2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.Capacitor2.customContextMenuRequested.connect(self.handlebutton)
                        

    def addInductorButton(self):
        self.Inductor2 = DragButton('', self)
        self.Inductor2.setGeometry(QtCore.QRect(40, 280, 141, 51))
        self.Inductor2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Inductor2.setAcceptDrops(False)
        self.Inductor2.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("Inductor.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Inductor2.setIcon(icon3)
        self.Inductor2.setIconSize(QtCore.QSize(135, 80))
        self.Inductor2.setFlat(True)
        self.Inductor2.setObjectName(_fromUtf8("Inductor"))
        self.Inductor2.show()
        self.Inductor2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.Inductor2.customContextMenuRequested.connect(self.handlebutton)

    def addDiodeButton(self):
        self.Diode2 = DragButton('', self)
        self.Diode2.setGeometry(QtCore.QRect(50, 190, 111, 71))
        self.Diode2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Diode2.setAcceptDrops(False)
        self.Diode2.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap
        (QtGui.QPixmap(_fromUtf8("Diode.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Diode2.setIcon(icon2)
        self.Diode2.setIconSize(QtCore.QSize(200, 67))
        self.Diode2.setFlat(True)
        self.Diode2.setObjectName(_fromUtf8("Diode"))
        self.Diode2.show()
        self.Diode2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.Diode2.customContextMenuRequested.connect(self.handlebutton)

    def addVoltageButton(self):
        self.DCVoltageSource2 = DragButton('', self)
        self.DCVoltageSource2.setGeometry(QtCore.QRect(70, 350, 71, 71))
        self.DCVoltageSource2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.DCVoltageSource2.setAcceptDrops(False)
        self.DCVoltageSource2.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("DCVoltageSource.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DCVoltageSource2.setIcon(icon4)
        self.DCVoltageSource2.setIconSize(QtCore.QSize(100, 60))
        self.DCVoltageSource2.setFlat(True)
        self.DCVoltageSource2.setObjectName(_fromUtf8("DCVoltageSource"))
        self.DCVoltageSource2.show()
        self.DCVoltageSource2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.DCVoltageSource2.customContextMenuRequested.connect(self.handlebutton)
        

    def handlebutton(self):
        if QtGui.qApp.keyboardModifiers() & QtCore.Qt.ShiftModifier:
            form = SettingDialog(self)
            form.show()

        

class SettingDialog(QDialog, SettingDialog.Ui_SettingDialog):
    def __init__(self, parent=None):
       super(SettingDialog, self).__init__(parent)
       self.setupUi(self)


        



        
app = QtGui.QApplication(sys.argv)
form = MainWindow()
form.show()
app.exec_()
