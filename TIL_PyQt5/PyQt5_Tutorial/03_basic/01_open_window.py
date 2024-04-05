## Ex 3-1. 창 띄우기.

# 필요한 모듈들을 불러옵니다. 기본적인 UI 구성요소를 제공하는 위젯 (클래스)들은 PyQt5.QtWidgets 모듈에 포함되어 있습니다.
# QtWidgets 모듈에 포함된 모든 클래스들과 이에 대한 자세한 설명은 QtWidgets 공식 문서에서 확인할 수 있습니다.
import sys
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    # 여기서 self는 MyApp 객체를 말합니다.
    # setWindowTitle() 메서드는 타이틀바에 나타나는 창의 제목을 설정합니다.
    # move() 메서드는 위젯을 스크린의 x=300px, y=300px의 위치로 이동시킵니다.
    # resize() 메서드는 위젯의 크기를 너비 400px, 높이 200px로 조절합니다.
    # show() 메서드는 위젯을 스크린에 보여줍니다.
    def initUI(self):
        self.setWindowTitle('My First Application')
        self.move(300, 300)
        self.resize(400, 200)
        self.show()

# '__name__'은 현재 모듈의 이름이 저장되는 내장 변수입니다.
# 만약 'moduleA.py'라는 코드를 import해서 예제 코드를 수행하면 __name__ 은 'moduleA'가 됩니다. 
# 그렇지 않고 코드를 직접 실행한다면 __name__ 은 __main__ 이 됩니다. 
# 따라서 이 한 줄의 코드를 통해 프로그램이 직접 실행되는지 혹은 모듈을 통해 실행되는지를 확인합니다.
if __name__ == '__main__':
    # 모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성해야 합니다.
    # QApplication 클래스에 대한 자세한 설명은 QApplication 공식 문서에서 확인할 수 있습니다.
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())