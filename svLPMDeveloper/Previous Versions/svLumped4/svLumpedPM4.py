from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QPushButton
from PyQt4.QtGui import QGraphicsScene
from PyQt4.QtCore import Qt

from xml.dom import minidom
import os
import sys

import svLumpedGui3A
from dragbutton import DragButton
import SettingDialog



try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s



wireCount = 0
componentCount = 0




class MainWindow(QMainWindow, svLumpedGui3A.Ui_MainWindow):


    def __init__(self, SettingDialog, parent=None,):
       super(MainWindow, self).__init__(parent)
       self.setupUi(self)
       self.Resistor.clicked.connect(self.addResistorButton)
       self.Capacitor.clicked.connect(self.addCapacitorButton)
       self.Inductor.clicked.connect(self.addInductorButton)
       self.Diode.clicked.connect(self.addDiodeButton)
       self.DCVoltageSource.clicked.connect(self.addVoltageButton)
       self.DeleteWire.clicked.connect(self.deleteWire)
       self.CircuitView.setScene(QtGui.QGraphicsScene(self))
       self.BoundaryFace.clicked.connect(self.addBoundaryFaceButton)
       self.Ground.clicked.connect(self.addGroundButton)
       self.Export.clicked.connect(self.exportXML)
       self.scene = self.CircuitView.scene()
     
       

    def mousePressEvent(self, event):
        global wireCount
        
        
        if event.buttons() == QtCore.Qt.MidButton:
            self.start = event.pos()
            self.start = self.mapToGlobal(event.pos())
            self.start = self.CircuitView.mapFromGlobal(self.start)
            self.start = self.CircuitView.mapToScene(self.start)
            self.clickX = self.start.x()
            self.clickY = self.start.y() 
            self.selectedItem = self.scene.itemAt(self.start)
            self.itemX = self.selectedItem.geometry().x()
            self.itemY = self.selectedItem.geometry().y()
            self.spock = self.selectedItem.widget()
            


            
        if (self.clickY > (self.itemY + 88)) & self.spock.isChecked():
            self.start = QtCore.QPointF(self.itemX - 49, self.itemY + 176)


        elif (self.clickY < (self.itemY +88)) & self.spock.isChecked():
            self.start = QtCore.QPointF(self.itemX -49, self.itemY)
        
           
        elif self.clickX < (self.itemX + 88):
            self.start = QtCore.QPointF(self.itemX, self.itemY + 49)

        elif self.clickX > (self.itemX + 88):
            self.start = QtCore.QPointF(self.itemX +176, self.itemY + 49)



        if event.buttons() == QtCore.Qt.RightButton:
            self.end = event.pos()
            self.end = self.mapToGlobal(event.pos())
            self.end = self.CircuitView.mapFromGlobal(self.end)
            self.end = self.CircuitView.mapToScene(self.end)
            self.clickX = self.end.x()
            self.clickY = self.end.y() 
            self.selectedItem = self.scene.itemAt(self.end)
            self.itemX = self.selectedItem.geometry().x()
            self.itemY = self.selectedItem.geometry().y()
            self.spock = self.selectedItem.widget()
 

        if self.spock.isFlat() == False:
                self.end = QtCore.QPointF(self.itemX +88, self.itemY)
                
                
                      
        elif (self.clickY > (self.itemY + 88)) & self.spock.isChecked():
            self.end = QtCore.QPointF(self.itemX - 49, self.itemY + 176)
    

        elif (self.clickY < (self.itemY +88)) & self.spock.isChecked():
            self.end = QtCore.QPointF(self.itemX -49, self.itemY)
            
           
        elif self.clickX < (self.itemX + 88):
            self.end = QtCore.QPointF(self.itemX, self.itemY + 49)

        elif self.clickX > (self.itemX + 88):
            self.end = QtCore.QPointF(self.itemX +176, self.itemY + 49)

    
        self.wire = QtGui.QGraphicsLineItem(QtCore.QLineF(self.start, self.end))
        self.scene.addItem(self.wire)
        
        if self.start == self.end:
            self.scene.removeItem(self.wire)

        else:
            wireCount = wireCount+1
            self.wire.setZValue(1) 
            

    
    def deleteWire(self):
        global wireCount
        if wireCount > 0:
            deleteWire = self.scene.items()[0]
            self.scene.removeItem(deleteWire)
            wireCount = wireCount - 1


    def exportXML(self):
        global wireCount, componentCount
        allComponents = self.scene.items()
        totalComponents = wireCount + componentCount

        root = minidom.Document()
        xml = root.createElement('root')
        root.appendChild(xml)

        for QtGui.QGraphicsProxyWidget in allComponents[wireCount:totalComponents]:
            ComponentWidget = QtGui.QGraphicsProxyWidget.widget()
            if ComponentWidget.isFlat() == False:
                node1 = QtGui.QGraphicsProxyWidget.pos().x() +88, QtGui.QGraphicsProxyWidget.pos().y()
                node2 = ''

            elif ComponentWidget.isChecked():
                node1 = QtGui.QGraphicsProxyWidget.pos().x() - 49, QtGui.QGraphicsProxyWidget.pos().y()
                node2 = QtGui.QGraphicsProxyWidget.pos().x() -49, QtGui.QGraphicsProxyWidget.pos().y() + 176

            else:
                node1 = QtGui.QGraphicsProxyWidget.pos().x(),  QtGui.QGraphicsProxyWidget.pos().y() + 49
                node2 = QtGui.QGraphicsProxyWidget.pos().x() + 176, QtGui.QGraphicsProxyWidget.pos().y() +49


            xmlcomponents = root.createElement('component')
            xml.appendChild(xmlcomponents)

            componentChild = root.createElement("Type")
            componentChild.appendChild(root.createTextNode(ComponentWidget.componentType)) 
            xmlcomponents.appendChild(componentChild)

            componentChild = root.createElement("Name")
            componentChild.appendChild(root.createTextNode(str(ComponentWidget.name)))
            xmlcomponents.appendChild(componentChild)

            
            componentChild = root.createElement("Value")
            componentChild.appendChild(root.createTextNode(str(ComponentWidget.value)))
            xmlcomponents.appendChild(componentChild)

            componentChild = root.createElement("Unit Metric Prefix")
            componentChild.appendChild(root.createTextNode(str(ComponentWidget.unit)))
            xmlcomponents.appendChild(componentChild)

            componentChild = root.createElement("Node")
            componentChild.appendChild(root.createTextNode(str(node1)))
            xmlcomponents.appendChild(componentChild)

            componentChild = root.createElement("Node")
            componentChild.appendChild(root.createTextNode(str(node2))) 
            xmlcomponents.appendChild(componentChild)


        for QtGui.QGraphicsLineItem in allComponents[0:wireCount]:
            WirePos = QtGui.QGraphicsLineItem.line()
            WirePos = str(WirePos)
            stringLength = len(WirePos)-1 
            wire = WirePos[20:stringLength]

            xmlwire = root.createElement('wire')
            xml.appendChild(xmlwire)

            wireChild = root.createElement("Wire")
            wireChild.appendChild(root.createTextNode(wire))
            xmlwire.appendChild(wireChild) 

            
        xmlStr = root.toprettyxml(indent = '\t')
    
        savePathFile = 'test.xml'
        with open(savePathFile, 'w') as f:
            f.write(xmlStr) 
       
 
    def addResistorButton(self):
        global componentCount
        self.Resistor2 = DragButton('')
##        self.Resistor2.setGeometry(QtCore.QRect(40, 30, 131, 61))
        self.Resistor2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Resistor2.setAcceptDrops(False)
        self.Resistor2.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Resistor.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Resistor2.setIcon(icon)
        self.Resistor2.setIconSize(QtCore.QSize(130, 70))
        self.Resistor2.setObjectName(_fromUtf8("Resistor"))
        self.Resistor2.setFlat(True)
        self.Resistor2.setCheckable(True)
        self.Resistor2.clicked.connect(self.handlebutton)
        self.Resistor2.componentType = 'Resistor'
        self.sceneResistor = self.scene.addWidget(self.Resistor2)
        componentCount = componentCount + 1 
        
        
        
    

    def addCapacitorButton(self):
        global componentCount
        self.Capacitor2 = DragButton('')
##        self.Capacitor2.setGeometry(QtCore.QRect(80, 120, 51, 51))
        self.Capacitor2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Capacitor2.setAcceptDrops(False)
        self.Capacitor2.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("capacitor.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Capacitor2.setIcon(icon1)
        self.Capacitor2.setIconSize(QtCore.QSize(130, 70))
        self.Capacitor2.setFlat(True)
        self.Capacitor2.setObjectName(_fromUtf8("Capacitor"))
        self.Capacitor2.setCheckable(True)
        self.Capacitor2.setChecked(False)
        self.Capacitor2.clicked.connect(self.handlebutton)
        self.Capacitor2.componentType = 'Capacitor'
        self.sceneCapacitor = self.scene.addWidget(self.Capacitor2)
        componentCount = componentCount + 1
        
        

    def addInductorButton(self):
        global componentCount
        self.Inductor2 = DragButton('')
##        self.Inductor2.setGeometry(QtCore.QRect(40, 280, 141, 51))
        self.Inductor2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Inductor2.setAcceptDrops(False)
        self.Inductor2.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("Inductor.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Inductor2.setIcon(icon3)
        self.Inductor2.setIconSize(QtCore.QSize(130, 70))
        self.Inductor2.setFlat(True)
        self.Inductor2.setCheckable(True)
        self.Inductor2.setObjectName(_fromUtf8("Inductor"))
        self.Inductor2.clicked.connect(self.handlebutton)
        self.Inductor2.componentType = 'Inductor'
        self.scene.addWidget(self.Inductor2)
        componentCount = componentCount + 1


    def addDiodeButton(self):
        global componentCount
        self.Diode2 = DragButton('')
##        self.Diode2.setGeometry(QtCore.QRect(50, 190, 111, 71))
        self.Diode2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Diode2.setAcceptDrops(False)
        self.Diode2.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Diode.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Diode2.setIcon(icon2)
        self.Diode2.setIconSize(QtCore.QSize(130, 70))
        self.Diode2.setFlat(True)
        self.Diode2.setObjectName(_fromUtf8("Diode"))
        self.Diode2.clicked.connect(self.handlebutton)
        self.Diode2.setCheckable(True)
        self.Diode2.componentType = 'Diode'
        self.scene.addWidget(self.Diode2)
        componentCount = componentCount + 1


    def addVoltageButton(self):
        global componentCount
        self.DCVoltageSource2 = DragButton('')
        self.DCVoltageSource2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.DCVoltageSource2.setAcceptDrops(False)
        self.DCVoltageSource2.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("DCVoltageSource.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DCVoltageSource2.setIcon(icon4)
        self.DCVoltageSource2.setIconSize(QtCore.QSize(139, 70))
        self.DCVoltageSource2.setFlat(True)
        self.DCVoltageSource2.setObjectName(_fromUtf8("DC Voltage Source"))
        self.DCVoltageSource2.clicked.connect(self.handlebutton)
        self.DCVoltageSource2.setCheckable(True)
        self.DCVoltageSource2.componentType = 'DC Voltage Source'
        self.scene.addWidget(self.DCVoltageSource2)
        componentCount = componentCount + 1


    def addBoundaryFaceButton(self):
        global componentCount
        self.BoundaryFace2 = DragButton('')
        self.BoundaryFace2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.BoundaryFace2.setAcceptDrops(False)
        self.BoundaryFace2.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("BoundaryFace.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoundaryFace2.setIcon(icon4)
        self.BoundaryFace2.setIconSize(QtCore.QSize(139, 70))
        self.BoundaryFace2.setFlat(True)
        self.BoundaryFace2.setObjectName(_fromUtf8("Boundary Face"))
        self.BoundaryFace2.clicked.connect(self.handlebutton)
        self.BoundaryFace2.componentType = 'Boundary Face'
        self.scene.addWidget(self.BoundaryFace2)
        componentCount = componentCount + 1


    def addGroundButton(self):
        global ground, componentCount 
        self.Ground2 = DragButton('')
        self.Ground2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Ground2.setAcceptDrops(False)
        self.Ground2.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("Ground.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Ground2.setIcon(icon4)
        self.Ground2.setIconSize(QtCore.QSize(139, 70))
        self.Ground2.setFlat(False)
        self.Ground2.setObjectName(_fromUtf8("Ground"))
        self.Ground2.componentType = 'Ground'
        self.scene.addWidget(self.Ground2)
        componentCount = componentCount + 1
        


    def handlebutton(self):
    
        if QtGui.qApp.keyboardModifiers() & QtCore.Qt.ShiftModifier:
            self.widgetSet = self.sender()
            self.Settings = SettingDialog(self)
            Type = self.widgetSet.componentType
            self.Settings.Type.setText(Type) 
            self.Settings.exec_()
            self.widgetSet.name = self.Settings.Name.text()
            self.widgetSet.value = self.Settings.Value.value()
            self.widgetSet.unit = self.Settings.Unit.currentText()
            self.Settings.Name.clear()
            self.Settings.Value.setValue(0) 
            self.Settings.Unit.setCurrentIndex(0) 
            
            
        if QtGui.qApp.keyboardModifiers() & QtCore.Qt.AltModifier:
            self.transform = QtGui.QTransform()
            self.transform.rotate(90)
            self.selectedItem.setTransform(self.transform)
            self.spock.setChecked(True)
            
        if QtGui.qApp.keyboardModifiers() & QtCore.Qt.ControlModifier:
            self.scene.removeItem(self.selectedItem)



class SettingDialog(QDialog, SettingDialog.Ui_SettingDialog):
    def __init__(self, parent=None):
       QtGui.QWidget.__init__(self, parent)
       self.setupUi(self)
 
       
        
app = QtGui.QApplication(sys.argv)
form = MainWindow(SettingDialog)
form.show()
app.exec_()
