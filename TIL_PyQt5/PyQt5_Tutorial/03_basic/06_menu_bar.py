'''
GUI 어플리케이션에서 메뉴바(menu bar)는 흔하게 사용됩니다.
다양한 명령들의 모음이 메뉴바에 위치합니다. (QMenuBar 공식 문서 참고)

macOS에서는 메뉴바를 다르게 다루는데, 아래 예제에서 볼 수 있듯이 한 줄의 코드(menubar.setNativeMenuBar(False))를 추가함으로써 macOS에서도 Windows 환경과 동일한 결과를 얻을 수 있습니다.

우선 폴더 안에 아래와 같이 메뉴에 해당하는 아이콘(exit.png)을 저장해 둡니다.
'''

# Ex 3-6. 메뉴바 만들기.
# 한 개의 메뉴를 갖는 메뉴바를 만들었습니다.
# 이 메뉴는 클릭했을 때 어플리케이션을 종료하는 기능을 갖고 있습니다. 또한 이 기능은 단축키 (Ctrl+Q)로도 실행이 가능합니다.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon

class MyApp(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 이 세 줄의 코드를 통해 아이콘(exit.png)과 'Exit' 라벨을 갖는 하나의 동작(action)을 만들고, 이 동작에 대해 단축키(shortcut)를 정의합니다.
        # 또한 메뉴에 마우스를 올렸을 때, 상태바에 나타날 상태팁을 setStatusTip() 메서드를 사용하여 설정했습니다.
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')

        # 이 동작을 선택했을 때, 생성된(triggered) 시그널이 QApplictation 위젯의 quit() 메서드에 연결되고, 어플리케이션을 종료시키게 됩니다.
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        # menuBar() 메서드는 메뉴바를 생성합니다. 이어서 'File' 메뉴를 하나 만들고, 거기에 'exitAction' 동작을 추가합니다.
        # '&File'의 앰퍼샌드(ampersand,&)는 간편하게 단축키를 설정하도록 해줍니다.
        # 'F' 앞에 앰퍼샌드가 있으므로 'Alt+F'가 File 메뉴의 단축키가 됩니다. 만약 'i'의 앞에 앰퍼샌드를 넣으면 'Alt+I'가 단축키가 됩니다.
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        self.setWindowTitle('Menubar')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


