import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * # 아이콘 넣기

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__() # 부모 클래스인 QMainWindow 클래스에서 생성자 함수 호출
        self.setGeometry(300, 300, 400, 400) # 윈도우 크기 변경
        self.setWindowIcon(QIcon("pie-chart.png")) # 아이콘 넣기
        self.setWindowTitle("My HTS v1.0") # 윈도우 타이틀 변경


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()

