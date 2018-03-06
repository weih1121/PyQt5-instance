import sys
from PyQt5.QtWidgets import QApplication, QWidget
from TcpClient.client import Ui_Form

class TcpClient(QWidget, Ui_Form):
    def __init__(self):
        super(TcpClient, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tcpClient = TcpClient()
    tcpClient.show()
    sys.exit(app.exec())