import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtWidgets,uic
import cx_Oracle as oci

sid = 'XE'
host = 'localhost'
port = 1521 
username = 'attendance'
password = '12345'

class MypageWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        uic.loadUi('./toyproject/마이페이지.ui', self)
        self.setWindowTitle('마이페이지')

        self.btn_add = self.findChild(QPushButton, "btn_add")
        self.btn_mod = self.findChild(QPushButton, "btn_mod")
        self.btn_del = self.findChild(QPushButton, "btn_del")
        self.btn_search = self.findChild(QPushButton, "btn_search")
        self.btn_all = self.findChild(QPushButton, "btn_all")

        if self.btn_add:
            self.btn_add.clicked.connect(self.btnAddClick)
        if self.btn_mod:
            self.btn_mod.clicked.connect(self.btnModClick)
        if self.btn_del:
            self.btn_del.clicked.connect(self.btnDelClick)
    

  
        self.std_year = self.findChild(QComboBox, "std_year")
        self.std_month = self.findChild(QComboBox, "std_month")
        self.std_day = self.findChild(QComboBox, "std_day")
        self.std_grade = self.findChild(QComboBox, "std_grade")
        self.std_class = self.findChild(QComboBox, "std_class")
                                                
        self.show()

    def tblstudentDoubleClick(self):
        selected = self.tblstudent.currentRow()
        std_name = self.tblstudent.item(selected, 0).text()
        std_id = self.tblstudent.item(selected, 1).text()
        std_pwd = self.tblstudent.item(selected, 2).text()
        std_mobile = self.tblstudent.item(selected, 3).text()
        std_addr = self.tblstudent.item(selected, 4).text()
        std_no = self.tblstudent.item(selected, 5).text()
        std_search = self.tblstudent.item(selected, 6).text()

        self.std_name.setText(std_name)
        self.std_id.setText(std_id)
        self.std_pwd.setText(std_pwd)
        self.std_mobile.setText(std_mobile)
        self.std_addr.setText(std_addr)
        self.std_no.setText(std_no)
        self.std_search.setText(std_search)
            

    def btnAddClick(self):
        self.std_name = self.findChild(QLineEdit, "std_name")
        self.std_id = self.findChild(QLineEdit, "std_id")
        self.std_pwd = self.findChild(QLineEdit, "std_pwd")
        self.std_mobile = self.findChild(QLineEdit, "std_mobile")
        self.std_addr = self.findChild(QLineEdit, "std_addr")
        self.std_no = self.findChild(QLineEdit, "std_no")

        if not all([self.std_name, self.std_id, self.std_pwd, self.std_mobile, self.std_addr, self.std_no]):
            QMessageBox.warning(self, '경고', '입력 필드가 존재하지 않습니다! (UI 확인 필요)')
            return

        # 입력 값 가져오기
        std_name = self.std_name.text().strip()
        std_id = self.std_id.text().strip()
        std_pwd = self.std_pwd.text().strip()
        std_mobile = self.std_mobile.text().strip()
        std_addr = self.std_addr.text().strip()
        std_no = self.std_no.text().strip()

        # 필수 정보 확인
        if not all([std_name, std_id, std_pwd, std_mobile, std_addr, std_no]):
            QMessageBox.warning(self, '경고', '필수 정보를 입력해주세요!')
            return
        
        values = (std_name, std_id, std_pwd, std_mobile, std_addr, std_no)
        
        # DB 저장 시도
        if self.addData(values):
            QMessageBox.about(self, '저장 성공', '학생 정보 등록 성공!')
        else:
            QMessageBox.about(self, '저장 실패', '관리자에게 문의하세요.')
    
    def btnModClick(self):
        # UI에서 입력 필드 가져오기
        self.std_name = self.findChild(QLineEdit, "std_name")
        self.std_id = self.findChild(QLineEdit, "std_id")
        self.std_pwd = self.findChild(QLineEdit, "std_pwd")
        self.std_mobile = self.findChild(QLineEdit, "std_mobile")
        self.std_addr = self.findChild(QLineEdit, "std_addr")
        self.std_no = self.findChild(QLineEdit, "std_no")

        if not all([self.std_name, self.std_id, self.std_pwd, self.std_mobile, self.std_addr, self.std_no]):
            QMessageBox.warning(self, '경고', '입력 필드가 존재하지 않습니다! (UI 확인 필요)')
            return

        # 입력 값 가져오기
        std_name = self.std_name.text().strip()
        std_id = self.std_id.text().strip()  # 학번 기준으로 수정
        std_pwd = self.std_pwd.text().strip()
        std_mobile = self.std_mobile.text().strip()
        std_addr = self.std_addr.text().strip()
        std_no = self.std_no.text().strip()

        # 필수 정보 확인
        if not all([std_name, std_id, std_pwd, std_mobile, std_addr, std_no]):
            QMessageBox.warning(self, '경고', '필수 정보를 입력해주세요!')
            return
        
        values = (std_name, std_id, std_pwd, std_mobile, std_addr, std_no)
        
        # DB 수정 시도
        if self.modData(values):
            QMessageBox.about(self, '수정 성공', '학생 정보 수정 성공!')
        else:
            QMessageBox.about(self, '수정 실패', '관리자에게 문의하세요.')

    def btnDelClick(self):
        # UI에서 입력 필드 가져오기
        self.std_id = self.findChild(QLineEdit, "std_id")
        self.std_pwd = self.findChild(QLineEdit, "std_pwd")

        if not all([self.std_id, self.std_pwd]):
            QMessageBox.warning(self, '경고', '입력 필드가 존재하지 않습니다! (UI 확인 필요)')
            return

        # 입력 값 가져오기
        std_id = self.std_id.text().strip()
        std_pwd = self.std_pwd.text().strip()

        # 필수 정보 확인
        if not std_id or not std_pwd:
            QMessageBox.warning(self, '경고', '학생 ID와 비밀번호를 입력해주세요!')
            return 

        # 삭제 확인 메시지
        reply = QMessageBox.question(
            self, '삭제 확인', f'학생 ID "{std_id}" 정보를 삭제하시겠습니까?',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            values = (std_id, std_pwd)
            if self.delData(values):
                QMessageBox.about(self, '삭제 성공', '학생 정보 삭제 성공!')
            else:
                QMessageBox.warning(self, '삭제 실패', '학생 정보를 찾을 수 없거나 비밀번호가 틀렸습니다.')

    def btnsrhClick(self):
        self.std_name = self.findChild(QLineEdit, "std_name")
        if not all([self.std_id, self.std_pwd, self.std_mobile, self.std_addr, self.std_no]):
            QMessageBox.warning(self, '경고', '학생 이름을 입력해주세요.')
            return

    def addData(self, values):
        connection= None  
        try:
            connection = oci.connect("attendance/12345@localhost:1521/XE")
            cur = connection.cursor()

            std_id = values[1]  

            cur.execute("SELECT COUNT(*) FROM students WHERE student_id = :1", (std_id,))
            count = cur.fetchone()[0]

            if count > 0:
                print(f" 학생 ID {std_id} 는 이미 존재합니다!")
                QMessageBox.warning(self, "오류", f"학생 ID {std_id} 는 이미 존재합니다!")
                return False  

            sql = """INSERT INTO students (name, student_id, password, mobile, address, student_no)
                    VALUES (:1, :2, :3, :4, :5, :6)"""
            cur.execute(sql, values)
            connection.commit()

            print(f"학생 ID {std_id} 정보 저장 완료!")
            return True

        except oci.DatabaseError as e:
            print("데이터 저장 오류:", e)
            QMessageBox.warning(self, "DB 오류", "학생 정보 저장 중 오류 발생!")
            return False

        finally:
            if connection:
                cur.close()
                connection.close()


    def modData(self, values):
        connection, 
        cursor = None, None
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



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MypageWindow()
    win.show()
    app.exec_()