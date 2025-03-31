import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, QtGui, uic
from PyQt5 import uic
from PyQt5.QtGui import QPixmap  # QPixmap 모듈 추가

# Oracle 데이터베이스 연결을 위한 cx_Oracle 모듈 임포트
import cx_Oracle as oci

# Oracle 데이터베이스 연결 정보 설정
sid = 'XE'  # 데이터베이스 SID
host = '210.119.14.71'  # 데이터베이스 호스트 주소 (외부 접속 시 변경 필요)
port = 1521  # 데이터베이스 포트 번호
username = 'attendance'  # 데이터베이스 사용자 이름
password = '12345'  # 데이터베이스 비밀번호

# 메인 윈도우 클래스 정의
class MainWindow(QMainWindow): 
    def __init__(self):
        super(MainWindow, self).__init__() 
        self.initUI()  # UI 초기화 함수 호출
        self.generated_numbers = set()  # 생성된 숫자를 저장할 집합 초기화

    # UI 초기화 함수
    def initUI(self):
        # UI 파일 로드
        uic.loadUi('./teamproject/loginway.ui', self)
        self.setWindowTitle('학생용 로그인 방식')  # 윈도우 제목 설정
        

         # QLabel 객체 가져오기
        self.atd_num_label = self.findChild(QLabel, 'atd_num')
        self.images_label = self.findChild(QLabel, 'images') 
        self.images_2_label = self.findChild(QLabel, 'images_2') 

        # QLabel에 이미지 설정
        pixmap = QPixmap('images/mypage.png')  # 이미지 파일 경로
        self.images_label.setPixmap(pixmap)  # QLabel에 이미지 설정
        self.images_label.setScaledContents(True)  # 이미지가 QLabel 크기에 맞게 조정되도록 설정

        pixmap = QPixmap('images/atd.png')  # 이미지 파일 경로
        self.images_2_label.setPixmap(pixmap)  # QLabel에 이미지 설정
        self.images_2_label.setScaledContents(True)  # 이미지가 QLabel 크기에 맞게 조정되도록 설정

        # 출결번호 생성 버튼 클릭 시그널 연결
        self.btn_num.clicked.connect(self.btn_numClick)
        self.middle.clicked.connect(self.middleClick)
        self.exit.clicked.connect(self.exitClick)
        self.back.clicked.connect(self.backClick)
        self.my_page.clicked.connect(self.my_pageClick)
        self.btn_atd.clicked.connect(self.btn_atdClick)



    # btn_chk 버튼 클릭 이벤트 처리 함수
    def btn_numClick(self):
        QMessageBox.information(self, '출석 확인', '출석 되었습니다!')
    
    def middleClick(self):
        QMessageBox.information(self, '조퇴 처리','조퇴 처리 되었습니다!')

    def exitClick(self):
        QMessageBox.information(self, '외출', '외출 처리 되었습니다!')  # 메시지 박스 표시
    
    def backClick(self):
        QMessageBox.information(self, '복귀', '복귀 처리 되었습니다!')  # 메시지 박스 표시

    def my_pageClick(self):
        QMessageBox.information(self, '마이페이지', '마이페이지로 이동합니다')  # 메시지 박스 표시

    def btn_atdClick(self):

        QMessageBox.information(self, '출석관리', '출석관리로 이동합니다')  # 메시지 박스 표시


        # 프로그램 실행 진입점
if __name__ == '__main__':
    app = QApplication(sys.argv)  # QApplication 객체 생성
    win = MainWindow()  # MainWindow 객체 생성
    win.show()  # 메인 윈도우 표시
    app.exec_()  # 이벤트 루프 실행