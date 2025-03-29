import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5 import QtGui, QtWidgets, uic

import cx_Oracle as oci

class PersonApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Person Database Viewer")
        self.setGeometry(100, 100, 800, 600)

        self.initUI()

    def initUI(self):
        # 메인 위젯 및 레이아웃 생성
        self.main_widget = QWidget()
        self.layout = QVBoxLayout(self.main_widget)
        self.setCentralWidget(self.main_widget)

        # 테이블 위젯 생성
        self.table_widget = QTableWidget()
        self.layout.addWidget(self.table_widget)

        self.loadData()
        self.table_widget.cellDoubleClicked.connect(self.showDetails)

    def loadData(self):
        # 데이터베이스 연결
        connection = pymysql.connect(
            host="localhost", user="root", password="", database="people"
        )
        cursor = connection.cursor()
        query = "SELECT id, name, age FROM person"
        cursor.execute(query)
        data = cursor.fetchall()

        # 테이블 설정
        self.table_widget.setRowCount(len(data))
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["ID", "Name", "Age"])

        for row_idx, row_data in enumerate(data):
            for col_idx, col_data in enumerate(row_data):
                self.table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

        self.data = data  # 전체 데이터 저장
        connection.close()

    def showDetails(self, row, column):
        person_id = self.table_widget.item(row, 0).text()

        # 데이터베이스에서 추가 정보 가져오기
        connection = oci.connect(
            host="localhost", user="root", password="", database="people"
        )
        cursor = connection.cursor()
        query = f"SELECT * FROM person WHERE id={person_id}"
        cursor.execute(query)
        person = cursor.fetchone()
        connection.close()

        # 상세 정보 팝업 창
        details = f"ID: {person[0]}\nName: {person[1]}\nAge: {person[2]}\nGender: {person[3]}\nCity: {person[4]}"
        QMessageBox.information(self, "Person Details", details)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PersonApp()
    window.show()
    sys.exit(app.exec_())