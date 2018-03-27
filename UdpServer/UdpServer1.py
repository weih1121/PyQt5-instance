import sys
from server1 import Ui_Form
from PyQt5.QtNetwork import QUdpSocket, QHostAddress
from PyQt5.QtCore import QDataStream, QIODevice, QByteArray
from PyQt5.QtWidgets import QWidget, QApplication

class UdpCommunication(Ui_Form, QWidget):
    def __init__(self):
        super(UdpCommunication, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.udpSocket = QUdpSocket()                              #socket

        self.udpSocket.bind(9999)
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

        message = text.encode()
        self.udpSocket.writeDatagram(message, QHostAddress(ip), port)

    # def readDatagram(self, p_int):  # real signature unknown; restored from __doc__
    #     """ readDatagram(self, int) -> Tuple[bytes, QHostAddress, int] """
    #     pass

    # def readDatagram(self, p_int): # real signature unknown; restored from __doc__
    #     """ readDatagram(self, int) -> Tuple[bytes, QHostAddress, int] """
    #     pass
    def handleRecv(self):
        ip = QHostAddress()
        buf = bytes()
        buf, ip, port = self.udpSocket.readDatagram(1024)
        ip = ip.toString()
        message = buf.decode()
        self.ui.textEdit.setText('{Ip},{Port}:{Message}'.format(Ip=ip, Port=port, Message=message))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = UdpCommunication()
    win.show()
    sys.exit(app.exec_())