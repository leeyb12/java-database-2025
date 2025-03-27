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
basic_msg = '학생관리'

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
        self.loadData()

    def init(self):
        uic.loadUi('./toyproject/studentmanag.ui', self)
        self.setWindowTitle('학생관리')

        self.statusbar.showMessage(basic_msg)


        self.btn_add.clicked.connect(self.btnAddClick)
        self.btn_del.clicked.connect(self.btnDelClick)

    def clearInput(self):
        self.input_std_name.clear()
        self.input_std_reason.clear()
        self.input_std_grade.clear()
        self.input_std_class.clear()
        self.input_std_no.clear()
        

