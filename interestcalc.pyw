# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interestcalc.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import math

vardic = {'FV':'','PV':'','r':'','t':'','n':''}

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(356, 258)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 0, 101, 41))
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
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 50, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.textChanged.connect(self.fvChanged)
        
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 80, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.textChanged.connect(self.pvChanged)
        
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 110, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.textChanged.connect(self.rChanged)
        
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 140, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.textChanged.connect(self.tChanged)
        
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 170, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.textChanged.connect(self.nChanged)
        self.lineEdit_5.setText('12')
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 356, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def fvChanged(self):
        vardic['FV']=self.lineEdit.text()
        if list(vardic.values()).count('')==1:
            self.calcDecision()
            
    def pvChanged(self):
        vardic['PV']=self.lineEdit_2.text()
        if list(vardic.values()).count('')==1:
            self.calcDecision()
    def rChanged(self):
        vardic['r']=self.lineEdit_3.text()
        if list(vardic.values()).count('')==1:
            self.calcDecision()
    def tChanged(self):
        vardic['t']=self.lineEdit_4.text()
        if list(vardic.values()).count('')==1:
            self.calcDecision()
    def nChanged(self):
        vardic['n']=self.lineEdit_5.text()
        if list(vardic.values()).count('')==1:
            self.calcDecision()
        
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
        PV = float(vardic['PV'])
        r = float(vardic['r'])
        t = int(vardic['t'])
        n = int(vardic['n'])

        FV = round(PV*(1+r/n)**(t*n),2)
        
        vardic['FV']=str(FV)
        self.lineEdit.setText(vardic['FV'])
        
    def pvCalc(self):
        FV = float(vardic['FV'])
        r = float(vardic['r'])
        t = int(vardic['t'])
        n = int(vardic['n'])

        PV = round(FV/((1+r/n)**(t*n)),2)
        
        vardic['PV']=str(PV)
        self.lineEdit_2.setText(vardic['PV'])
        
    def rCalc(self):
        FV = float(vardic['FV'])
        PV = float(vardic['PV'])
        t = int(vardic['t'])
        n = int(vardic['n'])

        r = round(n*((FV/PV)**(1/(n*t))-1),3)

        vardic['r']=str(r)
        self.lineEdit_3.setText(vardic['r'])
        
    def tCalc(self):
        FV = float(vardic['FV'])
        PV = float(vardic['PV'])
        r = float(vardic['r'])
        n = int(vardic['n'])

        t = round(math.log(FV/PV)/(n*math.log((n+r)/n)),1)

        vardic['t']=str(t)
        self.lineEdit_4.setText(vardic['t'])
        
    def nCalc(self):
        FV = float(vardic['FV'])
        PV = float(vardic['PV'])
        r = float(vardic['r'])
        t = int(vardic['t'])
        

        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "FV = PV*(1+r/n)^tn"))
        self.label_2.setText(_translate("MainWindow", "Future Value:    FV"))
        self.label_3.setText(_translate("MainWindow", "Present Value:  PV"))
        self.label_4.setText(_translate("MainWindow", "Interest Rate:   r"))
        self.label_5.setText(_translate("MainWindow", "Time Period:      t"))
        self.label_6.setText(_translate("MainWindow", "compound per:  n"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

