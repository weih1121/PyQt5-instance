from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog
from PyQt5.QtNetwork import QTcpServer, QTcpSocket, QHostAddress
from PyQt5.QtCore import QIODevice, QDataStream, QDir, QFileInfo, QFile, QTimer
from TransFile.Server.FileTranportServer import Ui_Form
import sys

class Client(QWidget, Ui_Form):
    def __init__(self):
        super(Client, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_SendFile.setDisabled(True)
        self.ui.pushButton_FileSelection.setDisabled(False)
        self.fileToSend = None          #定义和文件相关的信息
        self.fileSize = 0               #文件大小
        self.fileName = 0               #文件名
        self.sendSize = 0               #已经发送文件大小
        self.time = QTimer()            #设置定时器

        self.tcpserver = QTcpServer()   #创建监听套接字

        self.tcpserver.listen(QHostAddress.Any, 8888)
        self.tcpserver.newConnection.connect(self.handleNewConnection)
        #self.ui.pushButton_FileSelection.click.connect(self.SelectFile)
        # self.ui.pushButton_SendFile.click.connect(self.SendFile)

    def handleNewConnection(self):
        self.tcpsocket = QTcpSocket()
        self.tcpsocket = self.tcpserver.nextPendingConnection()
        ip = self.tcpsocket.peerAddress().toString()
        port = self.tcpsocket.peerPort()

        self.ui.textEdit.setText("[{IP}:{Port}]".format(IP=ip, Port=port))
        self.ui.textEdit.append("\n客户端与服务器连接成功可以传文件")
        self.ui.pushButton_FileSelection.setDisabled(False)
        self.tcpsocket.readyRead.connect(self.HandleReceive)

    def SelectFile(self):
        filepath = QFileDialog.getOpenFileName('open', '../', 'ALL (*.*)')
        if filepath:
            self.fileName = None
            self.fileSize = 0

            #获取文件信息
            info = QFileInfo(filepath)
            self.fileName = info.fileName()
            self.fileSize = info.size()

            #只读方式打开文件，指定文件名
            self.file = QFile()
            isok = self.file.open(QIODevice.ReadOnly)
            if not isok:
                print('只读方式打开文件失败！')

            #提示打开文件路径
            self.ui.textEdit.append('\n %s'%filepath)
            self.ui.pushButton_SendFile.setDisabled(False)
        else:
            print("打开文件出错")



    def SendFile(self):
        #先发送文件头部信息
        head = "{FileName}##{FileSize}".format(FileName=self.fileName, FileSize=self.fileSize)
        head.encode(encoding='utf-8')
        len = self.tcpsocket.write(head)
        if len > 0:
            #发送真正的文件信息
            #防止TCP粘包 需要通过定时器延时20ms
            self.time.start(20)
            self.SendAction()
            self.time.stop()
        else:
            pass

    def HandleReceive(self):
        pass

    def SendAction(self):
        buf = bytes()
        len = 0
        while self.fileSize != self.sendSize:
            buf = self.file.read(4 * 1024)
            self.tcpsocket.write(buf, len)
            self.sendSize += len

        #判断文件是否发送完毕
        if self.sendSize == self.fileSize:
            self.ui.textEdit.append("\n文件发送完毕")
            self.file.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Client()
    win.show()
    sys.exit(app.exec_())
