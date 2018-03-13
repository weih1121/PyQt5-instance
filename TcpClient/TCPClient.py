import sys
from PyQt5.QtWidgets import QApplication, QWidget
from TcpClient.client import Ui_Form
from PyQt5.QtNetwork import QTcpSocket, QHostAddress
from PyQt5.QtCore import QByteArray, QDataStream, QIODevice

class TcpClient(QWidget, Ui_Form):
    def __init__(self):
        super(TcpClient, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.tcpSocket = QTcpSocket(self)
        self.ui.connectButton.clicked.connect(self.buttonConnect)
        self.tcpSocket.connected.connect(self.sucessConnect)
        self.ui.sendButton.clicked.connect(self.sendButtonClicked)
        self.tcpSocket.readyRead.connect(self.receiveMessage)

    def buttonConnect(self):
        ip = self.ui.IPLineEdit.text()
        port = self.ui.portLineEdit.text()
        self.tcpSocket.connectToHost(QHostAddress(ip), int(port))#主动和服务器建立连接

    def sucessConnect(self):
        self.ui.showText.setText("成功和服务器建立连接")

    def sendButtonClicked(self):
        message = self.ui.sendText.toPlainText()
        self.communication = QByteArray()
        stream = QDataStream(self.communication, QIODevice.WriteOnly)
        stream.writeQString(message)
        self.tcpSocket.write(self.communication)

    def receiveMessage(self):
        array = self.tcpSocket.readAll()
        self.ui.showText.append(str(array))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tcpClient = TcpClient()
    tcpClient.show()
    sys.exit(app.exec())