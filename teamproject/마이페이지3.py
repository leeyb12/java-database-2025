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

        self.btn_add.clicked.connect(self.btnAddClick) 
        self.btn_mod.clicked.connect(self.btnModClick)
        self.btn_del.clicked.connect(self.btnDelClick)
        self.btn_search.clicked.connect(self.btnSrhClick)
        self.btn_all.clicked.connect(self.btnAllClick)

    def tbllstudentDoubleClick(self):
        selected = self.tblstudent.currentRow()
        std_name = self.tblstudent.item(selected, 0).text()
        std_id = self.tblstudent.item(selected, 1).text()
        std_pwd = self.tblstudent.item(selected, 2).text()
        std_mobile = self.tblstudent.item(selected, 3).text()
        std_addr = self.tblstudent.item(selected, 4).text()
        std_no = self.tblstudent.item(selected, 5).text()
        
        self.std_name.setText(std_name)
        self.std_id.setText(std_id)
        self.std_pwd.setText(std_pwd)
        self.std_mobile.setText(std_mobile)
        self.std_addr.setText(std_addr)
        self.std_no.setText(std_no)

    def 



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MypageWindow()
    win.show()
    app.exec_()