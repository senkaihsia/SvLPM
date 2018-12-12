# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'svLumpedGui2.ui'
#
# Created: Tue Jul 18 13:27:39 2017
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(860, 438)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Resistor = QtGui.QPushButton(self.centralwidget)
        self.Resistor.setGeometry(QtCore.QRect(20, 10, 61, 51))
        self.Resistor.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Resistor.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Resistor.setIcon(icon)
        self.Resistor.setIconSize(QtCore.QSize(45, 50))
        self.Resistor.setObjectName(_fromUtf8("Resistor"))
        self.Capacitor = QtGui.QPushButton(self.centralwidget)
        self.Capacitor.setGeometry(QtCore.QRect(20, 70, 61, 51))
        self.Capacitor.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("capacitor.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Capacitor.setIcon(icon1)
        self.Capacitor.setIconSize(QtCore.QSize(50, 50))
        self.Capacitor.setObjectName(_fromUtf8("Capacitor"))
        self.Inductor = QtGui.QPushButton(self.centralwidget)
        self.Inductor.setGeometry(QtCore.QRect(20, 130, 61, 51))
        self.Inductor.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Inductor.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Inductor.setIcon(icon2)
        self.Inductor.setIconSize(QtCore.QSize(45, 45))
        self.Inductor.setObjectName(_fromUtf8("Inductor"))
        self.DCVoltageSource = QtGui.QPushButton(self.centralwidget)
        self.DCVoltageSource.setGeometry(QtCore.QRect(20, 180, 61, 51))
        self.DCVoltageSource.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("DCVoltageSource.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DCVoltageSource.setIcon(icon3)
        self.DCVoltageSource.setIconSize(QtCore.QSize(50, 50))
        self.DCVoltageSource.setObjectName(_fromUtf8("DCVoltageSource"))
        self.Diode = QtGui.QPushButton(self.centralwidget)
        self.Diode.setGeometry(QtCore.QRect(20, 240, 61, 51))
        self.Diode.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("Diode.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Diode.setIcon(icon4)
        self.Diode.setIconSize(QtCore.QSize(45, 60))
        self.Diode.setObjectName(_fromUtf8("Diode"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 860, 22))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFIle = QtGui.QMenu(self.menubar)
        self.menuFIle.setObjectName(_fromUtf8("menuFIle"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFIle.addAction(self.actionNew)
        self.menuFIle.addAction(self.actionOpen)
        self.menuFIle.addSeparator()
        self.menuFIle.addAction(self.actionSave)
        self.menuFIle.addSeparator()
        self.menuFIle.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFIle.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "svLumpedPM2", None, QtGui.QApplication.UnicodeUTF8))
        self.Resistor.setToolTip(QtGui.QApplication.translate("MainWindow", "Resistor", None, QtGui.QApplication.UnicodeUTF8))
        self.Resistor.setStatusTip(QtGui.QApplication.translate("MainWindow", "Click to Create Resistor", None, QtGui.QApplication.UnicodeUTF8))
        self.Capacitor.setToolTip(QtGui.QApplication.translate("MainWindow", "Capacitor", None, QtGui.QApplication.UnicodeUTF8))
        self.Capacitor.setStatusTip(QtGui.QApplication.translate("MainWindow", "Click to Create Capacitor", None, QtGui.QApplication.UnicodeUTF8))
        self.Inductor.setToolTip(QtGui.QApplication.translate("MainWindow", "Inductor", None, QtGui.QApplication.UnicodeUTF8))
        self.Inductor.setStatusTip(QtGui.QApplication.translate("MainWindow", "Click to Create Inductor", None, QtGui.QApplication.UnicodeUTF8))
        self.DCVoltageSource.setToolTip(QtGui.QApplication.translate("MainWindow", "DC Voltage Source", None, QtGui.QApplication.UnicodeUTF8))
        self.DCVoltageSource.setStatusTip(QtGui.QApplication.translate("MainWindow", "Click to Create DC Voltage Source", None, QtGui.QApplication.UnicodeUTF8))
        self.Diode.setToolTip(QtGui.QApplication.translate("MainWindow", "Diode", None, QtGui.QApplication.UnicodeUTF8))
        self.Diode.setStatusTip(QtGui.QApplication.translate("MainWindow", "Click to Create Diode", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFIle.setTitle(QtGui.QApplication.translate("MainWindow", "File ", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))

