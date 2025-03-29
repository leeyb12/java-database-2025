import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5 import QtGui, QtWidgets, uic

import cx_Oracle as oci

sid = 'XE'  
host = '210.119.14.71'  
port = 1521  
username = 'attendance' 
password = '12345'  
basic_msg = 'OO고등학교 출결관리앱 v1.0'

class MypageWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        uic.loadUi('./teamproject/마이페이지.ui', self)
        self.setWindowTitle('마이페이지')
        

    def loadData(self):
        try:
            connection = oci.connect(username, password, f"{host}:{port}/{sid}")
            cursor = connection.cursor()
            query = """SELECT s_name, s_id, s_pw, s_birth, s_tel, s_addr, class_no, s_no FROM student"""
            cursor.execute(query)
            data = cursor.fetchall()

            self.tblstudent.setRowCount(len(data))
            self.tblstudent.setColumnCount(len(data[0]))
            self.tblstudent.setHorizontalHeaderLabels(
                ["이름", "ID", "PWD", "생년월일", "전화번호", "주소", "반", "번호"]
            )

            for row_idx, row_data in enumerate(data):
                for col_idx, col_data in enumerate(row_data):
                    self.tblstudent.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

        except oci.DatabaseError as e:
            QMessageBox.critical(self, "데이터베이스 오류", f"오류 내용: {str(e)}")
        finally:
            cursor.close()
            connection.close()


    #     self.btn_search.clicked.connect(self.btnSearchClick)

    # def btnSearchClick(self):
    #     std_name = self.std_name.text().strip()
    #     if not std_name:
    #         QMessageBox.warning(self, "검색 오류", "검색할 이름을 입력하세요.")
    #         return  # 들여쓰기 수정
        
    #     print(f"Searching for student: {std_name}")

    #     try:
    #         connection = oci.connect(username, password, f"{host}:{port}/{sid}")
    #         cursor = connection.cursor()

    #         query = """SELECT s_name, s_id, s_pw, s_birth, s_tel, s_addr, class_no, s_no 
    #                    FROM student WHERE s_name LIKE :s_name"""
    #         cursor.execute(query, {"s_name": f"%{std_name}%"})
    #         data = cursor.fetchall()

    #         if not data:
    #             QMessageBox.information(self, "검색 결과", "해당 이름을 가진 학생이 없습니다.")
    #             return  # 데이터가 없을 경우 여기서 종료
            

    #     except oci.DatabaseError as e:
    #         QMessageBox.critical(self, "데이터베이스 오류", f"오류 내용: {str(e)}")

    #     finally:
    #         cursor.close()
    #         connection.close()

    # def loadData(self):
    #     try:
    #         connection = oci.connect(username, password, f"{host}:{port}/{sid}")
    #         cursor = connection.cursor()
    #         query = """SELECT s_name, s_id, s_pw, s_birth, s_tel, s_addr, class_no, s_no FROM student"""
    #         cursor.execute(query)
    #         data = cursor.fetchall()
    #         self.loadTableData(data)

    #     except oci.DatabaseError as e:
    #         QMessageBox.critical(self, "데이터베이스 오류", f"오류 내용: {str(e)}")

        # finally:
        #     cursor.close()
        #     connection.close()

    def loadTableData(self):
        """데이터를 테이블에 로드하는 메서드"""
        self.tlbstudent.setHorizontalHeaderLabels(
            ["이름", "ID", "PWD", "생년월일", "전화번호", "주소", "반", "번호"]
        )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MypageWindow()
    win.show()
    app.exec_()
