
from PyQt4 import QtGui, QtCore

class wireWidget(QtGui.QWidget):
    def __init__(self, point1, point2):
        self.p1 = point1
        self.p2 = point2

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(QtGui.QPen(QtCore.Qt.black))
        painter.drawLine(self.p1, self.p2)
        painter.end()

    
