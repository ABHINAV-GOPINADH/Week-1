from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit,
    QPushButton, QLabel, QListWidget, QMessageBox
)
import sys

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def __str__(self):
        return f"{self.student_id} - {self.name}"

class StudentManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")
        self.setFixedSize(400, 500)

        self.students = []  # Stores Student objects

        # Layout
        self.layout = QVBoxLayout()

        # Input fields
        self.id_input = QLineEdit()
        self.id_input.setPlaceholderText("Student ID")
        self.layout.addWidget(self.id_input)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Student Name")
        self.layout.addWidget(self.name_input)

        # Buttons
        self.add_button = QPushButton("Add Student")
        self.add_button.clicked.connect(self.add_student)
        self.layout.addWidget(self.add_button)

        self.remove_button = QPushButton("Remove Selected Student")
        self.remove_button.clicked.connect(self.remove_student)
        self.layout.addWidget(self.remove_button)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search by name or ID")
        self.layout.addWidget(self.search_input)

        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.search_student)
        self.layout.addWidget(self.search_button)

        # Student list
        self.list_widget = QListWidget()
        self.layout.addWidget(self.list_widget)

        self.setLayout(self.layout)

    def add_student(self):
        student_id = self.id_input.text().strip()
        name = self.name_input.text().strip()

        if not student_id or not name:
            QMessageBox.warning(self, "Input Error", "Both ID and name are required.")
            return

        student = Student(student_id, name)
        self.students.append(student)
        self.update_list()
        self.id_input.clear()
        self.name_input.clear()

    def remove_student(self):
        selected_items = self.list_widget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "No Selection", "Select a student to remove.")
            return

        for item in selected_items:
            text = item.text()
            self.students = [s for s in self.students if str(s) != text]
        self.update_list()

    def search_student(self):
        query = self.search_input.text().strip().lower()
        results = [str(s) for s in self.students if query in s.name.lower() or query in s.student_id.lower()]

        self.list_widget.clear()
        if results:
            self.list_widget.addItems(results)
        else:
            self.list_widget.addItem("No results found.")

    def update_list(self):
        self.list_widget.clear()
        self.list_widget.addItems([str(s) for s in self.students])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StudentManager()
    window.show()
    sys.exit(app.exec())
