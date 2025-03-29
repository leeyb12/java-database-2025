import sys
from PyQt5.QtWidgets import (
    QApplication, QDialog, QLineEdit, QPushButton, 
    QVBoxLayout, QHBoxLayout, QComboBox, QTableWidget, QTableWidgetItem, 
    QMessageBox, QFileDialog
)
from PyQt5 import uic

class StudentManagementWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        uic.loadUi('./teamproject/학생관리.ui', self)  # UI 파일 로드
        self.setWindowTitle('학생 관리 시스템')

        # 버튼 및 기능 연결
        self.btn_add.clicked.connect(self.add_student)
        self.btn_update.clicked.connect(self.update_student)
        self.btn_delete.clicked.connect(self.delete_student)
        self.btn_search.clicked.connect(self.search_student)
        self.btn_show_all.clicked.connect(self.show_all_students)
        self.btn_upload.clicked.connect(self.upload_photo)

        # 학생 데이터 리스트
        self.students = []

        # 테이블 설정
        self.table_students.setColumnCount(7)
        self.table_students.setHorizontalHeaderLabels(["이름", "ID", "생년월일", "전화번호", "주소", "학년", "반"])
        self.table_students.cellClicked.connect(self.load_selected_row)

    def add_student(self):
        name = self.input_name.text()
        student_id = self.input_id.text()
        birthdate = f"{self.combo_year.currentText()}-{self.combo_month.currentText()}-{self.combo_day.currentText()}"
        phone = self.input_phone.text()
        address = self.input_address.text()
        grade = self.combo_grade.currentText()
        class_num = self.combo_class.currentText()

        if name and student_id:
            self.students.append([name, student_id, birthdate, phone, address, grade, class_num])
            self.update_table()
            self.clear_inputs()
        else:
            QMessageBox.warning(self, "입력 오류", "이름과 ID는 필수 입력 사항입니다.")

    def update_student(self):
        selected_row = self.table_students.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "수정 오류", "수정할 학생을 선택하세요.")
            return

        self.students[selected_row] = [
            self.input_name.text(),
            self.input_id.text(),
            f"{self.combo_year.currentText()}-{self.combo_month.currentText()}-{self.combo_day.currentText()}",
            self.input_phone.text(),
            self.input_address.text(),
            self.combo_grade.currentText(),
            self.combo_class.currentText()
        ]

        self.update_table()
        self.clear_inputs()

    def delete_student(self):
        selected_row = self.table_students.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "삭제 오류", "삭제할 학생을 선택하세요.")
            return

        del self.students[selected_row]
        self.update_table()
        self.clear_inputs()

    def search_student(self):
        search_name = self.input_search.text().strip()
        if not search_name:
            QMessageBox.warning(self, "검색 오류", "검색할 이름을 입력하세요.")
            return

        filtered_students = [s for s in self.students if search_name in s[0]]
        self.update_table(filtered_students)

    def show_all_students(self):
        self.update_table()

    def upload_photo(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "사진 선택", "", "Images (*.png *.jpg *.jpeg)")
        if file_name:
            QMessageBox.information(self, "사진 업로드", f"선택한 파일: {file_name}")

    def update_table(self, data=None):
        if data is None:
            data = self.students

        self.table_students.setRowCount(len(data))
        for row, student in enumerate(data):
            for col, value in enumerate(student):
                self.table_students.setItem(row, col, QTableWidgetItem(value))

    def load_selected_row(self):
        selected_row = self.table_students.currentRow()
        if selected_row == -1:
            return

        student = self.students[selected_row]
        self.input_name.setText(student[0])
        self.input_id.setText(student[1])

    def clear_inputs(self):
        self.input_name.clear()
        self.input_id.clear()
        self.input_phone.clear()
        self.input_address.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = StudentManagementWindow()
    win.show()
    app.exec_()
