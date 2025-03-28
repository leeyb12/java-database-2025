import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import cx_Oracle as oci

# Oracle DB 연결 설정
sid = 'XE'
host = 'localhost'
port = 1521
username = 'attendance'
password = '12345'
basic_msg = '출결관리앱'

class MypageWindow(QDialog):
    def __init__(self):
        super(MypageWindow, self).__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('./toyproject/마이페이지.ui', self)

        # UI 요소 가져오기
        self.tblStudent = self.findChild(QTableWidget, "tblStudent")

        # 버튼 찾기 (버튼이 정상적으로 할당되지 않으면 오류 발생 가능)
        self.btn_add = self.findChild(QPushButton, "btn_add")
        self.btn_mod = self.findChild(QPushButton, "btn_mod")
        self.btn_del = self.findChild(QPushButton, "btn_del")
        self.btn_search = self.findChild(QPushButton, "btn_search")
        self.btn_all = self.findChild(QPushButton, "btn_all")

        # 디버깅 출력
        print(f"🔍 btn_add: {self.btn_add}")
        print(f"🔍 btn_mod: {self.btn_mod}")
        print(f"🔍 btn_del: {self.btn_del}")
        print(f"🔍 btn_search: {self.btn_search}")
        print(f"🔍 btn_all: {self.btn_all}")

        # 버튼 이벤트 연결 (None 체크 추가)
        if self.btn_add:
            self.btn_add.clicked.connect(self.btnAddClick)
        if self.btn_mod:
            self.btn_mod.clicked.connect(self.btnModClick)
        if self.btn_del:
            self.btn_del.clicked.connect(self.btnDelClick)
        if self.btn_search:
            self.btn_search.clicked.connect(self.btnSrhClick)
        if self.btn_all:
            self.btn_all.clicked.connect(self.btnAllClick)

        # 콤보박스 설정
        self.synComboBox()
        self.insertDefaultData()

        self.show()

    def synComboBox(self):
        """ UI에서 QComboBox 찾기 및 데이터 추가 """
        self.btn_std_year = self.findChild(QComboBox, "std_year_comboBox") 
        self.btn_std_month = self.findChild(QComboBox, "btn_std_month")
        self.btn_std_day = self.findChild(QComboBox, "btn_std_day")
        self.btn_std_grade = self.findChild(QComboBox, "btn_std_grade")
        self.btn_std_class = self.findChild(QComboBox, "btn_std_class")

        # 콤보박스가 None이면 오류 출력
        if not self.btn_std_year:
            print("⚠️ std_year_comboBox 를 찾을 수 없습니다!")
        else:
            self.btn_std_year.addItems([str(i) for i in range(1960, 2026)])

        if self.btn_std_month:
            self.btn_std_month.addItems([str(i) for i in range(1, 13)])
        if self.btn_std_day:
            self.btn_std_day.addItems([str(i) for i in range(1, 32)])
        if self.btn_std_grade:
            self.btn_std_grade.addItems(["1", "2", "3"])
        if self.btn_std_class:
            self.btn_std_class.addItems([str(i) for i in range(1, 11)])

    def btnAddClick(self):
        """ 학생 정보 추가 """
        std_name = self.findChild(QLineEdit, "input_std_name").text()
        std_id = self.findChild(QLineEdit, "input_std_id").text()
        std_pwd = self.findChild(QLineEdit, "input_std_pwd").text()
        std_mobile = self.findChild(QLineEdit, "input_std_mobile").text()
        std_addr = self.findChild(QLineEdit, "input_std_addr").text()

        if not all([std_name, std_id, std_pwd, std_mobile, std_addr]):
            QMessageBox.warning(self, '경고', '필수 정보를 입력해주세요!')
            return

        values = (std_name, std_id, std_pwd, std_mobile, std_addr)
        if self.addData(values):
            QMessageBox.about(self, '저장 성공', '학생 정보 등록 성공!')
        else:
            QMessageBox.about(self, '저장 실패', '관리자에게 문의하세요.')

    def addData(self, values):
        """ 데이터베이스에 학생 추가 """
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
            print(f"❌ Error occurred: {e}")
            return False
        finally:
            if cursor: cursor.close()
            if connection: connection.close()

    def btnSrhClick(self):
        """ 학생 검색 """
        std_name = self.findChild(QLineEdit, "input_std_name").text().strip()
        if not std_name:
            QMessageBox.warning(self, "경고", "학생 이름을 입력해주세요!")
            return

        try:
            connection = oci.connect(username, password, f"{host}:{port}/{sid}")
            cursor = connection.cursor()

            query = """SELECT name, id, password, mobile, address FROM attendance.students WHERE name = :1"""
            cursor.execute(query, (std_name,))
            students = cursor.fetchall()

            if students:
                self.tblStudent.setRowCount(len(students))
                for i, student in enumerate(students):
                    for j, data in enumerate(student):
                        self.tblStudent.setItem(i, j, QTableWidgetItem(str(data)))
            else:
                QMessageBox.information(self, "검색 결과", "해당 이름의 학생을 찾을 수 없습니다.")
                self.tblStudent.setRowCount(0)

        except Exception as e:
            print(f"❌ Error occurred: {e}")
            QMessageBox.warning(self, "오류", "데이터 검색 중 오류가 발생했습니다.")
        finally:
            if cursor: cursor.close()
            if connection: connection.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MypageWindow()
    win.show()
    app.exec_()
