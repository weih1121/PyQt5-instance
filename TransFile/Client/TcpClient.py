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
        self.fileName = None
        self.fileSize = None
        self.receSize = 0
        self.isStart = False        #判断是不是文件头

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
        buf = bytes()
        buf = self.tcpsocket.readAll()
        if self.isStart == False:
            self.isStart = True
            #解析头部信息 并且进行初始化工作 再打开文件
            buf = buf.decode()
            self.fileName = buf.session('##, 0, 0')
            self.fileSize = int(buf.session('##', 1, 1))

            self.file.setFileName(self.fileName)
            isok = self.open(QIODevice.WriteOnly)
            if False == isok:
                print('打开文件失败')
        else:
            len = self.file.write(buf)
            self.receSize += len

            if self.receSize == self.fileSize:
                self.file.close()
                QMessageBox(self, '完成', "文件接收完成")





if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Client()
    win.show()
    sys.exit(app.exec_())
