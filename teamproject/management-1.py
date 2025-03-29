import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import cx_Oracle as oci

# 데이터베이스 연결 정보
sid = 'XE'  
host = '210.119.14.71'  
port = 1521  
username = 'attendance' 
password = '12345'  

class MypageWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        uic.loadUi('./teamproject/마이페이지.ui', self)  # UI 파일 로드
        self.setWindowTitle('마이페이지')
        
        # UI에서 위젯 가져오기
        self.btlstudent = self.findChild(QTableWidget, "btlstudent")  # QTableWidget
        self.input_std_name = self.findChild(QLineEdit, "input_std_name")  # 검색 입력 필드
        self.btn_search = self.findChild(QPushButton, "btn_search")  # 검색 버튼

        # 검색 버튼 클릭 이벤트 연결
        self.btn_search.clicked.connect(self.btnSearchClick)

    def btnSearchClick(self):
        std_name = self.input_std_name.text().strip()
        if not std_name:
            QMessageBox.warning(self, "검색 오류", "검색할 이름을 입력하세요.")
            return

        print(f"Searching for student: {std_name}")

        try:
            connection = oci.connect(username, password, f"{host}:{port}/{sid}")
            cursor = connection.cursor()

            # 이름 검색 쿼리 실행
            query = """SELECT s_name, s_id, s_pw, s_birth, s_tel, s_addr, class_no, s_no 
                       FROM student 
                       WHERE s_name LIKE :s_name"""
            cursor.execute(query, {"s_name": f"%{std_name}%"})
            data = cursor.fetchall()

            if not data:
                QMessageBox.information(self, "검색 결과", "해당 이름을 가진 학생이 없습니다.")
                self.btlstudent.setRowCount(0)
                return

            # 결과를 QTableWidget에 표시
            self.btlstudent.setRowCount(len(data))
            self.btlstudent.setColumnCount(len(data[0]))
            self.btlstudent.setHorizontalHeaderLabels(
                ["이름", "ID", "PWD", "생년월일", "전화번호", "주소", "반", "번호"]
            )

            for row_idx, row_data in enumerate(data):
                for col_idx, col_data in enumerate(row_data):
                    self.btlstudent.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

        except oci.DatabaseError as e:
            QMessageBox.critical(self, "데이터베이스 오류", f"오류 내용: {str(e)}")
        finally:
            cursor.close()
            connection.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MypageWindow()
    win.show()
    app.exec_()
