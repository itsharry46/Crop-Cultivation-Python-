# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crop1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
import sys
import sqlite3

db=sqlite3.connect('crop.db')
cr=db.cursor()

nam = []
class Ui_Crop(object):

    def gettext(self):
        name = self.lineEdit.text()
        return (name)
    
    #function for soil_name retrevie
    def pressed(self):
        self.comboBox_2.clear()
        value1 = self.comboBox.currentText()
        crop = [] 
        cr.execute('select crop_name from crop where soil_name=?',(value1,))
        for row1 in cr.fetchall():
            crop.append(row1 [0])
            
        for i in crop:
            self.comboBox_2.addItem(i)
        #return (value1)
       
    #Function of crop_name retrieve 
    
    def pressed1(self):
        value2 = self.comboBox_2.currentText() 
        return (value2)
    
    def openwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.setupUi1(self.window)
        Crop.hide()
        self.window.show()
    
    def loaddata(self):
        name = self.pressed1()
        result = cr.execute('select name,crop_type,percentage from detail where name=?',(name,))                                 #instead of one i need test
        self.tableWidget.setRowCount(1)
        
        for row_no, row_data in enumerate(result):
            self.tableWidget.insertRow(row_no)
            for col_no, data in enumerate(row_data):
                self.tableWidget.setItem(row_no,col_no,QtWidgets.QTableWidgetItem(str(data)))

    
    def graph(self):
        name = self.pressed1()
        list = []
        list1 = []
        cr.execute('select crop_type,percentage from detail where name=?',(name,))
        for row in cr.fetchall():
            list.append(row [0])
            list1.append(row [1])

        slice=[list1]
        activity=(list)
        colors=['b','g','r','c','m','y','k','w']
        plt.title('Graph Analysis')
        plt.pie(slice,labels=activity,colors=colors,startangle=90,autopct='%.1f%%')
        plt.show(block=False)
        plt.pause(5)
        plt.close()
        
        
        
        
        
        
        
        
        
    def graph1(self):
        name = self.gettext()
        list2 = []
        list3 = []
        cr.execute('select s_name,per from detail1 where c_type=?',(name,))
        for row1 in cr.fetchall():
            list2.append(row1[0])
            list3.append(row1 [1])

        slice=[list3]
        activity=(list2)
        colors=['b','g','r','c','m','y','k','w']
        plt.title('Graph Analysis')
        plt.pie(slice,labels=activity,colors=colors,startangle=90,autopct='%.1f%%')
        plt.show(block=False)
        plt.pause(5)
        plt.close()
        

            
    
        
    #b = (openwindow(self))
    
    
    def setupUi(self, Crop):
        Crop.setObjectName("Crop")
        Crop.setEnabled(True)
        Crop.resize(647, 317)
        Crop.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(Crop)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 20, 161, 31))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(240, 100, 151, 22))
        self.comboBox.setObjectName("comboBox")
        
        #adding element into combobox for soil
        soil = []
        cr.execute('select soil_type from soil')
        for row in cr.fetchall():
            soil.append(row [0])
            
        for i in soil:
            self.comboBox.addItem(i)
            
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 100, 81, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 140, 91, 21))
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(240, 140, 151, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        
        #adding element into comboBox for crop
        crop = []
        value1 = ['Alluvial Soil']
        cr.execute('select crop_name from crop where soil_name=?',(value1[0],))
        for row1 in cr.fetchall():
            crop.append(row1 [0])
            
        for i in crop:
            self.comboBox_2.addItem(i)
            
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(280, 200, 75, 23))
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openwindow)                                                                        #send to next window
        self.pushButton.clicked.connect(self.loaddata)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(-40, -40, 731, 431))
        self.label_4.setStyleSheet("background-image: url(E:/Project/Python/window1.jpg);")
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 100, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.pressed)                                                                         #fetch data of soil
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 140, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.pressed1)                                                                        #fetch data of crop
        self.label_4.raise_()
        self.comboBox.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.comboBox_2.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        Crop.setCentralWidget(self.centralwidget)

        self.retranslateUi(Crop)
        QtCore.QMetaObject.connectSlotsByName(Crop)

    def retranslateUi(self, Crop):
        _translate = QtCore.QCoreApplication.translate
        Crop.setWindowTitle(_translate("Crop", "MainWindow"))
        self.label.setText(_translate("Crop", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#000000;\">Crop Cultivation</span></p></body></html>"))
        self.label_2.setText(_translate("Crop", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Soil Name</span></p></body></html>"))
        self.label_3.setText(_translate("Crop", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Crop Name</span></p></body></html>"))
        self.pushButton.setText(_translate("Crop", "Next"))
        self.label_4.setText(_translate("Crop", "TextLabel"))
        self.pushButton_3.setText(_translate("Crop", "Select"))
        self.pushButton_4.setText(_translate("Crop", "Select"))







    #def hello(self):

    def setupUi1(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(570, 413)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(90, 60, 321, 181))
        self.tableWidget.setMinimumSize(QtCore.QSize(256, 0))
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-410, -80, 971, 651))
        self.label.setStyleSheet("background-image: url(E:/Project/Python/window1.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(460, 130, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.graph)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 10, 131, 31))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 330, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.graph1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 330, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 260, 191, 41))
        self.label_3.setObjectName("label_3")
        self.label.raise_()
        self.tableWidget.raise_()
        self.pushButton.raise_()
        self.label_2.raise_()
        self.pushButton_2.raise_()
        self.lineEdit.raise_()
        self.label_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 570, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi1(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #return self.lineEdit.text()

    def retranslateUi1(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Crop Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Crop Type"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Percentage"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "Result"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#000000;\">Details of Crop</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Result"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#000000;\">Enter Crop Type Name</span></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Crop = QtWidgets.QMainWindow()
    ui = Ui_Crop()
    ui.setupUi(Crop)
    #ui.loaddata()
    Crop.show()
    sys.exit(app.exec_())
