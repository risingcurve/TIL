import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.btn = QPushButton("종료", self) # 버튼 생성을 위한 클래스
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.btn_clicked)

    # 버튼이 클릭될 때 호출되는 메서드
    def btn_clicked(self):
        self.close() # 창 닫기
        
'''
# 버튼 크기 조절
btn.resize(100, 30)
'''

app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()