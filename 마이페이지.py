import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5 import QtWidgets, QtGui, uic

import cx_Oracle as oci

sid ='XE'
host = 'localhost'
port = 1521 
username = 'attendance'
password = '12345'
basic_msg = 'mypage'

class MainWindow(QMainWindow):  
    def initUI(self):
        uic.loadUi('./toyproject/mypage.ui', self)
        self.setWindowTitle('마이페이지')


        self.statusbar.showMessage(basic_msg)

        self.btn_add.clicked.connect(self.btnAddClick)
        self.btn_mod.clicked.connect(self.btnModClick)
        self.btn_del.clicked.connect(self.btnDelClick)
        self.btn_end.clicked.connect(self.btnEndClick)
    
        self.tb_student.doubleClicked.connect(self.tb_studentDoubleClick)
        self.show()
    
    def clearInput(self):
        self.input_std_name.clear()
        self.input_std_id.clear()
        self.input_std_pwd.clear()
        self.input_std_mobile.clear()
        self.input_std_no.clear()
        self.input_std_search.clear()

    def tblStudentDoubleClick(self):
        selected = self.tblStudent.currentRow()
        std_name = self.tblStudent.item(selected, 0).text()
        std_id = self.tblStudent.item(selected, 1).text()
        std_pwd = self.tblStudent.item(selected, 2).text()
        std_birth = self.tblStudent.item(selected, 3).text()
        std_mobile = self.tblStudent.item(selected, 4).text()
        std_addr = self.tblStudent.item(selected, 5).text()
        std_class = self.tblStudent.item(selected, 6).text()
        std_grade = self.tblStudent.item(selected, 7).text()
        std_no = self.tblStudent.item(selected, 8).text()

        self.input_std_name.setText(std_name)
        self.input_std_id.setText(std_id)
        self.input_std_pwd.setText(std_pwd)
        self.input_std_birth.setText(std_birth)
        self.input_std_mobile.setText(std_mobile)
        self.input_std_addr.setText(std_addr)
        self.input_std_class.setText(std_class)
        self.input_std_grade.setText(std_grade)
        self.input_std_no.setText(std_no)

        self.statusbar.showMessage(f'{basic_msg} | 수정모드')

    def btnAddClick(self):
        std_name = self.input_std_name.text()
        std_id = self.input_std_id.text()
        std_pwd = self.input_std_pwd.text()
        std_birth = self.input_std_birth.text()
        std_mobile = self.input_std_mobile.text()
        std_addr = self.input_std_addr.text()
        std_classroom = self.input_std_classroom.text()
        if std_name == '' or std_id == '' or std_pwd == '' or std_birth == '' or std_mobile == '' or std_addr == '' or std_classroom == '': 
            QMessageBox.warning(self, '경고', '학생이름, 아이디와 비밀번호를 입력해주세요!')
            return
        else:
            print('DB입력 진행!')
            values = (std_name, std_id, std_pwd, std_birth, std_mobile, std_addr, std_classroom)
            if self.addData(values) == True:
                QMessageBox.about(self, '저장성공', '학생정보 등록 성공!!!')
            else: 
                QMessageBox.about(self, '저장실패', '관리자에게 문의하세요.')

            self.clearInput()

            self.statusbar.showMessage(f'{basic_msg} | 저장완료')
    
    def btnModClick(self):
        std_name = self.input_std_name.text()
        std_id = self.input_std_id.text()
        std_pwd = self.input_std_pwd.text()
        std_mobile = self.input_std_mobile.text()
        std_addr = self.input_std_addr.text()
        std_classroom = self.input_std_classroom.text()

        if std_name == '' or std_id == '' or std_pwd == '' or std_mobile == '' or std_addr == '' or std_classroom == '': 
            QMessageBox.warning(self,'경고','학생이름, 아이디와 비밀번호를 입력해주세요!')
            return
        else:
            print('DB수정 진행')
            values = (std_name, std_id, std_pwd, std_mobile, std_addr, std_classroom)
            if self.modData(values) == True:
                QMessageBox.about(self, '수정성공', '학생정보 수정 성공!!!')
            else: 
                QMessageBox.about(self, '수정실패', '관리자에게 문의하세요.')
        
        
        self.clearInput()

        self.statusbar.showMessage(f'{basic_msg} | 수정완료')
    
    def btnDelClick(self):
        std_id = self.input_std_id.text()
        std_pwd = self.input_std_pwd.text()
        
        if std_id == '' or std_pwd == '':
            QMessageBox.warning(self, '경고', '학생이름을 입력해주세요!')
            return 
        else:
            print('DB삭제 진행!') 
            values = (std_id, std_pwd)
            if self.delData(values) == True:
                QMessageBox.about(self, '삭제성공', '학생정보 삭제 성공!!!')
            else:
                QMessageBox.about(self, '삭제실패', '관리자에게 문의하세요.')
            
            
            self.clearInput()

            self.statusbar.showMessage(f'{basic_msg} | 삭제완료')
    
    def btnEndClick(self): 
        self.statusbar.showMessage(f'{basic_msg} | 종료')

        self.clearInput()
class MainWindow(QMainWindow):  
    def initUI(self):
        uic.loadUi('./toyproject/mypage.ui', self)
        self.setWindowTitle('마이페이지') 
        
    def btnSrhClick(self):
        std_name = self.input_std_name.text()
        std_id = self.input_std_id.text()
        std_pwd = self.input_std_pwd.text()
        std_birth = self.input_std_birth.text()
        std_mobile = self.input_std_mobile.text()
        std_addr = self.input_std_addr.text()
        std_class = self.input_std_class.text()
        std_grade = self.input_std_grade.text()
        std_no = self.input_std_no.text()
        print(std_name, std_id, std_pwd, std_birth, std_mobile, std_addr, std_class, std_grade, std_no)
        
        self.clearInput()
    
    def btnAllClick(self):
        std_name = self.input_std_name.text()
        std_id = self.input_std_id.text()
        std_pwd = self.input_std_pwd.text()
        std_birth = self.input_std_birth.text()
        std_mobile = self.input_std_mobile.text()
        std_addr = self.input_std_addr.text()
        std_class = self.input_std_class.text()
        std_grade = self.input_std_grade.text()
        std_no = self.input_std_no.text()
        print(std_name, std_id, std_pwd, std_birth, std_mobile, std_addr, std_class, std_grade, std_no)
        self.clearInput()

    def makeTable(self, lst_student):
        self.tblStudent.setSelectionMode(QAbstractItemView.SingleSelection) 
        self.tblStudent.setEditTriggers(QAbstractItemView.NoEditTriggers) 
        self.tblStudent.setColumnCount(9)
        self.tblStudent.setRowCount(len(lst_student)) # 커서에 들어있는 데이터 길이만큼 row 생성
        self.tblStudent.setHorizontalHeaderLabels(['이름', 'ID', 'PWD', '생년월일', '전화번호', '주소', '반', '학년', '번호'])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow() 
    win.show()
    app.exec_()