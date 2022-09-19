from cProfile import label
import sys
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from structs import *

def draw_point(scene, pi):
    pen = QtGui.QPen()
    pen.setWidth(1)
    
    scene.addLine(pi.x,pi.y,pi.x,pi.y, pen)   
    scene.update()

def draw_line(scene, pi, pf):
    
    pen = QtGui.QPen()
    pen.setWidth(1)
    
    scene.addLine(pi.x,pi.y,pf.x,pf.y, pen)   
    scene.update()

def draw_wireframe(scene, wireframe):
    
    pen = QtGui.QPen()
    pen.setWidth(1)

    for j in range(0, len(wireframe.pontos)):
                if(j == 0):
                    scene.addLine(wireframe.pontos[j].x,wireframe.pontos[j].y,wireframe.pontos[j].x,wireframe.pontos[j].y, pen)
                else:
                    scene.addLine(wireframe.pontos[j - 1].x,wireframe.pontos[j - 1].y,wireframe.pontos[j].x,wireframe.pontos[j].y, pen)

def draw_objects(scene, objs):
    pen = QtGui.QPen()
    pen.setWidth(2)
    for i in range(0, len(objs)):

        if(isinstance(objs[i], Wireframe)):
            for j in range(0, len(objs[i].pontos)):
                if(j == 0):
                    scene.addLine(objs[i].pontos[j].x,objs[i].pontos[j].y,objs[i].pontos[j].x,objs[i].pontos[j].y, pen)
                else:
                    scene.addLine(objs[i].pontos[j - 1].x,objs[i].pontos[j - 1].y,objs[i].pontos[j].x,objs[i].pontos[j].y, pen)
        
        if(isinstance(objs[i], Line)):
            scene.addLine(objs[i].xi,objs[i].yi,objs[i].xf,objs[i].yf, pen)        
    
        if(isinstance(objs[i], Point)):
            scene.addLine(objs[i].x,objs[i].y,objs[i].x,objs[i].y, pen)
    scene.update()