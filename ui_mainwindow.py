# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from fnmatch import translate
from typing import List
from PyQt5 import QtCore, QtGui, QtWidgets
from cProfile import label
import sys
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from canvas_draw import *

from structs import *
from transforms import *

from ui_newobject import *

objectList = []

class Ui_MainWindow(object):
    def newObject(self, MainWindow):
            dialog = NewObject()
            dialog.exec()
            print(objectList)
            if (self.objectsListWidget.count() != len(objectList)):
                self.objectsListWidget.addItem(objectList[-1][0])
            MainWindow.updateViewport()
            

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(810, 646)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.functionsGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.functionsGroupBox.setGeometry(QtCore.QRect(0, 0, 211, 601))
        self.functionsGroupBox.setObjectName("functionsGroupBox")
        self.objectsListWidget = QtWidgets.QListWidget(self.functionsGroupBox)
        self.objectsListWidget.setGeometry(QtCore.QRect(10, 50, 181, 121))
        self.objectsListWidget.setObjectName("objectsListWidget")
        self.objectsLabel = QtWidgets.QLabel(self.functionsGroupBox)
        self.objectsLabel.setGeometry(QtCore.QRect(10, 30, 67, 17))
        self.objectsLabel.setObjectName("objectsLabel")
        self.groupBox_2 = QtWidgets.QGroupBox(self.functionsGroupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 220, 191, 361))
        self.groupBox_2.setObjectName("groupBox_2")
        self.upButton = QtWidgets.QPushButton(self.groupBox_2)
        self.upButton.setGeometry(QtCore.QRect(40, 70, 51, 25))
        self.upButton.setObjectName("upButton")
        
        

        #self.upButton.clicked.connect(lambda: draw_line(self.scene, pi, pf))

        self.leftButton = QtWidgets.QPushButton(self.groupBox_2)
        self.leftButton.setGeometry(QtCore.QRect(10, 100, 51, 25))
        self.leftButton.setObjectName("leftButton")
        self.rightButton = QtWidgets.QPushButton(self.groupBox_2)
        self.rightButton.setGeometry(QtCore.QRect(70, 100, 51, 25))
        self.rightButton.setObjectName("rightButton")
        self.downButton = QtWidgets.QPushButton(self.groupBox_2)
        self.downButton.setGeometry(QtCore.QRect(40, 130, 51, 25))
        self.downButton.setObjectName("downButton")
        self.inButton = QtWidgets.QPushButton(self.groupBox_2)
        self.inButton.setGeometry(QtCore.QRect(140, 80, 41, 25))
        self.inButton.setObjectName("inButton")
        self.outButton = QtWidgets.QPushButton(self.groupBox_2)
        self.outButton.setGeometry(QtCore.QRect(140, 110, 41, 25))
        self.outButton.setObjectName("outButton")
        self.stepEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.stepEdit.setGeometry(QtCore.QRect(50, 30, 61, 31))
        self.stepEdit.setObjectName("stepEdit")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 41, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(120, 35, 21, 21))
        self.label_3.setObjectName("label_3")
        self.transformObjectButton = QtWidgets.QPushButton(self.functionsGroupBox)
        self.transformObjectButton.setGeometry(QtCore.QRect(110, 180, 81, 25))
        self.transformObjectButton.setObjectName("transformObjectButton")
        self.newObjectButton = QtWidgets.QPushButton(self.functionsGroupBox)
        self.newObjectButton.setGeometry(QtCore.QRect(10, 180, 91, 25))
        self.newObjectButton.setObjectName("newObjectButton")
        self.viewportGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.viewportGroupBox.setGeometry(QtCore.QRect(220, 10, 581, 481))
        self.viewportGroupBox.setObjectName("viewportGroupBox")
        self.graphicsView = QtWidgets.QGraphicsView(self.viewportGroupBox)
        self.graphicsView.setGeometry(QtCore.QRect(5, 31, 573, 423))
        self.graphicsView.setObjectName("graphicsView")
        
        self.newObjectButton.clicked.connect(lambda: self.newObject(MainWindow))

        self.scene = QGraphicsScene(0, 0, 570, 420)
        
        self.messagesTextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.messagesTextBrowser.setGeometry(QtCore.QRect(220, 500, 581, 101))
        self.messagesTextBrowser.setObjectName("messagesTextBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 810, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Interactive Graphics System"))
        self.functionsGroupBox.setTitle(_translate("MainWindow", "Functions Menu"))
        self.objectsLabel.setText(_translate("MainWindow", "Objects"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Window"))
        self.upButton.setText(_translate("MainWindow", "UP"))
        self.leftButton.setText(_translate("MainWindow", "LEFT"))
        self.rightButton.setText(_translate("MainWindow", "RIGHT"))
        self.downButton.setText(_translate("MainWindow", "DOWN"))
        self.inButton.setText(_translate("MainWindow", "IN"))
        self.outButton.setText(_translate("MainWindow", "OUT"))
        self.label_2.setText(_translate("MainWindow", "Step:"))
        self.label_3.setText(_translate("MainWindow", "%"))
        self.transformObjectButton.setText(_translate("MainWindow", "Transform"))
        self.newObjectButton.setText(_translate("MainWindow", "New Object"))
        self.viewportGroupBox.setTitle(_translate("MainWindow", "Viewport"))
        
        self.graphicsView.setScene(self.scene)

        


class MainWindow(QMainWindow):
    def __init__(self):
        self.win_size = []
        self.win_size.append(0)
        self.win_size.append(0)
        self.win_size.append(800)
        self.win_size.append(600)

        self.list_objects = []
        self.p1 = Point(0, 0)
        self.p2 = Point(220, 80)
        self.p3 = Point(60, 300)
        self.line1 = Line(self.p1, self.p2)

        #self.list_objects.append(self.p1)
        #self.list_objects.append(self.p2)
        self.list_objects.append(self.line1)
        self.list_objects.append(self.p3)

        self.pa = Point(200, 0)
        self.pb = Point(200, 50)
        self.pc = Point(250, 50)
        self.pd = Point(250, 0)
        self.quad = Wireframe()
        self.quad.add_ponto(self.pa)
        self.quad.add_ponto(self.pb)
        self.quad.add_ponto(self.pc)
        self.quad.add_ponto(self.pd)
        self.quad.add_ponto(self.pa)
        self.list_objects.append(self.quad)





        

        

        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #self.quad = translation(self.quad, 300, 0)
        #self.quad = rotation(self.quad, (1.2708))
        #self.quad = self_rotation(self.quad, 2.1415926)
        p1 = Point(0, 0)
        p2 = Point(250, 200)
        #draw_point(self.ui.scene, p1)
        #draw_line(self.ui.scene, p1, p2, win_size)
        #self.ui.upButton.clicked.connect(lambda: (draw_objects(self.ui.scene, self.list_objects, win_size)))
        #draw_objects(self.ui.scene, self.list_objects, win_size)
        #draw_wireframe(self.ui.scene, self.quad, win_size)

    def updateViewport(self):
        self.ui.scene.clear()
        draw_objects(self.ui.scene, objectList, self.win_size)

class NewObject(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        self.ui = Ui_NewObject()
        self.ui.setupUi(self)
        self.ui.addPointButton.clicked.connect(self.addWireframePoint)
    
    def accept(self):
        if (self.ui.nameEdit.text() == ""):
            QMessageBox.about(self, "Error", "Define the object name!")
            return
        if (self.ui.tabWidget.currentIndex() == 0):
            #Point
            if (self.ui.xpointEdit.text() == "" or self.ui.ypointEdit.text() == ""):
                QMessageBox.about(self, "Error", "Define the point correctly!")
                return
            point = Point(int(self.ui.xpointEdit.text()), int(self.ui.ypointEdit.text()))
            print(point.x.__str__() + ", " + point.y.__str__())
            objectList.append((self.ui.nameEdit.text(),point))
        elif (self.ui.tabWidget.currentIndex() == 1):
            #Line
            if (self.ui.x1lineEdit.text() == "" or self.ui.y1lineEdit.text() == "" or
                self.ui.x2lineEdit.text() == "" or self.ui.y2lineEdit.text() == ""):
                QMessageBox.about(self, "Error", "Define the line correctly")
                return
            pi = Point(int(self.ui.x1lineEdit.text()), int(self.ui.y1lineEdit.text()))
            pf = Point(int(self.ui.x2lineEdit.text()), int(self.ui.y2lineEdit.text()))
            line = Line(pi, pf)
            objectList.append((self.ui.nameEdit.text(),line))
        else:
            #Wireframe
            wireframe = Wireframe()
            for i in range(self.ui.pointListWidget.count()):
                print(self.ui.pointListWidget.item(i).text())
                p = Point(int(self.ui.pointListWidget.item(i).text()[1:self.ui.pointListWidget.item(i).text().index(",")]),
                int(self.ui.pointListWidget.item(i).text()[self.ui.pointListWidget.item(i).text().index(",")+1:self.ui.pointListWidget.item(i).text().__len__()-1]))
                print(str(p.x) + ", " + str(p.y))
                wireframe.add_ponto(p)
            objectList.append((self.ui.nameEdit.text(),wireframe))
        
        return super().accept()

    def reject(self) -> None:
        return super().reject()

    def addWireframePoint(self):
        if (self.ui.x1wireframeEdit.text() == "" or self.ui.y1wireframeEdit.text() == ""):
            QMessageBox.about(self, "Error", "Define the point correctly")
            return
        self.ui.pointListWidget.addItem("("+self.ui.x1wireframeEdit.text() +","+self.ui.y1wireframeEdit.text()+")")

    

if __name__ == "__main__":
    app = QApplication(sys.argv)    

    window = MainWindow()
    
    window.show()

    sys.exit(app.exec())
