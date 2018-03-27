import sys
from server import Ui_Form
from PyQt5.QtNetwork import QUdpSocket, QHostAddress
from PyQt5.QtCore import QDataStream, QIODevice, QByteArray
from PyQt5.QtWidgets import QWidget, QApplication

class UdpCommunication(Ui_Form, QWidget):
    def __init__(self):
        super(UdpCommunication, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.udpSocket = QUdpSocket()                              #创建socket

        self.udpSocket.bind(8888)                                  #绑定端口并监听
        self.ui.pushButton_send.clicked.connect(self.handleSend)
        self.udpSocket.readyRead.connect(self.handleRecv)

    # def writeDatagram(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
    #     """
    #     writeDatagram(self, bytes, Union[QHostAddress, QHostAddress.SpecialAddress], int) -> int
    #     writeDatagram(self, Union[QByteArray, bytes, bytearray], Union[QHostAddress, QHostAddress.SpecialAddress], int) -> int
    #     writeDatagram(self, QNetworkDatagram) -> int
    #     """
    #     return 0

    def handleSend(self):
        text = self.ui.textEdit.toPlainText()
        ip = self.ui.lineEdit_IP.text()
        port = int(self.ui.lineEdit_PORT.text())

        # message = QByteArray()
        # data = QDataStream(message, QIODevice.WriteOnly)
        # data.writeQString(text)
        message = bytes(text, encoding="utf-8")
        self.udpSocket.writeDatagram(message, QHostAddress(ip), port)

    # def readDatagram(self, p_int):  # real signature unknown; restored from __doc__
    #     """ readDatagram(self, int) -> Tuple[bytes, QHostAddress, int] """
    #     pass

    def handleRecv(self):
        buf = bytes()
        buf, ip, port = self.udpSocket.readDatagram(1024)
        message = buf.decode()
        self.ui.textEdit.setText(message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = UdpCommunication()
    win.show()
    sys.exit(app.exec_())