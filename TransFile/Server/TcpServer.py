from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog
from PyQt5.QtNetwork import QTcpServer, QTcpSocket, QHostAddress
from PyQt5.QtCore import QFileInfo, QFile, QTimer
from TransFile.Server.FileTranportServer import Ui_Form
import sys

class Client(QWidget, Ui_Form):
    def __init__(self):
        super(Client, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.timer = QTimer(self)
        self.ui.pushButton_SendFile.setDisabled(True)
        self.ui.pushButton_FileSelection.setDisabled(True)
        self.tcpserver = QTcpServer()   #创建监听套接字

        self.tcpserver.listen(QHostAddress.Any, 8888)
        self.tcpserver.newConnection.connect(self.handleNewConnection)
        self.ui.pushButton_FileSelection.clicked.connect(self.SelectFile)
        self.ui.pushButton_SendFile.clicked.connect(self.SendFile)

    def handleNewConnection(self):
        self.tcpsocket = QTcpSocket()
        self.tcpsocket = self.tcpserver.nextPendingConnection()
        ip = self.tcpsocket.peerAddress().toString()
        port = self.tcpsocket.peerPort()

        self.ui.textEdit.setText("[{IP}:{Port}]".format(IP=ip, Port=port))
        self.ui.textEdit.append("\n客户端与服务器连接成功可以传文件")
        self.ui.pushButton_FileSelection.setDisabled(False)
        self.ui.pushButton_SendFile.setDisabled(False)

    def SelectFile(self):
        self.filepath =  QFileDialog.getOpenFileName(self, 'open', '../', 'ALL (*.*)')
        if self.filepath[0]:
            self.fileName = QFileInfo(self.filepath[0]).fileName()
            self.fileSize = QFileInfo(self.filepath[0]).size()
            self.ui.textEdit.append('\n %s' % self.filepath[0])
            self.ui.pushButton_SendFile.setDisabled(False)
        else:
            self.ui.textEdit.setText("打开文件失败！line：47")

    def SendFile(self):
        with open(self.filepath[0], 'rb') as f:
            for line in f:
                self.tcpsocket.write(line)

        self.ui.textEdit.setText("文件发送完毕！！")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Client()
    win.show()
    sys.exit(app.exec_())
