import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox, QTableWidget, QTableWidgetItem, QMessageBox

class StudentManagementApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("학생 관리 시스템")
        self.setGeometry(100, 100, 600, 500)

        # 학생 데이터 리스트
        self.students = []

        # UI 요소 생성
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # 입력 필드
        form_layout = QHBoxLayout()
        
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("이름")
        self.id_input = QLineEdit(self)
        self.id_input.setPlaceholderText("ID")
        
        self.grade_combo = QComboBox(self)
        self.grade_combo.addItems(["1", "2", "3"])  # 학년
        
        self.class_combo = QComboBox(self)
        self.class_combo.addItems(["1", "2", "3", "4", "5"])  # 반
        
        self.number_input = QLineEdit(self)
        self.number_input.setPlaceholderText("번호")
        
        self.address_input = QLineEdit(self)
        self.address_input.setPlaceholderText("주소")

        form_layout.addWidget(QLabel("이름:"))
        form_layout.addWidget(self.name_input)
        form_layout.addWidget(QLabel("ID:"))
        form_layout.addWidget(self.id_input)
        form_layout.addWidget(QLabel("학년:"))
        form_layout.addWidget(self.grade_combo)
        form_layout.addWidget(QLabel("반:"))
        form_layout.addWidget(self.class_combo)
        form_layout.addWidget(QLabel("번호:"))
        form_layout.addWidget(self.number_input)
        form_layout.addWidget(QLabel("주소:"))
        form_layout.addWidget(self.address_input)
        
        layout.addLayout(form_layout)

        # 버튼
        button_layout = QHBoxLayout()
        self.add_btn = QPushButton("입력", self)
        self.add_btn.clicked.connect(self.add_student)

        self.update_btn = QPushButton("수정", self)
        self.update_btn.clicked.connect(self.update_student)

        self.delete_btn = QPushButton("삭제", self)
        self.delete_btn.clicked.connect(self.delete_student)

        button_layout.addWidget(self.add_btn)
        button_layout.addWidget(self.update_btn)
        button_layout.addWidget(self.delete_btn)

        layout.addLayout(button_layout)

        # 학생 목록 테이블
        self.table = QTableWidget(self)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["이름", "ID", "학년", "반", "번호", "주소"])
        self.table.cellClicked.connect(self.load_selected_row)
        layout.addWidget(self.table)

        # 검색 필드
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("검색할 학생 이름 입력")

        self.search_btn = QPushButton("검색", self)
        self.search_btn.clicked.connect(self.search_student)

        self.show_all_btn = QPushButton("전체보기", self)
        self.show_all_btn.clicked.connect(self.show_all_students)

        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_btn)
        search_layout.addWidget(self.show_all_btn)

        layout.addLayout(search_layout)

        self.setLayout(layout)

    def add_student(self):
        name = self.name_input.text()
        student_id = self.id_input.text()
        grade = self.grade_combo.currentText()
        class_num = self.class_combo.currentText()
        number = self.number_input.text()
        address = self.address_input.text()

        if name and student_id and number:
            self.students.append([name, student_id, grade, class_num, number, address])
            self.update_table()
            self.clear_inputs()
        else:
            QMessageBox.warning(self, "입력 오류", "이름, ID, 번호는 필수 입력 사항입니다.")

    def update_student(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "수정 오류", "수정할 학생을 선택하세요.")
            return

        self.students[selected_row] = [
            self.name_input.text(),
            self.id_input.text(),
            self.grade_combo.currentText(),
            self.class_combo.currentText(),
            self.number_input.text(),
            self.address_input.text()
        ]

        self.update_table()
        self.clear_inputs()

    def delete_student(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "삭제 오류", "삭제할 학생을 선택하세요.")
            return

        del self.students[selected_row]
        self.update_table()
        self.clear_inputs()

    def search_student(self):
        search_name = self.search_input.text().strip()
        if not search_name:
            QMessageBox.warning(self, "검색 오류", "검색할 이름을 입력하세요.")
            return

        filtered_students = [s for s in self.students if search_name in s[0]]
        self.update_table(filtered_students)

    def show_all_students(self):
        self.update_table()

    def update_table(self, data=None):
        if data is None:
            data = self.students

        self.table.setRowCount(len(data))
        for row, student in enumerate(data):
            for col, value in enumerate(student):
                self.table.setItem(row, col, QTableWidgetItem(value))

    def load_selected_row(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            return

        student = self.students[selected_row]
        self.name_input.setText(student[0])
        self.id_input.setText(student[1])
        self.grade_combo.setCurrentText(student[2])
        self.class_combo.setCurrentText(student[3])
        self.number_input.setText(student[4])
        self.address_input.setText(student[5])

    def clear_inputs(self):
        self.name_input.clear()
        self.id_input.clear()
        self.number_input.clear()
        self.address_input.clear()
        self.grade_combo.setCurrentIndex(0)
        self.class_combo.setCurrentIndex(0)
        self.table.clearSelection()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StudentManagementApp()
    window.show()
    sys.exit(app.exec_())
