import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, QtGui, uic

import cx_Oracle as oci

sid = 'XE'
host = 'localhost'
port = 1521
username = 'attendance'
password = '12345'
basic_msg = '학생출석관리'

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
        self.loadData()
        
    
    def initUI(self):
        uic.loadUi('./toyproject/studentannoun.ui', self)
        self.setWindowTitle('출석관리')

        self.statusbar.showMessage(basic_msg)

        self.btn_add.clicked.connect(self.btnAddClick)
        self.btn_mod.clicked.connect(self.btnModClick)
        self.btn_del.clicked.connect(self.btnDelClick)

    def clearInput(self):
        self.input_write.clear()

    def StudentDoubleClick(self):
        selected = self.announment.currentRow()
        write = self.input_write.text()
        record = self.announment.item(selected, 0).text()
        self.input_record.setText(record)

        self.statusbar.showMessage(f'{basic_msg} | 수정모드')

    def btnAddClick(self):
        write = self.input_write.text()
        print(write)

        if write == '': 
           QMessageBox.warning(self, '경고', '글이 작성했는지 확인해주세요.')
        else:
            print('공지사항등록 진행!')
            values = write 
            if self.addData(values) == True:
                QMessageBox.about(self, '등록성공', '공지사항 등록 성공!!!')
            else:
                QMessageBox.about(self, '등록실패', '관리자에게 문의하세요.')
        
        self.loadData()
        self.clearInput()

        self.statusbar.showMessage(f'{basic_msg} | 저장완료')

    def btnModClick(self):
        record = self.input_record.text()

        if record == '':
            QMessageBox.about(self, '수정성공', '공지사항 수정 완료!')
        else:
            QMessageBox.about(self, '수정실패','관리자에게 문의하세요.')
        
        self.loadData()
        self.clearInput()

        self.statusbar.showMessage(f'{basic_msg} | 수정완료')

    def btnDelClick(self):
        record = self.input_record.text()

        if record == '':
            return
        else:
            print('DB삭제 진행!')
            values = (record)
            if self.delData(values) == True:
                QMessageBox.about(self, '삭제성공', '공지사항 삭제 성공!')
            else:
                QMessageBox.about(self, '삭제실패', '관리자에게 문의하세요.')
            
            self.loadData()
            self.clearInput()

            self.statusbar.showMessage(f'{basic_msg} | 삭제완료')
    
    def makeTable(self, lst_announments):
        self.announment.setSelectionMode(QAbstractItemView.SingleSelection)
        self.announment.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.announment.setColumnCount(2)
        self.announment.setRowCount(len(lst_announments))
        self.announment.setHorizontalHeaderLabels(['번호', '공지사항 글'])

        for i, write in enumerate(lst_announments):
            self.announment.setItem(i, 0, QTableWidgetItem(write))

    def loadData(self):
        conn = oci.connect(f'{username}/{password}@{host}:{port}/{sid}')
        cursor = conn.cursor()

        query = '''
                SELECT * FROM STUDENT
                '''
        cursor.execute(query)

        lst_announments = []
        for _, item in enumerate(cursor):
            lst_announments.append(item)

        self.makeTable(lst_announments)

        cursor.close()
        conn.close()
    
    def addData(self, tuples):
        isSucceed = False 
        conn = oci.connect(f'{username}/{password}@{host}:{port}/{sid}')
        cursor = conn.cursor()

        try:
            conn.begin()

            query = '''INSERT INTO WRITE.Teacher 
                       VALUES (WRITE)
                    '''

            cursor.execute(query, tuples)
        
            conn.commit()
            last_id = cursor.lastrowid
            print(last_id)
            isSucceed = True
            
        except Exception as e:
            print(e)
            conn.rollback()
            isSucceed = False
        finally: 
            cursor.close()
            conn.close()

        return isSucceed
    
    def modData(self, tuples):
        isSucceed = False
        conn = oci.connect(f'{username}/{password}@{host}:{port}/{sid}')
        cursor = conn.cursor()

        try: 
            conn.begin()

            query = '''UPDATE WRITE
                          SET RECORD'''
            
            cursor.execute(query, tuples)

            conn.commit()
            isSucceed = True
        except Exception as e:
            print(e)
            conn.rollback()
            isSucceed = False 
        finally:
            cursor.close()
            conn.close()

        return isSucceed
    
    def delData(self, tuples):
        isSucceed = False
        conn = oci.connect(f'{username}/{password}@{host}:{port}/{sid}')
        cursor = conn.cursor()

        try:
            conn.begin()
            
            query = '''
                    DELETE FROM RECORD 
                    '''
            cursor.execute(query, tuples)

            conn.commit()
            isSucceed = True 
        except Exception as e:
            print(e)
            conn.rollback()
            isSucceed = False 
        finally:
            cursor.close()
            conn.close()
        
        return isSucceed


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()