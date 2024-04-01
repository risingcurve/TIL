import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()


# print(sys.argv)
# app = QApplication(sys.argv)
app = QApplication(["qt01.py"])
window = MyWindow()
window.show()
app.exec_()

