import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__() # 부모 클래스인 QMainWindow 클래스에서 생성자 함수 호출

print("출력-1")
app = QApplication(sys.argv)

window = MyWindow()
window.show()

app.exec_()
print("출력-3")

