import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        btn = QPushButton("버튼", self)
        btn.move(20, 20)
        btn.clicked.connect(QApplication.instance().quit)


# 보다 읽기 쉬운 코딩
'''
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        btn = QPushButton("버튼", self)
        btn.move(20, 20)
        btn.clicked.connect(self.btn_clinked)

    def btn_clicked(self):
        QApplication.instanc().quit()
'''

# self.close 메서드 호출
'''
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        btn = QPushButton("버튼", self)
        btn.move(20, 20)
        btn.clicked.connect(self.close)
'''


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()