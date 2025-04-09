# add_target_dialog.py—GUI target slamming
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
from core.target_manager import add_target

class AddTargetDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Target")
        self.layout = QVBoxLayout(self)
        
        self.program_label = QLabel("Program:")
        self.program_input = QLineEdit()
        self.url_label = QLabel("URL:")
        self.url_input = QLineEdit()
        self.add_btn = QPushButton("Add")
        
        self.add_btn.clicked.connect(self.add_target)
        
        self.layout.addWidget(self.program_label)
        self.layout.addWidget(self.program_input)
        self.layout.addWidget(self.url_label)
        self.layout.addWidget(self.url_input)
        self.layout.addWidget(self.add_btn)

    def add_target(self):
        program = self.program_input.text()
        url = self.url_input.text()
        if program and url:
            add_target(program, url)
            self.accept()
