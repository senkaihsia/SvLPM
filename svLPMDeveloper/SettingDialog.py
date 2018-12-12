# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SettingDialog.ui'
#
# Created: Thu Aug 10 14:27:01 2017
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
        SettingDialog.resize(585, 386)
        self.verticalLayout = QtGui.QVBoxLayout(SettingDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_4 = QtGui.QLabel(SettingDialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.Type = QtGui.QLabel(SettingDialog)
        self.Type.setText(_fromUtf8(""))
        self.Type.setObjectName(_fromUtf8("Type"))
        self.verticalLayout.addWidget(self.Type)
        self.label_3 = QtGui.QLabel(SettingDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.Name = QtGui.QLineEdit(SettingDialog)
        self.Name.setObjectName(_fromUtf8("Name"))
        self.verticalLayout.addWidget(self.Name)
        self.label = QtGui.QLabel(SettingDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.Value = QtGui.QDoubleSpinBox(SettingDialog)
        self.Value.setDecimals(8)
        self.Value.setMaximum(1000000.0)
        self.Value.setObjectName(_fromUtf8("Value"))
        self.verticalLayout.addWidget(self.Value)
        self.label_2 = QtGui.QLabel(SettingDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.Unit = QtGui.QComboBox(SettingDialog)
        self.Unit.setObjectName(_fromUtf8("Unit"))
        self.Unit.addItem(_fromUtf8(""))
        self.Unit.addItem(_fromUtf8(""))
        self.Unit.addItem(_fromUtf8(""))
        self.Unit.addItem(_fromUtf8(""))
        self.Unit.addItem(_fromUtf8(""))
        self.Unit.addItem(_fromUtf8(""))
        self.Unit.addItem(_fromUtf8(""))
        self.Unit.addItem(_fromUtf8(""))
        self.Unit.setItemText(7, _fromUtf8(""))
        self.verticalLayout.addWidget(self.Unit)
        self.Save = QtGui.QDialogButtonBox(SettingDialog)
        self.Save.setOrientation(QtCore.Qt.Horizontal)
        self.Save.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.Save.setObjectName(_fromUtf8("Save"))
        self.verticalLayout.addWidget(self.Save)

        self.retranslateUi(SettingDialog)
        QtCore.QObject.connect(self.Save, QtCore.SIGNAL(_fromUtf8("accepted()")), SettingDialog.accept)
        QtCore.QObject.connect(self.Save, QtCore.SIGNAL(_fromUtf8("rejected()")), SettingDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingDialog)

    def retranslateUi(self, SettingDialog):
        SettingDialog.setWindowTitle(QtGui.QApplication.translate("SettingDialog", "Component Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("SettingDialog", "Component Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("SettingDialog", "Component Name or Boundary Face Pressure File: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SettingDialog", "Component Value", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SettingDialog", "Value Metric Prefix", None, QtGui.QApplication.UnicodeUTF8))
        self.Unit.setItemText(0, QtGui.QApplication.translate("SettingDialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.Unit.setItemText(1, QtGui.QApplication.translate("SettingDialog", "k", None, QtGui.QApplication.UnicodeUTF8))
        self.Unit.setItemText(2, QtGui.QApplication.translate("SettingDialog", "M", None, QtGui.QApplication.UnicodeUTF8))
        self.Unit.setItemText(3, QtGui.QApplication.translate("SettingDialog", "m", None, QtGui.QApplication.UnicodeUTF8))
        self.Unit.setItemText(4, QtGui.QApplication.translate("SettingDialog", "micro", None, QtGui.QApplication.UnicodeUTF8))
        self.Unit.setItemText(5, QtGui.QApplication.translate("SettingDialog", "n", None, QtGui.QApplication.UnicodeUTF8))
        self.Unit.setItemText(6, QtGui.QApplication.translate("SettingDialog", "p", None, QtGui.QApplication.UnicodeUTF8))

