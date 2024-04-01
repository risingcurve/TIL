import sys
from PyQt5.QtWidgets import *

def buy():
    print("몽땅 매수")

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        btn = QPushButton("버튼", self)
        btn.move(10, 10)
        btn.clicked.connect(buy)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()