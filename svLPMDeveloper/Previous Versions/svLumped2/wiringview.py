
from PyQt4 import QtGui, QtCore
from dragbutton import DragButton

class WiringView(QtGui.QGraphicsView):
    def __init__(self, parent):
        QtGui.QGraphicsView.__init__(self, parent)
        self.setScene(QtGui.QGraphicsScene(self))
        self.setSceneRect(QtCore.QRectF(self.viewport().rect()))
##        self.scene().addItem(QtGui.QGraphicsLineItem(QtCore.QLineF(0, 0, 100,100)))


    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.RightButton:
            self._start = event.pos()

##        super(WiringView, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        start = QtCore.QPointF(self.mapToScene(self._start))
        end = QtCore.QPointF(self.mapToScene(event.pos()))
        self.scene().addItem(QtGui.QGraphicsLineItem(QtCore.QLineF(start, end)))

##        super(WiringView, self).mouseReleaseEvent(event)
