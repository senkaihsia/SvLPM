from PyQt4 import QtCore, QtGui
import sys

class Example(QtGui.QWidget):        
    def __init__(self):
        super(Example, self).__init__()            
        self.initUI()


    def initUI(self):                           
        qbtn = QtGui.QPushButton('Quit', self)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)
        qbtn.mousePressEvent = self.getPos

        self.setGeometry(0, 0, 1024, 768)
        self.setWindowTitle('Quit button')    
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        self.show()

    def getPos (self, event):
        x = event.pos().x()
        y = event.pos().y()
        print x, y 





        
        
        

    








def main():        
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
