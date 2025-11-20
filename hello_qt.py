import sys
from PySide6.QtWidgets import (
    QApplication, QLabel, QWidget, QPushButton,
    QVBoxLayout, QLineEdit, QDialog, QMessageBox
)

from db import init_db, add_player, get_player, delete_player, search_player

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
        name = self.name_input.text().strip()
        age_text = self.age_input.text().strip()

        if not name:
            QMessageBox.warning(self, "Error", "Please enter a name.")
            return

        if not age_text.isdigit():
            QMessageBox.warning(self, "Error", "Please enter a valid age (number).")
            return

        age = int(age_text)
        add_player(name, age)
        QMessageBox.information(self, "Saved", "Player saved successfully!")
        self.close()

class DeletePlayerDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delete Player")

        layout = QVBoxLayout()

        # نعرض اللاعبين الحاليين
        players = get_player()
        if not players:
            players_text = "No players found."
        else:
            lines = []
            for pid, name, age in players:
                lines.append(f"{pid}: {name} ({age} years)")
            players_text = "\n".join(lines)

        layout.addWidget(QLabel("Existing players (ID: Name (Age))"))
        players_label = QLabel(players_text)
        players_label.setStyleSheet("font-family: monospace;")
        layout.addWidget(players_label)

        # إدخال الـ ID
        self.id_input = QLineEdit()
        self.id_input.setPlaceholderText("Enter Player ID to delete")
        layout.addWidget(self.id_input)

        delete_btn = QPushButton("Delete")
        delete_btn.clicked.connect(self.delete_player)

        layout.addWidget(delete_btn)

        self.setLayout(layout)

    def delete_player(self):
        player_id_text = self.id_input.text().strip()

        if not player_id_text.isdigit():
            QMessageBox.warning(self, "Error", "Please enter a valid numeric ID.")
            return

        player_id = int(player_id_text)

        # نحاول نمسح اللاعب
        delete_player(player_id)
        QMessageBox.information(self, "Deleted", f"Player with ID {player_id} deleted (if existed).")
        self.close()


class SearchPlayerDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search Player")

        layout = QVBoxLayout()

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Enter name to search")
        layout.addWidget(self.search_input)

        search_btn = QPushButton("Search")
        search_btn.clicked.connect(self.do_search)
        layout.addWidget(search_btn)

        self.results_label = QLabel("")
        self.results_label.setStyleSheet("font-family: monospace;")
        layout.addWidget(self.results_label)

        self.setLayout(layout)

    def do_search(self):
        name = self.search_input.text().strip()

        if not name:
            QMessageBox.warning(self, "Error", "Please enter a name to search.")
            return

        players = search_player(name)

        if not players:
            self.results_label.setText("No matching players found.")
            return

        lines = []
        for pid, pname, age in players:
            lines.append(f"{pid}: {pname} ({age} years)")

        self.results_label.setText("\n".join(lines))



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Player Manager")

        layout = QVBoxLayout()

        add_btn = QPushButton("Create Player")
        add_btn.clicked.connect(self.open_add_dialog)

        delete_btn = QPushButton("Delete Player")
        delete_btn.clicked.connect(self.open_delete_dialog)

        search_btn = QPushButton("Search Player")
        search_btn.clicked.connect(self.open_search_dialog)

        layout.addWidget(add_btn)
        layout.addWidget(delete_btn)
        layout.addWidget(search_btn)
        
        self.setLayout(layout)

    def open_add_dialog(self):
        dialog = AddPlayerDialog()
        dialog.exec()
    
    def open_delete_dialog(self):
        dialog = DeletePlayerDialog()
        dialog.exec()
    
    def open_search_dialog(self):
        dialog = SearchPlayerDialog()
        dialog.exec()


if __name__ == "__main__":
    init_db()  # create table if not exists

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
