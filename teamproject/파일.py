import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, QtGui, uic
import cx_Oracle as oci
import os

# 데이터베이스 설정
DB_CONFIG = {
    "username": "attendance",
    "password": "12345",
    "host": "localhost",
    "port": 1521,
    "sid": "XE"
}

class MypageWindow(QDialog):  
    def __init__(self):  
        super().__init__()
        self.initUI()
        self.setupConnections()

    def initUI(self):
        ui_path = os.path.abspath('./toyproject/마이페이지.ui')
        print(f"UI 파일 로드: {ui_path}")
        uic.loadUi(ui_path, self)
        self.setWindowTitle('마이페이지')
        
        # UI 요소 찾기
        self.btn_std_year = self.findChild(QComboBox, "btn_std_year")
        self.btn_std_month = self.findChild(QComboBox, "btn_std_month")
        self.btn_std_day = self.findChild(QComboBox, "btn_std_day")
        self.btn_std_grade = self.findChild(QComboBox, "btn_std_grade")
        self.btn_std_class = self.findChild(QComboBox, "btn_std_class")
        
        self.tblStudent = self.findChild(QTableWidget, "tblStudent")
        self.btn_add = self.findChild(QPushButton, "btn_add")
        self.btn_mod = self.findChild(QPushButton, "btn_mod")
        self.btn_del = self.findChild(QPushButton, "btn_del")
        
        self.input_std_name = self.findChild(QLineEdit, "input_std_name")
        self.input_std_id = self.findChild(QLineEdit, "input_std_id")
        self.input_std_pwd = self.findChild(QLineEdit, "input_std_pwd")
        self.input_std_mobile = self.findChild(QLineEdit, "input_std_mobile")
        self.input_std_addr = self.findChild(QLineEdit, "input_std_addr")
        
        self.synCombobBox()
        self.insertDefaultData()
        self.show()
    
    def setupConnections(self):
        self.btn_add.clicked.connect(self.btnAddClick)
        self.btn_mod.clicked.connect(self.btnModClick)
        self.btn_del.clicked.connect(self.btnDelClick)
        self.tblStudent.doubleClicked.connect(self.tblstudentDoubleClick)

    def synCombobBox(self):
        self.btn_std_year.addItems([str(i) for i in range(1960, 2026)])
        self.btn_std_month.addItems([str(i) for i in range(1, 13)])
        self.btn_std_day.addItems([str(i) for i in range(1, 32)])
        self.btn_std_grade.addItems(["1", "2", "3"])
        self.btn_std_class.addItems([str(i) for i in range(1, 11)])

    def insertDefaultData(self):
        sample_data = [
            ("홍길동", "12345", "password123", "01012345678", "서울시 강남구"),
            ("김영희", "12346", "password456", "01023456789", "서울시 송파구"),
            ("이철수", "12347", "password789", "01034567890", "서울시 마포구")
        ]
        for data in sample_data:
            self.addData(data)

    def tblstudentDoubleClick(self):
        selected = self.tblStudent.currentRow()
        self.input_std_name.setText(self.tblStudent.item(selected, 0).text())
        self.input_std_id.setText(self.tblStudent.item(selected, 1).text())
        self.input_std_pwd.setText(self.tblStudent.item(selected, 2).text())
        self.input_std_mobile.setText(self.tblStudent.item(selected, 3).text())
        self.input_std_addr.setText(self.tblStudent.item(selected, 4).text())

    def executeQuery(self, query, values=None):
        try:
            connection = oci.connect(**DB_CONFIG)
            cursor = connection.cursor()
            cursor.execute(query, values) if values else cursor.execute(query)
            connection.commit()
            return True
        except Exception as e:
            print(f"DB 오류: {e}")
            return False
        finally:
            cursor.close()
            connection.close()

    def addData(self, values):
        query = "INSERT INTO attendance.students (name, id, password, mobile, address) VALUES (:1, :2, :3, :4, :5)"
        return self.executeQuery(query, values)

    def btnAddClick(self):
        values = (
            self.input_std_name.text(), self.input_std_id.text(), self.input_std_pwd.text(),
            self.input_std_mobile.text(), self.input_std_addr.text()
        )
        if "" in values:
            QMessageBox.warning(self, '입력 오류', '모든 필드를 입력하세요!')
            return
        if self.addData(values):
            QMessageBox.about(self, '저장 성공', '학생 정보 등록 성공!')

    def btnModClick(self):
        values = (
            self.input_std_name.text(), self.input_std_pwd.text(), self.input_std_mobile.text(),
            self.input_std_addr.text(), self.input_std_id.text()
        )
        query = "UPDATE attendance.students SET name=:1, password=:2, mobile=:3, address=:4 WHERE id=:5"
        if self.executeQuery(query, values):
            QMessageBox.about(self, '수정 성공', '학생 정보 수정 성공!')

    def btnDelClick(self):
        std_id = self.input_std_id.text()
        std_pwd = self.input_std_pwd.text()
        if not std_id or not std_pwd:
            QMessageBox.warning(self, '입력 오류', 'ID와 비밀번호를 입력하세요!')
            return
        query = "DELETE FROM attendance.students WHERE id=:1 AND password=:2"
        if self.executeQuery(query, (std_id, std_pwd)):
            QMessageBox.about(self, '삭제 성공', '학생 정보 삭제 성공!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MypageWindow()
    app.exec_()