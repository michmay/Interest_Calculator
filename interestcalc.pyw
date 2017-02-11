# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interestcalc.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import math
from currency_tostr import *
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

vardic = {'FV':'','PV':'','r':'','t':'','n':'12'}

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        MainWindow.resize(680, 240)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(75, 0, 101, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 101, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 101, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 170, 101, 16))
        self.label_6.setObjectName("label_6")

        self.lineEdit = MyLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 50, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        #self.lineEdit.textEdited.connect(self.fvChanged)
        
        self.lineEdit_2 = MyLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 80, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText('15000')
        #self.lineEdit_2.textEdited.connect(self.pvChanged)

        self.lineEdit_3 = MyLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 110, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        #self.lineEdit_3.textEdited.connect(self.rChanged)
        self.lineEdit_3.setText('0.06')
        
        self.lineEdit_4 = MyLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 140, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        #self.lineEdit_4.setText('12')
        #self.lineEdit_4.textEdited.connect(self.tChanged)
        
        self.lineEdit_5 = MyLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 170, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        #self.lineEdit_5.textEdited.connect(self.nChanged)
        self.lineEdit_5.setText('12')




        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 726, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionRestart = QtWidgets.QAction(MainWindow)
        self.actionRestart.setObjectName("actionRestart")
        self.menuFile.addAction(self.actionRestart)
        self.menubar.addAction(self.menuFile.menuAction())
        self.actionRestart.triggered.connect(self.restart_fields)

        self.l = QtWidgets.QGroupBox(self.centralwidget)
        self.grid = QtWidgets.QGridLayout(self.l)
        self.l.setGeometry(QtCore.QRect(250, 30, 400, 200))
        self.l.setTitle("plot")
        #self.l.setSizePolicy(QtWidgets.sizeHint(),QtWidgets.sizeHint())


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def changed(self):
        vardic['FV'] = self.lineEdit.text()
        vardic['PV'] = self.lineEdit_2.text()
        vardic['r'] = self.lineEdit_3.text()
        vardic['t'] = self.lineEdit_4.text()
        vardic['n'] = self.lineEdit_5.text()
        if list(vardic.values()).count('') == 1:
            self.calcDecision()


            self.sc = MyMplCanvas(self.centralwidget, width=250, height=150, dpi=100)
            self.grid.addWidget(self.sc)

    def calcDecision(self):
        for name, val in vardic.items():
            if val == '':
                if name == 'FV':
                    self.fvCalc()
                if name == 'PV':
                    self.pvCalc()
                if name == 'r':
                    self.rCalc()
                if name == 't':
                    self.tCalc()
                if name == 'n':
                    self.nCalc()

    def fvCalc(self):
        PV = float(cur_to_str(vardic['PV']))
        r = float(vardic['r'])
        t = int(vardic['t'])
        n = int(vardic['n'])

        FV = round(PV*(1+r/n)**(t*n), 2)

        vardic['FV'] = str_to_cur(str(FV))
        self.lineEdit.setText(vardic['FV'])

    def pvCalc(self):
        FV = float(cur_to_str(vardic['FV']))
        r = float(vardic['r'])
        t = int(vardic['t'])
        n = int(vardic['n'])

        PV = round(FV/((1+r/n)**(t*n)), 2)

        vardic['PV'] = str_to_cur(str(PV))
        self.lineEdit_2.setText(vardic['PV'])

    def rCalc(self):
        FV = float(cur_to_str(vardic['FV']))
        PV = float(cur_to_str(vardic['PV']))
        t = int(vardic['t'])
        n = int(vardic['n'])

        r = round(n*((FV/PV)**(1/(n*t))-1), 3)

        vardic['r'] = str(r)
        self.lineEdit_3.setText(vardic['r'])

    def tCalc(self):
        FV = float(cur_to_str(vardic['FV']))
        PV = float(cur_to_str(vardic['PV']))
        r = float(vardic['r'])
        n = int(vardic['n'])

        t = round(math.log(FV/PV)/(n*math.log((n+r)/n)), 1)

        vardic['t']=str(t)
        self.lineEdit_4.setText(vardic['t'])

    def nCalc(self):
        FV = float(cur_to_str(vardic['FV']))
        PV = float(cur_to_str(vardic['PV']))
        r = float(vardic['r'])
        t = int(vardic['t'])



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Interest Calculator"))
        MainWindow.setWindowIcon(QtGui.QIcon(QtGui.QPixmap('pwis16.png')))
        self.label.setText(_translate("MainWindow", "FV = PV*(1+r/n)^tn"))
        self.label_2.setText(_translate("MainWindow", "Future Value:    FV"))
        self.label_3.setText(_translate("MainWindow", "Present Value:  PV"))
        self.label_4.setText(_translate("MainWindow", "Interest Rate:   r"))
        self.label_5.setText(_translate("MainWindow", "Time Period:      t"))
        self.label_6.setText(_translate("MainWindow", "compound per:  n"))

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionRestart.setText(_translate("MainWindow", "Restart"))




    def restart_fields(self):
        vardic = {'FV': '', 'PV': '', 'r': '', 't': '', 'n': '12'}
        self.lineEdit.setText(vardic['FV'])
        self.lineEdit_2.setText(vardic['PV'])
        self.lineEdit_3.setText(vardic['r'])
        self.lineEdit_4.setText(vardic['t'])
        self.lineEdit_5.setText(vardic['n'])


class MyLineEdit(QtWidgets.QLineEdit, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyLineEdit, self).__init__(parent)
        self.readyToEdit = True

    def mousePressEvent(self, e):
        super(MyLineEdit, self).mousePressEvent(e)  # required to deselect on 2e click
        if self.readyToEdit:
            self.selectAll()
            self.readyToEdit = False



    def focusOutEvent(self, event):
        print('This widget is out of focus')
        ui.changed()
        try:
            if float(self.text()) > 100:

                self.setText(str_to_cur(self.text()))
        except:
            pass
        QtWidgets.QLineEdit.focusOutEvent(self, QtGui.QFocusEvent(QtCore.QEvent.FocusOut))
        self.readyToEdit = True

    """def focusInEvent(self, event):
        print('This widget is in focus')

        QtWidgets.QLineEdit.focusInEvent(self, QtGui.QFocusEvent(QtCore.QEvent.FocusIn))
        #self.selectAll()
    """


    #to do,  '${:,.2f}'.format(1234.5) to go to dollars n back


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(1,1,1)
        # We want the axes cleared every time plot() is called
        #self.axes.hold(False)
        FigureCanvas.__init__(self, figure=fig)
        self.compute_initial_figure()

        #

        self.setParent(parent)
        FigureCanvas.setGeometry(self,300,20,100,100)
        FigureCanvas.setSizePolicy(self,
                QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)

        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):

        pv = float(cur_to_str(vardic['PV']))
        r = float(vardic['r'])
        n = float(vardic['n'])
        timelength = int(vardic['t'])# * int(n)
        time = list(range(timelength))

        value = [pv*(1+r/n)**(n*t) for t in time]
        self.axes.plot(time, value)
        self.draw()






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

