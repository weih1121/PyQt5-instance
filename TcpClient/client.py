# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.portLineEdit = QtWidgets.QLineEdit(Form)
        self.portLineEdit.setObjectName("portLineEdit")
        self.gridLayout.addWidget(self.portLineEdit, 0, 0, 1, 2)
        self.connectButton = QtWidgets.QPushButton(Form)
        self.connectButton.setObjectName("connectButton")
        self.gridLayout.addWidget(self.connectButton, 0, 2, 2, 1)
        self.IPLineEdit = QtWidgets.QLineEdit(Form)
        self.IPLineEdit.setObjectName("IPLineEdit")
        self.gridLayout.addWidget(self.IPLineEdit, 1, 0, 1, 2)
        self.showText = QtWidgets.QTextEdit(Form)
        self.showText.setReadOnly(True)
        self.showText.setObjectName("showText")
        self.gridLayout.addWidget(self.showText, 2, 0, 1, 3)
        self.sendText = QtWidgets.QTextEdit(Form)
        self.sendText.setObjectName("sendText")
        self.gridLayout.addWidget(self.sendText, 3, 0, 1, 3)
        self.sendButton = QtWidgets.QPushButton(Form)
        self.sendButton.setObjectName("sendButton")
        self.gridLayout.addWidget(self.sendButton, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(217, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        self.closeButton = QtWidgets.QPushButton(Form)
        self.closeButton.setObjectName("closeButton")
        self.gridLayout.addWidget(self.closeButton, 4, 2, 1, 1)

        self.retranslateUi(Form)
        self.closeButton.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "客户端"))
        self.connectButton.setText(_translate("Form", "connect"))
        self.sendButton.setText(_translate("Form", "send"))
        self.closeButton.setText(_translate("Form", "close"))

