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

class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        uic.loadUi('./teamproject/마이페이지.ui', self)
        self.setWindowTitle('마이페이지')

        self.btlstudent = QTableWidget()
    

        


    def loadData(self):
        connection = oci.connect(username, password, f"{host}:{port}/{sid}")
        cursor = connection.cursor()
        query = '''SELECT s.*,s.ROWID FROM ATTENDANCE.STUDENT s'''
        cursor.execute(query)
        data = cursor.fetchall()

        self.btnstudent.setRowCount(len(data))
        self.btnstudent.setColumnCount(len(data[0]))
        self.btnstudent.setHorizontalHeaderLabels(["이름", "ID", "PWD", "생년월일", "전화번호", "주소", "반", "학년", "번호"])
        
        for row_idx, row_data in enumerate(data):
            for col_idx, col_data in enumerate(row_data):
                self.btnstudent.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()