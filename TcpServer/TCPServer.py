from TcpServer.server import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtNetwork import QTcpSocket, QTcpServer, QHostAddress, QAbstractSocket
from PyQt5.QtCore import QIODevice
from TcpClient.TCPClient import TcpClient
import sys


class TcpServer(QWidget, Ui_Form):

    def __init__(self):
        super(TcpServer, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.tcpServer = QTcpServer(self)                           #指定父对象自动回收空间 监听套接字
        self.tcpSocket = QTcpSocket(self)                           #通信套接字

        self.tcpServer.listen(QHostAddress.Any, 8888)               #any默认绑定当前网卡的所有IP
        self.tcpServer.newConnection.connect(self.handleNewConnection)
        self.ui.sendButton.clicked.connect(self.sendMessage)

    def handleNewConnection(self):
        self.tcpSocket = self.tcpServer.nextPendingConnection()       #取出建立好链接的套接字
        #获取对方IP和端口
        ip = self.tcpSocket.peerAddress
        port = self.socket.peerPort()

        tmp = "[{IP}:{Port}]".format(IP=ip, Port=port)
        self.ui.showText.setText(tmp)
        self.tcpSocket.readyRead.connect(self.showMessage)

    def sendMessage(self):
        message = self.ui.sendEdit.toPlainText()# 获取编辑区内容
        self.tcpSocket.write(str)

    def showMessage(self):
        array = self.tcpSocket.readAll()
        self.ui.showText.append(array)

    def close(self):
        self.tcpSocket.disconnectFromHost()
        self.tcpSocket.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tcpServer = TcpServer()
    tcpClient = TcpClient()
    tcpClient.show()
    tcpServer.show()
    sys.exit(app.exec())