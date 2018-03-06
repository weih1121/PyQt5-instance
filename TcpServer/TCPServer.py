from TcpServer.server import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtNetwork import *
import sys

class TcpServer(QWidget, Ui_Form):
    def __init__(self):
        super(TcpServer, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.tcpServer = QTcpServer(self) #指定父对象自动回收空间
        self.tcpSocket = QTcpSocket()

        self.tcpServer.listen(QHostAddress.Any, 8888)
        self.tcpServer.newConnection().connect(self.handleNewConnection)

    def handleNewConnection(self):
        self.socket = self.tcpServer.nextPendingConnection()

        #获取对方IP和端口


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tcpServer = TcpServer()
    tcpServer.show()
    sys.exit(app.exec())