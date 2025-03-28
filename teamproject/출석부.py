import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5 import QtWidgets, QtGui, uic
import cx_Oracle as oci

sid = 'XE'
host = '210.119.14.71'
port = 1521
username = 'attendance'
password = '12345'
basic_msg = 'mypage'

class MainWindow(QDialog):  
    def __init__(self):  
        super().__init__()
        self.initUI()  

    def initUI(self):
        uic.loadUi('./teamproject/마이페이지.ui', self)
        self.setWindowTitle('마이페이지')
        self.synComboBox()
        self.insertDefaultData()

        self.btn_add.clicked.connect(self.btnAddClick)
        self.btn_mod.clicked.connect(self.btnModClick)
        self.btn_del.clicked.connect(self.btnDelClick)
        self.btn_search.clicked.connect(self.btnSrhClick)
        self.btn_all.clicked.connect(self.btnAllClick)

        self.btn_std_year.currentIndexChanged.connect(self.btnYearClick)
        self.btn_std_month.currentIndexChanged.connect(self.btnMonthClick)
        self.btn_std_day.currentIndexChanged.connect(self.btnDayClick)
        self.btn_std_grade.currentIndexChanged.connect(self.btnGradeClick)
        
        # 테이블 위젯 UI에서 가져오기
        self.tblStudent = self.findChild(QTableWidget, "tblStudent")
        self.tblStudent.cellDoubleClicked.connect(self.loadStudentInfo)

        self.show()

    def synComboBox(self):  # 기존: synCombobBox (오타 수정)
        self.btn_std_year.addItems([str(i) for i in range(1960, 2026)])
        self.btn_std_month.addItems([str(i) for i in range(1, 13)])
        self.btn_std_day.addItems([str(i) for i in range(1, 32)])
        self.btn_std_grade.addItems(["1", "2", "3"])
        self.btn_std_class.addItems([str(i) for i in range(1, 11)])

        # UI에서 위젯 찾기
        self.input_std_name = self.findChild(QLineEdit, "input_std_name")
        self.input_std_id = self.findChild(QLineEdit, "input_std_id")
        self.input_std_pwd = self.findChild(QLineEdit, "input_std_pwd")
        self.input_std_mobile = self.findChild(QLineEdit, "input_std_mobile")
        self.input_std_addr = self.findChild(QLineEdit, "input_std_addr")
        self.input_std_grade = self.findChild(QComboBox, "input_std_grade")
        self.input_std_class = self.findChild(QComboBox, "input_std_class")

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

    def btnSrhClick(self):
    
        std_name = self.input_std_name.text().strip()

        if not std_name:
            QMessageBox.warning(self, "경고", "학생 이름을 입력해주세요!")
            return

        connection, cursor = None, None
        try:
            connection = oci.connect(username, password, f"{host}:{port}/{sid}")
            cursor = connection.cursor()

            query = """SELECT name, id, password, mobile, address, class_no, grade_no 
                    FROM attendance.students WHERE name = :1"""
            cursor.execute(query, (std_name,))
            students = cursor.fetchall()

            if students:
                self.tblStudent.setRowCount(len(students))  # 테이블 행 개수 설정
                for i, student in enumerate(students):
                    for j, data in enumerate(student):
                        self.tblStudent.setItem(i, j, QTableWidgetItem(str(data)))

                # 첫 번째 학생 정보 자동 입력
                self.loadStudentInfo(0, 0)

            else:
                QMessageBox.information(self, "검색 결과", "해당 이름의 학생을 찾을 수 없습니다.")
                self.tblStudent.setRowCount(0)  # 테이블 초기화

        except Exception as e:
            print(f"Error occurred: {e}")
            QMessageBox.warning(self, "오류", "데이터 검색 중 오류가 발생했습니다.")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()


    def btnAllClick(self):
        self.btnSrhClick()

    def comboBoxFunction(self):
        index = self.mypage.currentIndex()
        print(f"Selected Index: {index}")

    def btnYearClick(self):
        std_year = self.btn_std_year.currentText()  
        print(f"Year selected: {std_year}")

    def btnMonthClick(self):
        std_month = self.btn_std_month.currentText()
        print(f"Month selected: {std_month}")
    
    def btnDayClick(self):
        std_day = self.btn_std_day.currentText()
        print(f"Day selected: {std_day}")
        
    def btnGradeClick(self):
        std_grade = self.btn_std_grade.currentText()
        print(f"Grade selected: {std_grade}")
        

    def clearComboBoxItem(self):
        self.btn_std_year.setCurrentIndex(0)
        self.btn_std_month.setCurrentIndex(0)
        self.btn_std_day.setCurrentIndex(0)
        self.btn_std_grade.setCurrentIndex(0)

    def insertDefaultData(self):
        default_data = []

        for data in default_data:
            if self.addData(data):
                print(f"{data[0]} 학생 정보 추가 성공!")
            else:
                print(f"{data[0]} 학생 정보 추가 실패!")

    def makeTable(self, lst_student):
        self.tblStudent.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblStudent.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tblStudent.setColumnCount(8)
        self.tblStudent.setHorizontalHeaderLabels(['이름', 'ID', 'PWD','생년월일', '전화번호', '주소', '반', '학년'])

        for i, row in enumerate(lst_student):
            for j, val in enumerate(row):
                self.tblStudent.setItem(i, j, QTableWidgetItem(str(val)))
    
   
     
    def addData(self, values):
        connection, cursor = None, None
        try:
            connection = oci.connect(username, password, f"{host}:{port}/{sid}")
            cursor = connection.cursor()
            
            query = '''INSERT INTO attendance.students (name, id, password, mobile, address)
                       VALUES (:1, :2, :3, :4, :5)
                    '''
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
            query = "UPDATE students SET name = :1, password = :2, mobile = :3 WHERE id = :4"
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
            query = "DELETE FROM students WHERE id = :1 AND password = :2"
            cursor.execute(query, values)
            connection.commit()
            return True
        except oci.DatabaseError as e:
            error, = e.args
            QMessageBox.warning(self, 'DB 오류', f"데이터베이스 오류 발생: {error.message}")
            return False
        finally:
           if cursor:
              cursor.close()
           if connection:
              connection.close()
    def loadSdata():
        dsn = oci.makedsn(host, port, sid)
        connection = oci.connect(username, password, dsn)
        cursor = connection.cursor()
        query = '''SELECT S_NO, S_ID, S_PW, S_NAME, S_BIRTH, S_TEL, S_ADDR, CLASS_NO FROM ATTENDANCE.STUDENT'''
        cursor.execute(query)
        lst_student = [item for item in cursor]  
        cursor.close()
        connection.close()
        return lst_student

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()