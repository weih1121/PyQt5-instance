# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FileTranportServer.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(333, 327)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 2)
        self.pushButton_FileSelection = QtWidgets.QPushButton(Form)
        self.pushButton_FileSelection.setObjectName("pushButton_FileSelection")
        self.gridLayout.addWidget(self.pushButton_FileSelection, 1, 0, 1, 1)
        self.pushButton_SendFile = QtWidgets.QPushButton(Form)
        self.pushButton_SendFile.setObjectName("pushButton_SendFile")
        self.gridLayout.addWidget(self.pushButton_SendFile, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "FileTransportServer"))
        self.pushButton_FileSelection.setText(_translate("Form", "文件选择"))
        self.pushButton_SendFile.setText(_translate("Form", "发送文件"))

