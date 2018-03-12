from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog
from PyQt5.QtCore import QFile, QIODevice
from file import Ui_Form
import sys

class FileOperation(QWidget, Ui_Form):
    def __init__(self):
        super(FileOperation, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton_readFile.clicked.connect(self.readFile)
        self.ui.pushButton_writeFile.clicked.connect(self.writeFile)


    # def readFile(self):
    #      fname = QFileDialog.getOpenFileName(self, "Open File", "./", "Txt (*.txt)")
    #                                                                                     #打开文件 返回一个字符串第一个是路径， 第二个是要打开文件的类型
    #                                                                                     #如果用户主动关闭文件对话框，则返回值为空
    #
    #      if fname[0]:                                                                   #判断路径非空
    #          f = QFile(fname[0])                                                       #创建文件对象，不创建文件对象也不报错 也可以读文件和写文件
    #                                                                                     #open()会自动返回一个文件对象
    #          f = open(fname[0], "r")                                                    #打开路径所对应的文件， "r"以只读的方式 也是默认的方式
    #          with f:
    #             data = f.read()
    #             self.ui.textEdit.setText(data)
    #          f.close()

    def writeFile(self):
        fname = QFileDialog.getSaveFileName(self, "Write File", "./", "All (*.*)")      #写入文件首先获取文件路径
        if fname[0]:                                                                    #如果获取的路径非空
            f = open(fname[0], "w")                                                     #以写入的方式打开文件
            with f:
                data = self.ui.textEdit.toPlainText()                                   #获取textEdit的str
                f.write(data)
                f.close()

    def readFile(self):
        fname = QFileDialog.getOpenFileName(self, "ReadFile", "../", "TXT (*.txt)")
        if fname[0]:
            f = open(fname[0], "r")
            with f:
                data = f.read()
                self.ui.textEdit.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = FileOperation()
    win.show()
    sys.exit(app.exec())