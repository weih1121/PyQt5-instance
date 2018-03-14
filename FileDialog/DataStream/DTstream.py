from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import QIODevice, QFile, QDataStream
import sys

class OPFile(QWidget):
    def __init__(self):
        super(OPFile, self).__init__()
        self.setWindowTitle("QDataStream Test")
        self.WriteFile()
        self.ReadFile()

    def WriteFile(self):
        file = QFile("./doc/test.txt")             #创建文件对象
        isok = file.open(QIODevice.WriteOnly)      #文件以只写的方式打开

        if isok:
            stream = QDataStream(file)             #创建数据流， 和file文件关联，相当于往数据流中输入数据相当于向数据中写数据
            stream.writeQString("内涵更重要")
            stream.writeInt(15)
            file.close()

    def ReadFile(self):
        file = QFile("./doc/test.txt")             #创建文件对象
        isok = file.open(QIODevice.ReadOnly)       #以只写的方式打开文件对象
        if isok:
            stream = QDataStream(file)             #创建数据流，和文件对象关联
            str = stream.readQString()             #读的时候按写的顺序取
            num = stream.readInt()
            print(str)
            print(num)
            file.close()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = OPFile()
    win.show()
    sys.exit(app.exec())
