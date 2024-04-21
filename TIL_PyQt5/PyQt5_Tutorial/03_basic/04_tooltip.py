'''
두 개의 PyQt5 위젯에 대한 툴팁을 보여줍니다.
푸시버튼(btn)과 창(MyApp) 위젯에 마우스를 올리면 각각 설정한 텍스트가 툴팁으로 나타납니다.
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 툴팁에 사용될 폰트를 설정합니다. 여기에서는 10px 크기의 'SansSerif' 폰트를 사용합니다.
        # 툴팁을 만들기 위해서는 setToolTip()메서드를 사용해서, 표시될 텍스트를 입력해 줍니다.
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        # 푸시버튼을 하나 만들고, 이 버튼에도 툴팁을 달아줍니다.
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButoon</b> widget')
        # 버튼의 위치와 크기를 설정합니다.
        # sizeHine()메서드는 버튼을 적절한 크기로 설정하도록 도와줍니다.
        btn.move(50, 50)
        btn.resize(btn.sizeHint())

        self.setWindowTitle('Tooltips')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


        