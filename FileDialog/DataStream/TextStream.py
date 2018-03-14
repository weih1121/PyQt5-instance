from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QTextStream, QFile, QIODevice
import sys

#通过文本方式读取文件可以在读取的时候指定编码， 智能操作文本

class TSStream(QWidget):
    def __init__(self):
        super(TSStream, self).__init__()
        self.setWindowTitle("TextStream 例子")
        self.writeFile()
        self.readFile()

    def writeFile(self):
        file = QFile("./doc/test.txt")                              #写文件第一步首先创建文件对象
        #file.setFileName("./doc/test.txt")                         #第二步将文件路径与文件关联，有2中方式，一是在创建文件对象时指定路径，二是通过setFileName指定

        isok = file.open(QIODevice.WriteOnly)                       #第三步打开文件，返回值为True/False
        if isok:
            stream = QTextStream(file)                              #创建文本流并且与打开的文件相关联，向文本流读写数据相当于从文件读写数据
            stream.setCodec("gbk")
            school = "nenu102"
            num = 52
            stream << school << num                                 #向文本流中写入数据通过<<操作符
            file.close()                                            #文本流操作结束后，关闭文件

    def readFile(selfself):
        file = QFile()
        file.setFileName("./doc/test.txt")

        isok = file.open(QIODevice.ReadOnly)
        if isok:
            stream = QTextStream(file)
            #stream.setCodec("utf8")
            str = stream.readAll()
            print(str)

            file.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TSStream()
    win.show()
    sys.exit(app.exec())