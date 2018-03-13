from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QTextStream, QFile, QIODevice
import sys

#通过文本方式读取文件可以在读取的时候指定编码， 智能操作文本
    # def read(self, p_int): # real signature unknown; restored from __doc__
    #     """ read(self, int) -> str """
    #     return ""
    #
    # def readAll(self): # real signature unknown; restored from __doc__
    #     """ readAll(self) -> str """
    #     return ""
    #
    # def readLine(self, maxLength=0): # real signature unknown; restored from __doc__
    #     """ readLine(self, maxLength: int = 0) -> str """
    #     return ""

    #返回值都是空 如何读数据 有点令我难以理解

class TSStream(QWidget):
    def __init__(self):
        super(TSStream, self).__init__()
        self.setWindowTitle("TextStream 例子")
        #self.writeFile()
        self.readFile()

    def writeFile(self):
        file = QFile()
        file.setFileName("./doc/test.txt")

        isok = file.open(QIODevice.WriteOnly)
        if isok:
            stream = QTextStream(file)
            print(type(stream))
            stream.setCodec("utf8")
            print(stream)
            file.close()

    def readFile(selfself):
        file = QFile()
        file.setFileName("./doc/demo.txt")

        isok = file.open(QIODevice.ReadOnly)
        if isok:
            stream = QTextStream(file)
            stream.setCodec("utf8")
            l, str = stream.read()

            file.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TSStream()
    win.show()
    sys.exit(app.exec())