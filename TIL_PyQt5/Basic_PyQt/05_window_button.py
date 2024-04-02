import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__() # 부모 클래스인 QMainWindow 클래스에서 생성자 함수 호출

        btn = QPushButton(text="매수", parent=self)
        btn.move(10, 10)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()

