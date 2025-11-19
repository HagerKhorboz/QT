import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QLineEdit, QMessageBox, QHBoxLayout
#important to start app
app = QApplication(sys.argv)
#imp to start the window
window = QWidget ()
window.setWindowTitle("My First app")

createP_button = QPushButton("Create Player")
deleteP_button = QPushButton("Delete Player")

label = QLabel("Hello")
name_input = QLineEdit()
name_input.setPlaceholderText("Name")

age_input = QLineEdit()
age_input.setPlaceholderText("Age")

input_layout = QHBoxLayout()
layout = QVBoxLayout()

layout.addWidget(label)

layout.addLayout(input_layout)

layout.addWidget(createP_button)
layout.addWidget(deleteP_button)

input_layout.addWidget(name_input)
input_layout.addWidget(age_input)



window.setLayout(layout)

window.show()

app.exec()
