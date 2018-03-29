from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from PyQt5.QtNetwork import QTcpServer, QTcpSocket, QHostAddress
from PyQt5.QtCore import QIODevice, QDataStream, QFile
from TransFile.Client.FileTransportClient import Ui_Form
import sys

class Client(QWidget, Ui_Form):
    def __init__(self):
        super(Client, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.file = QFile()

        self.tcpsocket = QTcpSocket()
        self.ui.pushButton_Connect.clicked.connect(self.ConnectToServer)
        self.tcpsocket.connected.connect(self.SuccessConnect)
        self.tcpsocket.readyRead.connect(self.HandleReceive)

    def ConnectToServer(self):
        ip = self.ui.lineEdit_IPAddress.text()
        port = self.ui.lineEdit_PORT.text()
        self.tcpsocket.connectToHost(QHostAddress(ip), int(port))

    def SuccessConnect(self):
        self.ui.textEdit.setText("成功和服务器建立连接")

    def HandleReceive(self):
        with open('../FileRecv/test.txt', 'wb') as f:
            buf = self.tcpsocket.readAll()
            f.write(buf)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Client()
    win.show()
    sys.exit(app.exec_())
