# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SettingDialog.ui'
#
# Created: Thu Jul 13 15:23:43 2017
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SettingDialog(object):
    def setupUi(self, SettingDialog):
        SettingDialog.setObjectName(_fromUtf8("SettingDialog"))
        SettingDialog.resize(496, 300)
        self.gridLayout = QtGui.QGridLayout(SettingDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(SettingDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(SettingDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(SettingDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3, 1, 1, 1)
        self.unitBox = QtGui.QComboBox(SettingDialog)
        self.unitBox.setObjectName(_fromUtf8("unitBox"))
        self.unitBox.addItem(_fromUtf8(""))
        self.unitBox.addItem(_fromUtf8(""))
        self.unitBox.addItem(_fromUtf8(""))
        self.unitBox.addItem(_fromUtf8(""))
        self.unitBox.addItem(_fromUtf8(""))
        self.unitBox.addItem(_fromUtf8(""))
        self.unitBox.addItem(_fromUtf8(""))
        self.unitBox.addItem(_fromUtf8(""))
        self.unitBox.addItem(_fromUtf8(""))
        self.unitBox.addItem(_fromUtf8(""))
        self.unitBox.addItem(_fromUtf8(""))
        self.unitBox.addItem(_fromUtf8(""))
        self.unitBox.addItem(_fromUtf8(""))
        self.unitBox.addItem(_fromUtf8(""))
        self.unitBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.unitBox, 2, 1, 1, 1)
        self.valueBox = QtGui.QDoubleSpinBox(SettingDialog)
        self.valueBox.setDecimals(6)
        self.valueBox.setMaximum(1000000.0)
        self.valueBox.setObjectName(_fromUtf8("valueBox"))
        self.gridLayout.addWidget(self.valueBox, 0, 1, 1, 1)

        self.retranslateUi(SettingDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SettingDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SettingDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingDialog)

    def retranslateUi(self, SettingDialog):
        SettingDialog.setWindowTitle(QtGui.QApplication.translate("SettingDialog", "Component Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SettingDialog", "Component Value", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SettingDialog", "Unit", None, QtGui.QApplication.UnicodeUTF8))
        self.unitBox.setItemText(0, QtGui.QApplication.translate("SettingDialog", "Ω", None, QtGui.QApplication.UnicodeUTF8))
        self.unitBox.setItemText(1, QtGui.QApplication.translate("SettingDialog", "kΩ", None, QtGui.QApplication.UnicodeUTF8))
        self.unitBox.setItemText(2, QtGui.QApplication.translate("SettingDialog", "MΩ", None, QtGui.QApplication.UnicodeUTF8))
        self.unitBox.setItemText(3, QtGui.QApplication.translate("SettingDialog", "pF", None, QtGui.QApplication.UnicodeUTF8))
        self.unitBox.setItemText(4, QtGui.QApplication.translate("SettingDialog", "nF", None, QtGui.QApplication.UnicodeUTF8))
        self.unitBox.setItemText(5, QtGui.QApplication.translate("SettingDialog", "µF", None, QtGui.QApplication.UnicodeUTF8))
        self.unitBox.setItemText(6, QtGui.QApplication.translate("SettingDialog", "µH", None, QtGui.QApplication.UnicodeUTF8))
        self.unitBox.setItemText(7, QtGui.QApplication.translate("SettingDialog", "mH", None, QtGui.QApplication.UnicodeUTF8))
        self.unitBox.setItemText(8, QtGui.QApplication.translate("SettingDialog", "H", None, QtGui.QApplication.UnicodeUTF8))
        self.unitBox.setItemText(9, QtGui.QApplication.translate("SettingDialog", "nV", None, QtGui.QApplication.UnicodeUTF8))
        self.unitBox.setItemText(10, QtGui.QApplication.translate("SettingDialog", "µV", None, QtGui.QApplication.UnicodeUTF8))
        self.unitBox.setItemText(11, QtGui.QApplication.translate("SettingDialog", "mV", None, QtGui.QApplication.UnicodeUTF8))
        self.unitBox.setItemText(12, QtGui.QApplication.translate("SettingDialog", "V", None, QtGui.QApplication.UnicodeUTF8))
        self.unitBox.setItemText(13, QtGui.QApplication.translate("SettingDialog", "kV", None, QtGui.QApplication.UnicodeUTF8))
        self.unitBox.setItemText(14, QtGui.QApplication.translate("SettingDialog", "MV", None, QtGui.QApplication.UnicodeUTF8))

