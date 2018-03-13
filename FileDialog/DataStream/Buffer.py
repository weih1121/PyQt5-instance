from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QBuffer, QIODevice, QByteArray
import sys

class Buffer(QWidget):
    def __init__(self):
        super(Buffer, self).__init__()
        self.setWindowTitle("Buffer Test")

        self.opbuffer()

    def opbuffer(self):
        memfile = QBuffer()                 #创建内存文件
        memfile.open(QIODevice.WriteOnly)
        memfile.write(QByteArray(1024, "121121121121221222121221212"))
        memfile.write(QByteArray("787887878787878878787878778"))
        memfile.close()
        print(memfile.close())


if __name__ == '__main__':
    app =QApplication(sys.argv)
    win = Buffer()
    win.show()
    sys.exit(app.exec())