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
        uic.loadUi('./teamproject/마이페이지.ui', self)
        self.setWindowTitle('마이페이지')

        # 테이블 위젯이 UI에 존재하는지 확인
        if not hasattr(self, 'btlstudent'):
            QMessageBox.critical(self, "오류", "QTableWidget(btlstudent)이 UI에 없습니다.")
            return

        # 버튼 이벤트 연결
        self.btn_search.clicked.connect(self.btnSearchClick)
        self.btn_insert.clicked.connect(self.btnInsertClick)
        self.btn_update.clicked.connect(self.btnUpdateClick)
        self.btn_delete.clicked.connect(self.btnDeleteClick)
        self.btn_show_all.clicked.connect(self.loadData)

        # 데이터 불러오기
        self.loadData()

    def loadData(self):
        try:
            connection = oci.connect(username, password, f"{host}:{port}/{sid}")
            cursor = connection.cursor()
            
            query = """SELECT s_name, s_id, s_pw, 
                          TO_CHAR(s_birth, 'YYYY-MM-DD') AS s_birth, 
                          s_tel, s_addr, class_no, s_no 
                   FROM student"""
            cursor.execute(query)
            data = cursor.fetchall()
            
            # 테이블 초기화
            self.btlstudent.clearContents()
            self.btlstudent.setRowCount(len(data))
            self.btlstudent.setColumnCount(len(data[0]) if data else 8)
            self.btlstudent.setHorizontalHeaderLabels(["이름", "ID", "PWD", "생년월일", "전화번호", "주소", "반", "번호"])

            for row_idx, row_data in enumerate(data):
                for col_idx, col_data in enumerate(row_data):
                    self.btlstudent.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

        except oci.DatabaseError as e:
            QMessageBox.critical(self, "데이터베이스 오류", f"오류 내용: {str(e)}")
        finally:
            cursor.close()
            connection.close()

    def btnSearchClick(self):
        """입력된 이름으로 학생 검색"""
        std_name = self.input_std_name.text().strip()
        if not std_name:
            QMessageBox.warning(self, "검색 오류", "검색할 이름을 입력하세요.")
            return
        
        try:
            connection = oci.connect(username, password, f"{host}:{port}/{sid}")
            cursor = connection.cursor()

            query = """SELECT s_name, s_id, s_pw, TO_CHAR(s_birth, 'YYYY-MM-DD') AS s_birth, 
                              s_tel, s_addr, class_no, s_no 
                       FROM student
                       WHERE s_name LIKE :s_name"""
            cursor.execute(query, {"s_name": f"%{std_name}%"})
            data = cursor.fetchall()

            if not data:
                QMessageBox.information(self, "검색 결과", "해당 이름을 가진 학생이 없습니다.")
                return
            
            self.loadTableData(data)

        except oci.DatabaseError as e:
            QMessageBox.critical(self, "DB 오류", f"오류 내용: {str(e)}")

        finally:
            cursor.close()
            connection.close()

    def loadTableData(self, data):
        """QTableWidget에 검색된 데이터 로드"""
        self.btlstudent.setRowCount(len(data))
        self.btlstudent.setColumnCount(8)
        self.btlstudent.setHorizontalHeaderLabels(
            ["이름", "ID", "PWD", "생년월일", "전화번호", "주소", "반", "번호"]
        )

        for row_idx, row_data in enumerate(data):
            for col_idx, col_data in enumerate(row_data):
                self.btlstudent.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

    def btnInsertClick(self):
        """학생 정보 추가"""
        name = self.std_name.text().strip()
        std_id = self.std_id.text().strip()
        pwd = self.std_pwd.text().strip()
        birth = f"{self.cmb_year.currentText()}-{self.cmb_month.currentText()}-{self.cmb_day.currentText()}"
        tel = self.std_tel.text().strip()
        addr = self.std_addr.text().strip()
        class_no = self.cmb_class.currentText()
        s_no = self.std_number.text().strip()

        if not (name and std_id and pwd and tel and addr and class_no and s_no):
            QMessageBox.warning(self, "입력 오류", "모든 필드를 입력하세요.")
            return

        try:
            connection = oci.connect(username, password, f"{host}:{port}/{sid}")
            cursor = connection.cursor()

            query = """INSERT INTO student (s_name, s_id, s_pw, s_birth, s_tel, s_addr, class_no, s_no)
                       VALUES (:name, :std_id, :pwd, TO_DATE(:birth, 'YYYY-MM-DD'), :tel, :addr, :class_no, :s_no)"""

            cursor.execute(query, {
                "name": name, "std_id": std_id, "pwd": pwd, "birth": birth,
                "tel": tel, "addr": addr, "class_no": class_no, "s_no": s_no
            })
            connection.commit()
            QMessageBox.information(self, "입력 성공", "학생 정보가 추가되었습니다.")
            self.loadData()  # 데이터 새로고침

        except oci.DatabaseError as e:
            QMessageBox.critical(self, "DB 오류", f"오류 내용: {str(e)}")

        finally:
            cursor.close()
            connection.close()

    def btnUpdateClick(self):
        """학생 정보 수정"""
        selected_row = self.btlstudent.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "수정 오류", "수정할 학생을 선택하세요.")
            return

        std_id = self.btlstudent.item(selected_row, 1).text()
        new_tel = self.std_tel.text().strip()
        new_addr = self.std_addr.text().strip()

        try:
            connection = oci.connect(username, password, f"{host}:{port}/{sid}")
            cursor = connection.cursor()

            query = """UPDATE student SET s_tel = :new_tel, s_addr = :new_addr WHERE s_id = :std_id"""
            cursor.execute(query, {"new_tel": new_tel, "new_addr": new_addr, "std_id": std_id})
            connection.commit()
            QMessageBox.information(self, "수정 성공", "학생 정보가 수정되었습니다.")
            self.loadData()

        except oci.DatabaseError as e:
            QMessageBox.critical(self, "DB 오류", f"오류 내용: {str(e)}")

        finally:
            cursor.close()
            connection.close()

    def btnDeleteClick(self):
        """학생 정보 삭제"""
        selected_row = self.btlstudent.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "삭제 오류", "삭제할 학생을 선택하세요.")
            return

        std_id = self.btlstudent.item(selected_row, 1).text()

        try:
            connection = oci.connect(username, password, f"{host}:{port}/{sid}")
            cursor = connection.cursor()

            query = "DELETE FROM student WHERE s_id = :std_id"
            cursor.execute(query, {"std_id": std_id})
            connection.commit()
            QMessageBox.information(self, "삭제 성공", "학생 정보가 삭제되었습니다.")
            self.loadData()

        except oci.DatabaseError as e:
            QMessageBox.critical(self, "DB 오류", f"오류 내용: {str(e)}")

        finally:
            cursor.close()
            connection.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MypageWindow()
    win.show()
    app.exec_()
