import sys
from PySide6.QtWidgets import {QApplication, QLabel, QWidget, QPushButton,
                                QVBoxLayout, QLineEdit, QMessageBox, QHBoxLayout}

from db import init_db, add_player


class AddPlayerDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create Player")

        layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter Name")

        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Enter Age")

        save_btn = QPushButton("Save")
        save_btn.clicked.connect(self.save_player)

        layout.addWidget(QLabel("Name:"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Age:"))
        layout.addWidget(self.age_input)
        layout.addWidget(save_btn)

        self.setLayout(layout)

    def save_player(self):
        name = self.name_input.text()
        age = int(self.age_input.text())
        add_player(name, age)
        self.close()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Player Manager")

        layout = QVBoxLayout()

        add_btn = QPushButton("Create Player")
        add_btn.clicked.connect(self.open_add_dialog)

        layout.addWidget(add_btn)

        self.setLayout(layout)

    def open_add_dialog(self):
        dialog = AddPlayerDialog()
        dialog.exec()


if __name__ == "__main__":
    init_db()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

window.setLayout(layout)

window.show()

app.exec()
