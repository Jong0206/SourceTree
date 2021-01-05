import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("labelTest.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #버튼에 기능을 할당하는 코드
        self.btn_changeText.clicked.connect(self.changeTextFunction)
        self.btn_printText.clicked.connect(self.printTextFunction)

    def changeTextFunction(self) :
        #self.Label이름.setText("String")
        #Label에 글자를 바꾸는 메서드
        self.lbl_Test.setText("This is Label - Changed Text")

    def printTextFunction(self) :
        #self.Label이름.text()
        #Label에 있는 글자를 가져오는 메서드
        print(self.lbl_Test.text())

# 파일의 내용 되돌리기
# - 특정 파일의 내용을 마지막 커밋으로 돌리고 싶다면 해당 파일 선택 후 '코드 뭉치 버리기' 선택
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()