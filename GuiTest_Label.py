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


# 브랜치 변경하기
# - 브랜치란 :  기존 내용을 유지한 체 새로운 내용을 추가하고 싶을 때 사용한다.
# - 체크아웃 : 특정 브랜치로 돌아가고 싶을 때 사용.
# - 소스트리의 체크아웃 : 브랜치 이름을 더블 클릭하는 것만으로 체크아웃이 가능

# 병합하기 1
# - 헤드 브랜치에 변경사항이 없고
# - 병합 대상 브랜치가 헤드로부터 시작된 경우
# - 아주 쉽게 병합 가능 = Fast-forward

# 병합하기 2
# - 헤드 브랜치에 추가적인 커밋이 생기는 경우
# - 진짜 병합이 필요해 진다.
# - 충돌이 안 나면 좋은데, 충돌이 나도 겁내지 말자

#충돌 해결하기
# - 제일 중요한 점: 겁내지 말아요!


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()