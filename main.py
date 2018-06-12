# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 19:32:01 2018

@author: lab
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QDialog, QCalendarWidget,QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate
from PyQt5 import QtCore as core
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon
 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import random
import numpy as np
import time
import matplotlib
matplotlib.use('Qt5Agg')
#style.use('fivethirtyeight')
class CalendarDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.cal = QCalendarWidget(self)
        self.cal.clicked[QDate].connect(self.showDate)   
        self.resize(300, 300)
        self.cal.resize(300, 300)
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.cal)  
        self.lbl = QLabel(self)
        date = self.cal.selectedDate() 
        vbox.addWidget(self.lbl)
    def showDate(self, date):     
        self.lbl.setText(date.toString())  
        
    
class GraphDialog(QDialog):
    def __init__(self,parent):
        super().__init__(parent)
        self.fig = Figure(figsize=(500, 400), dpi=80)
        self.canvas = FigureCanvas(self.fig)
       
        #self.canvas.setSizePolicy(self,QSizePolicy.Expanding,QSizePolicy.Expanding)
        #self.canvas.updateGeometry(self)
        self.vbox = QVBoxLayout(self)
        self.count=0   
        self.xStart=10
        self.yStart=1 
        print ('init')
        self.button1=QPushButton('Start graph')   
        self.button1.clicked.connect(self.plot2)
        self.vbox.addWidget(self.button1) 
        self.button2=QPushButton('Stop graph')  
        self.button2.clicked.connect(self.stop)
        self.vbox.addWidget(self.button2)
        self.vbox.addWidget(self.canvas)
        #self.setLayout(self.vbox)
    def plot2(self):
        
        self.fig.clear()
        self.axes = self.fig.add_subplot(111)
        self.axes.set_title('PyQt Matplotlib Example')
        self.canvas.draw() 
        self.xStart+=1
        self.yRandom=self.yStart*round(10*random.random(),3)
       
        self.animate(1)
    def animate(self,i):
        self.axes.set_title('PyQt Matplotlib Example')
        data=open('C:\\Users\\lab\\Desktop\\xy.txt','r').read()
        lines=data.split('\n')
        self.count+=1
        print( 'count= {}'.format(self.count))
        xs=[]
        ys=[]
        for line in lines:
            if(len(line))>1:
                x, y= line.split(',')
                xs.append(x)
                print (x)
                ys.append(y)
        self.axes.plot(xs,ys,'*-') 
        self.axes.set_xlim([0,50])
        self.axes.set_ylim([0,15]) 
        self.canvas.draw()             
#        self.axes.set_xticks([10,20,30,40,50])
#        self.axes.set_yticks([1.0, 2.0, 15.0])             
        #major_ticks = np.arange(10,50, 10)    
        #self.axes.set_xticks(major_ticks)       
    def stop(self):
        self.timer.stop()
        sys.exit()

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def openCalendar(self):
        self.calendarWidget = CalendarDialog(self)
        self.calendarWidget.show()  
    def openGraph(self):
        self.graphWidget=GraphDialog(self)
        self.graphWidget.show()
    def initUI(self):               
        
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAct = QAction(QIcon('C:\\Users\\lab\\Desktop\\exit.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)

        calendarAction = QAction(QIcon('C:\\Users\\lab\\Desktop\\calendar.png'), 'Calendar', self)
        calendarAction.triggered.connect(self.openCalendar)

        graphAction = QAction(QIcon('C:\\Users\\lab\\Desktop\\graph.png'), 'Graph', self)
        graphAction.triggered.connect(self.openGraph)

        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File') 
        fileMenu.addAction(exitAct)        
        fileMenu=menubar.addMenu('&Options')
        fileMenu.addAction(calendarAction)
        fileMenu = menubar.addMenu('&Plot') 
        fileMenu.addAction(graphAction)        


        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAct)
        
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')    
        self.show()
        
ex = Example()




