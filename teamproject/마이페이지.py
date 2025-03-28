import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5 import QtWidgets, QtGui, uic
import cx_Oracle as oci
import os

sid = 'XE'
host = 'localhost'
port = 1521 
username = 'attendance'
password = '12345'
basic_msg = 'mypage'

class MypageWindow(QDialog):  
    def __init__(self):  
        super().__init__()
        self.initUI()
        
    def initUI(self):
        uic.loadUi(os.path.abspath('./toyproject/마이페이지.ui'), self)
        self.setWindowTitle('마이페이지')
        self.synCombobBox()

        # 기본 데이터 삽입
        self.insertDefaultData()

        self.btn_add.clicked.connect(self.btnAddClick)
        self.btn_mod.clicked.connect(self.btnModClick)
        self.btn_del.clicked.connect(self.btnDelClick)

        self.btn_std_year.currentIndexChanged.connect(self.btnYearClick)
        self.btn_std_month.currentIndexChanged.connect(self.btnMonthClick)
        self.btn_std_day.currentIndexChanged.connect(self.btnDayClick)
        self.btn_std_grade.currentIndexChanged.connect(self.btnGradeClick)
        self.btn_std_class.currentIndexChanged.connect(self.btnClassClick)

        self.tblStudent = QTableWidget(self)
        self.tblStudent.setRowCount(10)  
        self.tblStudent.setColumnCount(5)  # 수정: DB 컬럼과 일치하도록 조정
        self.tblStudent.doubleClicked.connect(self.tblstudentDoubleClick)  

        self.show()

    def synCombobBox(self):
        """ 콤보박스 항목 초기화 """
        self.btn_std_year.addItems([str(i) for i in range(1960, 2026)])
        self.btn_std_month.addItems([str(i) for i in range(1, 13)])
        self.btn_std_day.addItems([str(i) for i in range(1, 32)])
        self.btn_std_grade.addItems(["1", "2", "3"])
        self.btn_std_class.addItems([str(i) for i in range(1, 11)])

    def insertDefaultData(self):
        """ 기본 데이터 삽입 """
        default_data = [
            ("홍길동", "12345", "password123", "01012345678", "서울시 강남구"),
            ("김영희", "12346", "password456", "01023456789", "서울시 송파구"),
            ("이철수", "12347", "password789", "01034567890", "서울시 마포구")
        ]

        for data in default_data:
            if self.addData(data):
                print(f"{data[0]} 학생 정보 추가 성공!")
            else:
                print(f"{data[0]} 학생 정보 추가 실패!")

    def clearInput(self):
        self.input_std_name.clear()
        self.input_std_id.clear()
        self.input_std_pwd.clear()
        self.input_std_mobile.clear()
        self.input_std_no.clear()
        self.input_std_search.clear()

    def tblstudentDoubleClick(self):
        selected = self.tblStudent.currentRow()
        std_name = self.tblStudent.item(selected, 0).text()
        std_id = self.tblStudent.item(selected, 1).text()
        std_pwd = self.tblStudent.item(selected, 2).text()
        std_mobile = self.tblStudent.item(selected, 3).text()
        std_addr = self.tblStudent.item(selected, 4).text()

        self.input_std_name.setText(std_name)
        self.input_std_id.setText(std_id)
        self.input_std_pwd.setText(std_pwd)
        self.input_std_mobile.setText(std_mobile)
        self.input_std_addr.setText(std_addr)

    def btnAddClick(self):
        std_name = self.input_std_name.text()
        std_id = self.input_std_id.text()
        std_pwd = self.input_std_pwd.text()
        std_mobile = self.input_std_mobile.text()
        std_addr = self.input_std_addr.text()
        
        if not all([std_name, std_id, std_pwd, std_mobile, std_addr]):
            QMessageBox.warning(self, '경고', '필수 정보를 입력해주세요!')
            return
        
        values = (std_name, std_id, std_pwd, std_mobile, std_addr)
        if self.addData(values):
            QMessageBox.about(self, '저장 성공', '학생 정보 등록 성공!')
        else:
            QMessageBox.about(self, '저장 실패', '관리자에게 문의하세요.')

    def btnModClick(self):
        std_name = self.input_std_name.text()
        std_id = self.input_std_id.text()
        std_pwd = self.input_std_pwd.text()
        std_mobile = self.input_std_mobile.text()
        std_addr = self.input_std_addr.text()
        
        if not all([std_name, std_id, std_pwd, std_mobile, std_addr]):
            QMessageBox.warning(self, '경고', '필수 정보를 입력해주세요!')
            return
        
        values = (std_name, std_pwd, std_mobile, std_addr, std_id)
        if self.modData(values):
            QMessageBox.about(self, '수정 성공', '학생 정보 수정 성공!')
        else:
            QMessageBox.about(self, '수정 실패', '관리자에게 문의하세요.')

    def btnDelClick(self):
        std_id = self.input_std_id.text()
        std_pwd = self.input_std_pwd.text()
        
        if std_id == '' or std_pwd == '':
            QMessageBox.warning(self, '경고', '학생 ID와 비밀번호를 입력해주세요!')
            return 
        else:
            print('DB삭제 진행!') 
            values = (std_id, std_pwd)
            if self.delData(values):
                QMessageBox.about(self, '삭제성공', '학생정보 삭제 성공!!!')
            else:
                QMessageBox.about(self, '삭제실패', '관리자에게 문의하세요.')
            
            self.statusbar.showMessage(f'{basic_msg} | 삭제완료')

    def addData(self, values):
        connection, cursor = None, None
        try:
            connection = oci.connect(username, password, f"{host}:{port}/{sid}")
            cursor = connection.cursor()
            
            query = "INSERT INTO attendance.students (name, id, password, mobile, address) VALUES (:1, :2, :3, :4, :5)"
            cursor.execute(query, values)
            connection.commit()
            return True
        except Exception as e:
            print(f"Error occurred: {e}")
            return False
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def modData(self, values):
        connection, cursor = None, None
        try:
            connection = oci.connect(username, password, f"{host}:{port}/{sid}")
            cursor = connection.cursor()
            query = "UPDATE attendance.students SET name = :1, password = :2, mobile = :3, address = :4 WHERE id = :5"
            cursor.execute(query, values)
            connection.commit()
            return True
        except Exception as e:
            print(f"Error occurred: {e}")
            return False
        finally:
            if cursor: cursor.close()
            if connection: connection.close()

    def delData(self, values):
        connection, cursor = None, None
        try:
            connection = oci.connect(username, password, f"{host}:{port}/{sid}")
            cursor = connection.cursor()
            query = "DELETE FROM attendance.students WHERE id = :1 AND password = :2"
            cursor.execute(query, values)
            connection.commit()
            return True
        except Exception as e:
            print(f"Error occurred: {e}")
            return False
        finally:
           if cursor:
              cursor.close()
           if connection:
              connection.close()

    def makeTable(self, lst_student):
        self.tblStudent.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblStudent.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tblStudent.setRowCount(len(lst_student)) 
        self.tblStudent.setHorizontalHeaderLabels(['이름', 'ID', 'PWD', '전화번호', '주소'])

        for i, row in enumerate(lst_student):
            for j, val in enumerate(row):
                self.tblStudent.setItem(i, j, QTableWidgetItem(str(val)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MypageWindow()
    app.exec_()
