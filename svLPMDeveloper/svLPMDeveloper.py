#! /usr/bin/env python
#! python
#! /usr/bin/python

# svLPM.py GUI created and developed by Senkai Hsia at Stanford University Marsden Cardiovascular Biomechanics Computation Laboratory July-August 2017
# The following is a commented version of the svLPM.py main code for the SimVascular Lumped Parameter Modeller for developers/curious individuals. 

# Acknowledgement and most sincere gratitude to the following for their invaluable assistance, support and mentorship: 
# svLPM GUI was created under the direction of CBCL Advisors: Dr Hongzhi Lan, Justin Tran, Gabriel Maher
# and Stanford CBCL Principle Investigator: Professor Alison L. Marsden

# Confessions:
# The original developer is not an experienced programmer: you're reading his first ever python program
# and thus the code is not optimised and only has relatively basic funtionality for creating LPM 
# Please excuse any repeated code/programming conventions not obeyed/python or coding terminology mistakes/any Star Trek references
# Please send bug reports to hongzhi@stanford.edu and/or Senkai.Hsia@Westminster.org.uk 
# Please refer to the Developer Documentation for more information and good luck! 


from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QPushButton
from PyQt4.QtGui import QGraphicsScene
from PyQt4.QtCore import Qt

#Importing all required modules from the PyQt4 framework. Please refer to the Developer Documentation for information about installation. 

from xml.dom import minidom
from xml.dom.minidom import Node
import xml.etree.ElementTree as ET
import os
import sys

# Importing all required modules native to python

import svLPMGui
from dragbutton import DragButton
import SettingDialog

# Importing modules from python files for the UI generated code from QtDesigner (see documentation) and the custom class QPushButton to enable drag and drop functionality. 


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

# enables encoding for readable text in pushbuttons 



wireCount = 0
componentCount = 0

# global variables needed to count items in the scene


class MainWindow(QMainWindow, svLPMGui.Ui_MainWindow):

# creates the MainWindow Class and imports the window attributes from the UI generated python file. 


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
       self.scene = self.CircuitView.scene()
       self.actionOpen.triggered.connect(self.openFile)
       self.actionSave_2.triggered.connect(self.XMLFileSave)
       self.actionSaveAs.triggered.connect(self.fileSaveAs)
       self.actionQuit_2.triggered.connect(self.Quit)
       self.actionClear.triggered.connect(self.Clear) 
       self.statusbar.setStyleSheet("QStatusBar{padding-left:8px;background:rgba(0,0,0,0);color:black;font-weight:bold;}")
       self.statusbar.messageChanged.connect(self.statusbarChanged)
       self.windowCancel = False

# adds functionality to all the widgets/menubar/statusbar in the mainwindow and connects their trigger event to the relevent method
       
       
  

       
    def mousePressEvent(self, event):
        global wireCount

# method for enabling click events to draw wires: note that all the component widgets in the scene are QGraphicsProxyWidgets which have embedded custom QPushButtons
# called DragButtons with drag and drop functionality handelled by the QPushbutton widget itself. 

        try:
    
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
                
# This part of the method sets the position of the mouse click event.
# First the position of the click is mapped to global, then to the scene
# and accesses the embedded DragButton widget in the QGraphicsProxyWidget that was pressed.
# the middle button was needed due to the LeftButton already being used for the Drag and Drop functionality and the clash would break the drag and drop. 

                
            if (self.clickY > (self.itemY + 88)) &self.spock.rotated == True :
                self.start = QtCore.QPointF(self.itemX - 49, self.itemY + 176)


            elif (self.clickY < (self.itemY +88)) & self.spock.rotated == True:
                self.start = QtCore.QPointF(self.itemX -49, self.itemY)

# checks whether the button has been rotated using the rotated class attribute from the DragButton class            
               
            elif self.clickX < (self.itemX + 88):
                self.start = QtCore.QPointF(self.itemX, self.itemY + 49)

            elif self.clickX > (self.itemX + 88):
                self.start = QtCore.QPointF(self.itemX +176, self.itemY + 49)

# This is the node assignment function: the dimensions of the QGraphicsProxy Widgets are all 176 by 98: therefore sets start position of button to node closest to the click.
# Note that the .geometry() function gives the x and y value of the "origin point" of the widget, which is the (0,0) of the widget but these co-ordinates have been mapped to the scene
# the node closest to the click is determined by whether the button is rotated or not: with the node assignment depending on whether the click is left or right of the central
# x axis for horizontal buttons or the y axis for rotated buttons 
                



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

# reimplements position handling from the above, but with the RightButton on the mouse. 
     

            if self.spock.componentType == "Ground":
                    self.end = QtCore.QPointF(self.itemX +88, self.itemY)
# checks if the component is a ground button: if so sets its end to one node in the top centre of the button
                    
                    
                          
            elif (self.clickY > (self.itemY + 88)) & self.spock.rotated == True:
                self.end = QtCore.QPointF(self.itemX - 49, self.itemY + 176)
        

            elif (self.clickY < (self.itemY +88)) & self.spock.rotated == True:
                self.end = QtCore.QPointF(self.itemX -49, self.itemY)
                
               
            elif self.clickX < (self.itemX + 88):
                self.end = QtCore.QPointF(self.itemX, self.itemY + 49)

            elif self.clickX > (self.itemX + 88):
                self.end = QtCore.QPointF(self.itemX +176, self.itemY + 49)
                

            wire = QtCore.QLineF(self.start, self.end)

            self.wire = QtGui.QGraphicsLineItem(wire)

            self.scene.addItem(self.wire)
# draws wire between two click positions
            
            if self.start == self.end:
                self.scene.removeItem(self.wire)
# intentional workaround: as both self.start and self.end are the same, it deletes the initial "wire" at the point of the first click. When setting another variable
#as the second click position (e.g. self.clickX2), it breaks the ability to draw another wire from a seperate click position as self.start will remain as the starting point. This workaround
# thus enables the self.start position to remain the start position of the wire (which is then removed) and then to be changed after the middle button is clicked on another component. 

            else:
                wireCount = wireCount+1
                self.wire.setZValue(1)
# increased the wireCount number to match the number of wires in the scene, and sets the ZValue for the QGraphicsLineItem to 1 to enable all the wires to stack first
#when the QGraphicsScene.items() function is run and returns an ordered list of all the items in the scene (Line Items and ProxyWidgets) 

     

        except Exception as err:
            self.statusbar.setStyleSheet("QStatusBar{padding-left:8px;background:rgba(255,0,0,255);color:black;font-weight:bold;}")
            self.statusbar.showMessage("Error: Component Not Pressed!", msecs = 1500)
#QOL improvement: shows red error message when a component is not selected with a click event

             
           
    def statusbarChanged(self, args):
        if not args:
            self.statusbar.setStyleSheet("QStatusBar{padding-left:8px;background:rgba(0,0,0,0);color:black;font-weight:bold;}")
#when the statusbar is changed after the message timer has expired, resets the statusbar colour to transparent


    def closeEvent(self, event):
        self.Quit()
        if self.windowCancel == True:
            event.ignore()
            self.confirmExit.close()
#method to overide the native closeEvent when exiting the program from the mainwindow X to bring up the confirmExit dialog
        

    def Clear(self):
        self.clearScene = QtGui.QMessageBox()
        self.clearScene.setIcon(QtGui.QMessageBox.Warning)
        self.clearScene.setText("Are you sure you want to clear the circuit?")
        self.clearScene.setInformativeText("Any changes will be lost without saving")
        self.clearScene.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.Cancel)
        self.clearScene.buttonClicked.connect(self.clearOptions)
        self.clearScene.exec_()

#Creates a MessageBox Dialog to confirm clearing the scene of all items

    def clearOptions(self, button):
        buttonPressed = button.text()

        if buttonPressed == "Cancel":
            self.clearScene.close()

        else:
            self.scene.clear() 
            



    def deleteWire(self):
        global wireCount
        if wireCount > 0:
            deleteWire = self.scene.items()[0]
# accesses the first item in the list (which will always be a wire due to the ZValue being 1 and the component's ZValue being default 0) and deletes it
            self.scene.removeItem(deleteWire)
            wireCount = wireCount - 1
        else:
            self.statusbar.setStyleSheet("QStatusBar{padding-left:8px;background:rgba(255,0,0,255);color:black;font-weight:bold;}")
            self.statusbar.showMessage("Error: No Wires Exist (yet!)", msecs = 1500)

# QOL message when no wires are in the scene

    def fileSaveAs(self):
        self.fileName = str(QtGui.QFileDialog.getSaveFileName(self, "Save File as XML"))
        self.XMLFileSave()

# Opens the Save File Dialog native to pyqt, accesses the string of the file and implements the XMLFileSave method
        

 
    def Quit(self):
        self.confirmExit = QtGui.QMessageBox()
        self.confirmExit.setIcon(QtGui.QMessageBox.Warning)
        self.confirmExit.setText("Are you sure you want to Quit?")
        self.confirmExit.setInformativeText("Any changes will be lost without saving!")
        self.confirmExit.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.Cancel)
        self.confirmExit.buttonClicked.connect(self.quitOptions)
        self.confirmExit.exec_()

    def quitOptions(self, button):
        buttonPressed = button.text()

        if buttonPressed == "Cancel":
            self.windowCancel = True
            self.confirmExit.close() 

    
        else:
            sys.exit()
# Quit Dialog when File>Quit is accessed 


               
    def XMLFileSave(self):
        global wireCount, componentCount

# method for exporting the circuit drawn to XML File
        
        allComponents = self.scene.items()
# returns a list of all the items in the scene, with the wires stacking first, then components
        totalComponents = wireCount + componentCount

        root = minidom.Document()
        xml = root.createElement('circuit')
        root.appendChild(xml)
# creates the framework for an XML File and sets the root of the XML File as "circuit" using the minidom API from xml.dom 

        if componentCount != 0 and wireCount != 0:

# Implements ability that user can only save file when there are both components and wires on the scene. 


            for QtGui.QGraphicsProxyWidget in allComponents[wireCount:totalComponents]:
                ComponentWidget = QtGui.QGraphicsProxyWidget.widget()

# Slices the list to access the components which will be located between the wires and the end of the list and accesses the embedded widget
#loops over all the components in the allcomponents list

                if ComponentWidget.componentType == "Ground":
                    node1 = ((QtGui.QGraphicsProxyWidget.pos().x() +88), (QtGui.QGraphicsProxyWidget.pos().y()))
                    node2 = ''
#the ground button only has 1 node

                elif ComponentWidget.rotated == True :
                    node1 = ((QtGui.QGraphicsProxyWidget.pos().x() - 49), (QtGui.QGraphicsProxyWidget.pos().y()))
                    node2 = ((QtGui.QGraphicsProxyWidget.pos().x() -49), (QtGui.QGraphicsProxyWidget.pos().y() + 176))

                else:
                    node1 = (QtGui.QGraphicsProxyWidget.pos().x(),  (QtGui.QGraphicsProxyWidget.pos().y() + 49))
                    node2 = ((QtGui.QGraphicsProxyWidget.pos().x() + 176), (QtGui.QGraphicsProxyWidget.pos().y() +49))


                xmlcomponents = root.createElement('Component')
                xmlcomponents.setAttribute('type', ComponentWidget.componentType) 
                xmlcomponents.setAttribute('value', str(ComponentWidget.value))
                xmlcomponents.setAttribute('metricPrefix', str(ComponentWidget.unit))
                xmlcomponents.setAttribute('name', str(ComponentWidget.name))
                xmlcomponents.setAttribute('rotated', str(ComponentWidget.rotated))
                xmlcomponents.setAttribute('DialogIndex', str(ComponentWidget.comboBoxIndex))
                xml.appendChild(xmlcomponents)

# creates child elements in the circuit root element and adds attributes from the class members(attributes) from each DragButton Component (Note that all attributes must be strings) 

                componentNode1 = root.createElement("Node")
                componentNode1.appendChild(root.createTextNode(str(node1)))
                xmlcomponents.appendChild(componentNode1)

                componentNode2 = root.createElement("Node")
                componentNode2.appendChild(root.createTextNode(str(node2))) 
                xmlcomponents.appendChild(componentNode2)

# adds the node positions for the component as child elements of the component element

                
            for wires in allComponents[0:wireCount]:
                WirePos = wires.line()
                WirePos = str(WirePos)
                stringLength = len(WirePos)-1 
                wire = WirePos[20:stringLength]

                xmlwire = root.createElement('wire')
                xml.appendChild(xmlwire)

                wirePos = root.createElement('wirePos')
                wirePos.appendChild(root.createTextNode(wire))
                xmlwire.appendChild(wirePos)

# slices the list to access only the wires which will stack first in the list and loops over each wire

        
                                
                
            xmlStr = root.toprettyxml(indent = '\t')
# adds the xml top string and indents for elements

            try:
                if self.sender() == self.actionSaveAs:
                    self.savePathFile = self.fileName + ".xml"
# checks if the sender of the method is File>SaveAs..., if so, it adds the .xml tag to the filename
    
                    

                elif self.sender() == self.actionSave_2:
                    self.savePathFile = self.fileName
# check if the sender of the method is File>Save, if so, it sets the self.filename (which was set when the user opened the XML file) as the filename and so overwrites its contents
# with the changes made
                     
            
                with open(self.savePathFile, 'w') as f:
                    f.write(xmlStr)
                    self.statusbar.showMessage("Circuit Saved to XML File", msecs = 3000)
# exports the circuit to the XML File or creates the file if it doesn't yet exist 

                    

            except Exception as err:
                self.statusbar.setStyleSheet("QStatusBar{padding-left:8px;background:rgba(255,0,0,255);color:black;font-weight:bold;}")
                self.statusbar.showMessage("Error: XML File does not exist! : Use Save As", msecs = 4000)
# an exception is generated if the user attempts to File>Save a previously unsaved circuit as the self.filename will not exist.
                
            
        elif componentCount == 0:
            self.statusbar.setStyleSheet("QStatusBar{padding-left:8px;background:rgba(255,0,0,255);color:black;font-weight:bold;}")
            self.statusbar.showMessage("Error: No Components Added!", msecs = 1600)

        elif wireCount == 0:
            self.statusbar.setStyleSheet("QStatusBar{padding-left:8px;background:rgba(255,0,0,255);color:black;font-weight:bold;}")
            self.statusbar.showMessage("Error: No Wires Added!", msecs = 1600)

# QOL improvement: error messages if the user's circuit has not wires or no components
          



    def openFile(self):
        global wireCount

# this method enables XML files to be opened, parsed, and rebuilds the circuit from the XML file parse

        try:
            self.fileName = str(QtGui.QFileDialog.getOpenFileName())        
            nameSplit = self.fileName.split("/") or self.fileName.split ("\\")                                               
            nameSplitNumber = (len(nameSplit)-1)
            xmlFile = nameSplit[nameSplitNumber]
            xmlLoad= ET.parse(xmlFile)
            circuit = xmlLoad.getroot()

# updates the self.fileName to the string of the opened file (this time with the .xml tag)
# returns a string of the file path. therefore the string is split to access only the final index with the "name.xml"
# method then parses the XML file and accesses the root (which should be "circuit") using the element tree API which was chosen instead of using minidom again because
# it is easier to access sub or child elements using element tree. 

            for components in circuit.findall("Component"):
                Type = components.get("type")
                Value = float(components.get("value"))
                Name = components.get("name")
                MetricPrefix = components.get("metricPrefix")
                Rotated = components.get("rotated")
                DialogIndex = int(components.get("DialogIndex"))
#accesses all the component attributes from the XML File and assigns them to a local variable for each component
                
                PosNode = components.find("Node").text
                componentPos= PosNode.split(",")
                componentX = float(componentPos[0].replace("(", ''))
                componentY = float(componentPos[1].replace(")", ''))

#accesses the string of the FIRST node subelement for each component, splits it and returns the float of the X and Y co-ordinates


# the following code the rebuilds the scene from the XML File by checking the component Type string and checking if the componenet is rotated
# it then re-adds the component to the scene using the original add component methods below and adds back all the original settings
# the position of the component is achieved by accessing the first node position, then setting the co-ordinates back to the origin point of the widget in the scene co-ordinates
# for horizontal components, the origin point is the top left hand corner of the widget, while for rotated components it is the top right hand corner
# (which is rotated by 90 degrees about the origin point of a horizontal widget) 

                if Type == "Resistor" and Rotated == "False":
                    self.addResistorButton()
                    componentY = componentY-49
                    self.sceneResistor.setPos(componentX, componentY)
                    loadWidget = self.sceneResistor.widget()
                    loadWidget.value = Value
                    loadWidget.name = Name
                    loadWidget.unit = MetricPrefix
                    loadWidget.comboBoxIndex = DialogIndex
   
                    

                if Type == "Capacitor" and Rotated == "False":
                    self.addCapacitorButton()
                    componentY = componentY-49
                    self.sceneCapacitor.setPos(componentX, componentY)
                    loadWidget = self.sceneCapacitor.widget()
                    loadWidget.value = Value
                    loadWidget.name = Name
                    loadWidget.unit = MetricPrefix
                    loadWidget.comboBoxIndex = DialogIndex
      
                    

                if Type == "Inductor" and Rotated == "False":
                    self.addInductorButton()
                    componentY = componentY-49
                    self.sceneInductor.setPos(componentX, componentY)
                    loadWidget = self.sceneInductor.widget()
                    loadWidget.value = Value
                    loadWidget.name = Name
                    loadWidget.unit = MetricPrefix
                    loadWidget.comboBoxIndex = DialogIndex
     

                if Type == "Diode" and Rotated == "False":
                    self.addDiodeButton()
                    componentY = componentY-49
                    self.sceneDiode.setPos(componentX, componentY)
                    loadWidget = self.sceneDiode.widget()
                    loadWidget.value = Value
                    loadWidget.name = Name
                    loadWidget.unit = MetricPrefix
                    loadWidget.comboBoxIndex = DialogIndex
   

                if Type == "DC Voltage Source" and Rotated == "False":
                    self.addVoltageButton()
                    componentY = componentY-49
                    self.sceneDCVoltageSource.setPos(componentX, componentY)
                    loadWidget = self.sceneDCVoltageSource.widget()
                    loadWidget.value = Value
                    loadWidget.name = Name
                    loadWidget.unit = MetricPrefix
                    loadWidget.comboBoxIndex = DialogIndex
     

                if Type == "Boundary Face" and Rotated == "False":
                    self.addBoundaryFaceButton()
                    componentY = componentY-49
                    self.sceneBoundaryFace.setPos(componentX, componentY)
                    loadWidget = self.sceneBoundaryFace.widget()
                    loadWidget.value = Value
                    loadWidget.name = Name
                    loadWidget.unit = MetricPrefix
                    loadWidget.comboBoxIndex = DialogIndex
                   

                if Type == "Ground":
                    self.addGroundButton()
                    componentX = componentX - 88
                    self.sceneGround.setPos(componentX, componentY)
                    loadWidget = self.sceneGround.widget()
                    loadWidget.value = Value
                    loadWidget.name = Name
                    loadWidget.unit = MetricPrefix
                    loadWidget.comboBoxIndex = DialogIndex
# ground button only has single node
                
                    
# code for all the rotated buttons:

                if Type == "Resistor" and Rotated == "True":
                    self.addResistorButton()
                    componentX = componentX+49
                    self.sceneResistor.setPos(componentX, componentY)
                    self.transform = QtGui.QTransform()
                    self.transform.rotate(90)
                    self.sceneResistor.setTransform(self.transform)
                    loadWidget = self.sceneResistor.widget()
                    loadWidget.value = Value
                    loadWidget.name = Name
                    loadWidget.unit = MetricPrefix
                    loadWidget.comboBoxIndex = DialogIndex
                    loadWidget.rotated = True 
             

                if Type == "Capacitor" and Rotated == "True":
                    self.addCapacitorButton()
                    componentX = componentX+49
                    self.sceneCapacitor.setPos(componentX, componentY)
                    self.transform = QtGui.QTransform()
                    self.transform.rotate(90)
                    self.sceneCapacitor.setTransform(self.transform)
                    loadWidget = self.sceneCapacitor.widget()
                    loadWidget.value = Value
                    loadWidget.name = Name
                    loadWidget.unit = MetricPrefix
                    loadWidget.comboBoxIndex = DialogIndex
                    loadWidget.rotated = True 
    

                if Type == "Inductor" and Rotated == "True":
                    self.addInductorButton()
                    componentX = componentX+49
                    self.sceneInductor.setPos(componentX, componentY)
                    self.transform = QtGui.QTransform()
                    self.transform.rotate(90)
                    self.sceneInductor.setTransform(self.transform)
                    loadWidget = self.sceneInductor.widget()
                    loadWidget.value = Value
                    loadWidget.name = Name
                    loadWidget.unit = MetricPrefix
                    loadWidget.comboBoxIndex = DialogIndex
                    loadWidget.rotated = True 
        

                if Type == "Diode" and Rotated == "True":
                    self.addDiodeButton()
                    componentX = componentX+49
                    self.sceneDiode.setPos(componentX, componentY)
                    self.transform = QtGui.QTransform()
                    self.transform.rotate(90)
                    self.sceneDiode.setTransform(self.transform)
                    loadWidget = self.sceneDiode.widget()
                    loadWidget.value = Value
                    loadWidget.name = Name
                    loadWidget.unit = MetricPrefix
                    loadWidget.comboBoxIndex = DialogIndex
                    loadWidget.rotated = True 
        
    
                if Type == "DC Voltage Source" and Rotated == "True":
                    self.addVoltageButton()
                    componentX = componentX+49
                    self.sceneDCVoltageSource.setPos(componentX, componentY)
                    self.transform = QtGui.QTransform()
                    self.transform.rotate(90)
                    self.sceneDCVoltageSource.setTransform(self.transform)
                    loadWidget = self.sceneDCVoltageSource.widget()
                    loadWidget.value = Value
                    loadWidget.name = Name
                    loadWidget.unit = MetricPrefix
                    loadWidget.comboBoxIndex = DialogIndex
                    loadWidget.rotated = True 
         

                if Type == "Boundary Face" and Rotated == "True":
                    self.addBoundaryFaceButton()
                    componentX = componentX+49
                    self.sceneBoundaryFace.setPos(componentX, componentY)
                    self.transform = QtGui.QTransform()
                    self.transform.rotate(90)
                    self.sceneBoundaryFace.setTransform(self.transform)
                    loadWidget = self.sceneBoundaryFace.widget()
                    loadWidget.value = Value
                    loadWidget.name = Name
                    loadWidget.unit = MetricPrefix
                    loadWidget.comboBoxIndex = DialogIndex
                    loadWidget.rotated = True 
           

                    
            for wires in circuit.findall("wire"):
                wireText = wires.find("wirePos").text
                wirePos = wireText.split(",")
                wireX1 = float(wirePos[0])
                wireY1 = float(wirePos[1])
                wireX2 = float(wirePos[2])
                wireY2 = float(wirePos[3])
                self.wire = QtGui.QGraphicsLineItem(QtCore.QLineF(wireX1, wireY1, wireX2, wireY2))
                self.scene.addItem(self.wire)
                self.wire.setZValue(1)
                wireCount = wireCount + 1

# all the wires in the XML file are accessed, the string of the start and end position is split into 2 pairs of co-ordinate values
#the x and y co-ordinates are then accessed from the respective string index and the wire is re-added and wirecount updated

            self.statusbar.showMessage("XML File \"" + xmlFile + "\" Loaded Successfully", msecs = 5000)

        except Exception as err:
            self.statusbar.setStyleSheet("QStatusBar{padding-left:8px;background:rgba(255,0,0,255);color:black;font-weight:bold;}")
            self.statusbar.showMessage("Error: Unable to Load File \"" + xmlFile + "\"", msecs = 4000)
# a try function was intiated at the start of the method as if the user opens a non XML file, it will print "unable to load file" error in the status bar

            

# The following are the original add component methods from the mainwindow once svLPM is launched. These add the specified component to the scene
# A custom QPushButton is created from the DragButtons class from dragbuttons.py in the svLPModeller file.
# The componentType class member/attribute of the Dragbutton is updated to the type of component created 
# The DragButton is then added to the scene and embedded into a QGraphicsProxyWidget
# the component count is increased to match the number of total components in the scene
                     

    def addResistorButton(self):
        global componentCount
        self.Resistor2 = DragButton('')
        self.Resistor2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Resistor2.setAcceptDrops(False)
        self.Resistor2.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Resistor.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Resistor2.setIcon(icon)
        self.Resistor2.setIconSize(QtCore.QSize(130, 70))
        self.Resistor2.setObjectName(_fromUtf8("Resistor"))
        self.Resistor2.setFlat(True)
        self.Resistor2.clicked.connect(self.handlebutton)
        self.Resistor2.componentType = 'Resistor'
        self.sceneResistor = self.scene.addWidget(self.Resistor2)
        componentCount = componentCount + 1 
        
        
        

    def addCapacitorButton(self):
        global componentCount
        self.Capacitor2 = DragButton('')
        self.Capacitor2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Capacitor2.setAcceptDrops(False)
        self.Capacitor2.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("capacitor.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Capacitor2.setIcon(icon1)
        self.Capacitor2.setIconSize(QtCore.QSize(130, 70))
        self.Capacitor2.setFlat(True)
        self.Capacitor2.setObjectName(_fromUtf8("Capacitor"))
        self.Capacitor2.clicked.connect(self.handlebutton)
        self.Capacitor2.componentType = 'Capacitor'
        self.sceneCapacitor = self.scene.addWidget(self.Capacitor2)
        componentCount = componentCount + 1
        
        

    def addInductorButton(self):
        global componentCount
        self.Inductor2 = DragButton('')
        self.Inductor2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Inductor2.setAcceptDrops(False)
        self.Inductor2.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("Inductor.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Inductor2.setIcon(icon3)
        self.Inductor2.setIconSize(QtCore.QSize(130, 70))
        self.Inductor2.setFlat(True)
        self.Inductor2.setObjectName(_fromUtf8("Inductor"))
        self.Inductor2.clicked.connect(self.handlebutton)
        self.Inductor2.componentType = 'Inductor'
        self.sceneInductor = self.scene.addWidget(self.Inductor2)
        componentCount = componentCount + 1


    def addDiodeButton(self):
        global componentCount
        self.Diode2 = DragButton('')
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
        self.Diode2.componentType = 'Diode'
        self.sceneDiode = self.scene.addWidget(self.Diode2)
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
        self.DCVoltageSource2.componentType = 'DC Voltage Source'
        self.sceneDCVoltageSource=self.scene.addWidget(self.DCVoltageSource2)
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
        self.sceneBoundaryFace= self.scene.addWidget(self.BoundaryFace2)
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
        self.Ground2.setFlat(True)
        self.Ground2.setObjectName(_fromUtf8("Ground"))
        self.Ground2.componentType = 'Ground'
        self.Ground2.ground = True
        self.sceneGround= self.scene.addWidget(self.Ground2)
        componentCount = componentCount + 1
        

#all the components added when clicked then call the handlebutton method below which can implement a variety of functions


    def handlebutton(self):
        global componentCount
    
        if QtGui.qApp.keyboardModifiers() & QtCore.Qt.ShiftModifier:
# This function allows the user to assign settings to a component
            self.widgetSet = self.sender()
# returns the DragButton which called the handlebutton method
            self.Settings = SettingDialog(self)
# returns the Component Setting Dialog
            Type = self.widgetSet.componentType
            Name = self.widgetSet.name
            Value = self.widgetSet.value
            ComboBoxIndex = self.widgetSet.comboBoxIndex
# assigns the existing class member/attributes of the Dragbutton sender to local variables

            
            
            self.Settings.Type.setText(Type)
            self.Settings.Name.setText(Name)
            self.Settings.Value.setValue(Value)
            self.Settings.Unit.setCurrentIndex(ComboBoxIndex)
# sets the lineEdits, label and the combobox to the current class member/attribute of the DragButton
# by default if they have not been set previously they are empty strings, integers or floats respectively
            
            self.Settings.exec_()
# executes and launches the Dialog (must be .exec_ () to retrieve inputs and NOT .show()) 

            self.widgetSet.name = self.Settings.Name.text()
            self.widgetSet.value = self.Settings.Value.value()
            self.widgetSet.unit = self.Settings.Unit.currentText()
            self.widgetSet.comboBoxIndex = self.Settings.Unit.currentIndex()
# when save is pressed, sets the current inputs of lineedits, doublespinbox and the combobox to the class member/attributes of the DragButton

            
            
        if QtGui.qApp.keyboardModifiers() & QtCore.Qt.AltModifier:
# This function allows the user to rotate a componenent: NOTE need to press middle button and then left click and ALT/OPTION
            self.transform = QtGui.QTransform()
            self.transform.rotate(90)
            self.selectedItem.setTransform(self.transform)
# THe middle button must be Pressed first to assign a self.selectedItem, which accesses QProxyWidget.
#The QProxyWidget is then rotated (couldn't use self.sender() because the DragButton cannot be rotated) 

            rotated = self.sender()
            rotated.rotated = True
# The DragButton which called the function is then accessed (Note not the QGraphicsProxyWidget which it is embedded in)
# The boolean rotated class attribute is then set as True, and so when the XML File is generated or rebuilt, the rotated attribute is "True"

            
            
        if QtGui.qApp.keyboardModifiers() & QtCore.Qt.ControlModifier:
# This function allows the user to delete the component and all associated settings
            self.scene.removeItem(self.selectedItem )
# removes the selected component QGraphicsProxyWidget from the scene (and so middle press first) 
            componentCount = componentCount -1
    


       



class SettingDialog(QDialog, SettingDialog.Ui_SettingDialog):
    def __init__(self, parent=None):
       QtGui.QWidget.__init__(self, parent)
       self.setupUi(self)

# sets up the UI for the Dialog

       
        
app = QtGui.QApplication(sys.argv)
form = MainWindow(SettingDialog)
form.show()
app.exec_()
# executes the mainwindow 
