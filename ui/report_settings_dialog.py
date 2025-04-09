# report_settings_dialog.py—GUI report crafting
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton
from core.report_generator import generate_report
from core.database import get_targets, get_vulns_by_target

class ReportSettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Generate Report")
        self.layout = QVBoxLayout(self)
        
        self.target_label = QLabel("Target URL:")
        self.target_combo = QComboBox()
        self.output_label = QLabel("Output File:")
        self.output_input = QLineEdit("report.md")
        self.gen_btn = QPushButton("Generate")
        
        targets = get_targets()
        self.target_combo.addItems([t[1] for t in targets])
        
        self.gen_btn.clicked.connect(self.generate)
        
        self.layout.addWidget(self.target_label)
        self.layout.addWidget(self.target_combo)
        self.layout.addWidget(self.output_label)
        self.layout.addWidget(self.output_input)
        self.layout.addWidget(self.gen_btn)

    def generate(self):
        target_url = self.target_combo.currentText()
        output_file = self.output_input.text()
        vulns = get_vulns_by_target(target_url)
        if target_url and output_file and vulns:
            generate_report(target_url, vulns, output_file)
            self.accept()
