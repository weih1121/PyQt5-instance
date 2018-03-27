# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FileTransportClient.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_IPAddress = QtWidgets.QLineEdit(Form)
        self.lineEdit_IPAddress.setObjectName("lineEdit_IPAddress")
        self.gridLayout.addWidget(self.lineEdit_IPAddress, 0, 1, 1, 2)
        self.pushButton_Connect = QtWidgets.QPushButton(Form)
        self.pushButton_Connect.setObjectName("pushButton_Connect")
        self.gridLayout.addWidget(self.pushButton_Connect, 0, 3, 2, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_PORT = QtWidgets.QLineEdit(Form)
        self.lineEdit_PORT.setObjectName("lineEdit_PORT")
        self.gridLayout.addWidget(self.lineEdit_PORT, 1, 1, 1, 2)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 2, 0, 1, 4)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 3, 0, 1, 4)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(217, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 2, 1, 1)
        self.pushButton_Disconnect = QtWidgets.QPushButton(Form)
        self.pushButton_Disconnect.setObjectName("pushButton_Disconnect")
        self.gridLayout.addWidget(self.pushButton_Disconnect, 4, 3, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "FileTransportClient"))
        self.label.setText(_translate("Form", "对方IP地址:"))
        self.pushButton_Connect.setText(_translate("Form", "连接"))
        self.label_2.setText(_translate("Form", "对方端口号:"))
        self.pushButton.setText(_translate("Form", "关闭"))
        self.pushButton_Disconnect.setText(_translate("Form", "断开连接"))

