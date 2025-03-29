class StudentDatabaseApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.createDatabase()

    def initUI(self):
        layout = QVBoxLayout()

        # 검색 입력 필드
        self.search_label = QLabel("학생 검색")
        layout.addWidget(self.search_label)

        self.search_input = QLineEdit()
        layout.addWidget(self.search_input)

        # 검색 버튼
        self.search_button = QPushButton("검색")
        self.search_button.clicked.connect(self.searchStudent)
        layout.addWidget(self.search_button)

        # 전체 보기 버튼
        self.view_all_button = QPushButton("전체보기")
        self.view_all_button.clicked.connect(self.loadAllStudents)
        layout.addWidget(self.view_all_button)

        # 테이블 위젯
        self.table = QTableWidget()
        self.table.setColumnCount(5)  # 예제: 이름, ID, 전화번호, 주소, 학번
        self.table.setHorizontalHeaderLabels(["이름", "ID", "전화번호", "주소", "학번"])
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.setWindowTitle("학생 정보 검색")

    def createDatabase(self):
        """SQLite 데이터베이스 생성 및 기본 데이터 추가"""
        self.conn = sqlite3.connect("students.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                phone TEXT,
                address TEXT,
                student_id TEXT
            )
        ''')

        # 샘플 데이터 추가 (이미 있으면 추가 안 함)
        self.cursor.execute("SELECT COUNT(*) FROM students")
        if self.cursor.fetchone()[0] == 0:
            sample_data = [
                ("김철수", "010-1234-5678", "서울", "2023001"),
                ("이영희", "010-9876-5432", "부산", "2023002"),
                ("박민수", "010-5678-1234", "대구", "2023003"),
            ]
            self.cursor.executemany("INSERT INTO students (name, phone, address, student_id) VALUES (?, ?, ?, ?)", sample_data)
            self.conn.commit()

    def searchStudent(self):
        """이름을 입력하고 검색 버튼을 눌렀을 때 해당 학생 정보 표시"""
        name = self.search_input.text()
        query = "SELECT name, id, phone, address, student_id FROM students WHERE name = ?"
        self.cursor.execute(query, (name,))
        result = self.cursor.fetchall()

        self.table.setRowCount(0)

        for row_num, row_data in enumerate(result):
            self.table.insertRow(row_num)
            for col_num, data in enumerate(row_data):
                self.table.setItem(row_num, col_num, QTableWidgetItem(str(data)))

    def loadAllStudents(self):
        """전체 학생 목록을 테이블에 표시"""
        query = "SELECT name, id, phone, address, student_id FROM students"
        self.cursor.execute(query)
        result = self.cursor.fetchall()

        self.table.setRowCount(0)

        for row_num, row_data in enumerate(result):
            self.table.insertRow(row_num)
            for col_num, data in enumerate(row_data):
                self.table.setItem(row_num, col_num, QTableWidgetItem(str(data)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StudentDatabaseApp()
    window.show()
    sys.exit(app.exec_())