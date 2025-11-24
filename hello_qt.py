import sys
from PySide6.QtWidgets import (
    QApplication, QLabel, QWidget, QPushButton,
    QVBoxLayout, QLineEdit, QDialog, QMessageBox, 
    QMainWindow, QTabWidget
)

from db import init_db, add_player, get_player, delete_player, search_player

class PlayersTab(QWidget):
    def __init__(self):
        super().__init__()

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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.setWindowTitle("Player Manager")

        central_widget = QWidget()
        central_layout = QVBoxLayout()

        tabs = QTabWidget()

        self.players_tab = PlayersTab()
        tabs.addTab(self.players_tab, "Players")

        self.matches_tab = QWidget()
        matches_layout = QVBoxLayout()
        matches_layout.addWidget(QLabel("Matches screen – to be implemented"))
        self.matches_tab.setLayout(matches_layout)
        tabs.addTab(self.matches_tab, "Matches")

        self.stats_tab = QWidget()
        stats_layout = QVBoxLayout()
        stats_layout.addWidget(QLabel("Stats & Analyzer – coming soon"))
        self.stats_tab.setLayout(stats_layout)
        tabs.addTab(self.stats_tab, "Stats")

        central_layout.addWidget(tabs)
        central_widget.setLayout(central_layout)

        self.setCentralWidget(central_widget)

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
