# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file.ui'
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
        spacerItem = QtWidgets.QSpacerItem(104, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.pushButton_readFile = QtWidgets.QPushButton(Form)
        self.pushButton_readFile.setObjectName("pushButton_readFile")
        self.gridLayout.addWidget(self.pushButton_readFile, 0, 1, 1, 1)
        self.pushButton_writeFile = QtWidgets.QPushButton(Form)
        self.pushButton_writeFile.setObjectName("pushButton_writeFile")
        self.gridLayout.addWidget(self.pushButton_writeFile, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(104, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_readFile.setText(_translate("Form", "读取文件"))
        self.pushButton_writeFile.setText(_translate("Form", "写入文件"))

