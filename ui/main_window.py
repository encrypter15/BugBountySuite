# main_window.py—the GUI command center with recon firepower!
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QFileDialog, QTextEdit
from PyQt6.QtCore import Qt
import logging
import asyncio
from core.database import get_targets, get_vulns_by_target
from ui.add_target_dialog import AddTargetDialog
from ui.add_vulnerability_dialog import AddVulnerabilityDialog
from ui.report_settings_dialog import ReportSettingsDialog
from integrations.recon_tools import run_all_recon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hunter’s Hub")
        self.resize(1000, 800)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        
        self.add_target_btn = QPushButton("Add Target")
        self.add_vuln_btn = QPushButton("Add Vulnerability")
        self.import_burp_btn = QPushButton("Import Burp XML")
        self.gen_report_btn = QPushButton("Generate Report")
        self.run_recon_btn = QPushButton("Run Recon Tools")
        
        self.add_target_btn.clicked.connect(self.open_add_target)
        self.add_vuln_btn.clicked.connect(self.open_add_vuln)
        self.import_burp_btn.clicked.connect(self.import_burp)
        self.gen_report_btn.clicked.connect(self.open_report_settings)
        self.run_recon_btn.clicked.connect(self.run_recon)
        
        self.layout.addWidget(self.add_target_btn)
        self.layout.addWidget(self.add_vuln_btn)
        self.layout.addWidget(self.import_burp_btn)
        self.layout.addWidget(self.gen_report_btn)
        self.layout.addWidget(self.run_recon_btn)
        
        self.target_table = QTableWidget()
        self.target_table.setColumnCount(2)
        self.target_table.setHorizontalHeaderLabels(["Program", "URL"])
        self.layout.addWidget(self.target_table)
        
        self.vuln_table = QTableWidget()
        self.vuln_table.setColumnCount(5)
        self.vuln_table.setHorizontalHeaderLabels(["Title", "Severity", "Date", "Status", "Notes"])
        self.layout.addWidget(self.vuln_table)
        
        self.recon_output = QTextEdit()
        self.recon_output.setReadOnly(True)
        self.layout.addWidget(self.recon_output)
        
        self.load_data()

    def load_data(self):
        targets = get_targets()
        self.target_table.setRowCount(len(targets))
        for i, (program, url) in enumerate(targets):
            self.target_table.setItem(i, 0, QTableWidgetItem(program))
            self.target_table.setItem(i, 1, QTableWidgetItem(url))
        
        if targets:
            vulns = get_vulns_by_target(targets[0][1])
            self.vuln_table.setRowCount(len(vulns))
            for i, vuln in enumerate(vulns):
                self.vuln_table.setItem(i, 0, QTableWidgetItem(vuln["title"]))
                self.vuln_table.setItem(i, 1, QTableWidgetItem(vuln["severity"]))
                self.vuln_table.setItem(i, 2, QTableWidgetItem(vuln["date_found"]))
                self.vuln_table.setItem(i, 3, QTableWidgetItem(vuln["status"]))
                self.vuln_table.setItem(i, 4, QTableWidgetItem(vuln["notes"] or ""))

    def open_add_target(self):
        dialog = AddTargetDialog(self)
        if dialog.exec():
            self.load_data()

    def open_add_vuln(self):
        dialog = AddVulnerabilityDialog(self)
        if dialog.exec():
            self.load_data()

    def import_burp(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Import Burp XML", "", "XML Files (*.xml)")
        if file_name:
            from integrations.burpsuite import import_burp_xml
            import_burp_xml(file_name)
            self.load_data()

    def open_report_settings(self):
        dialog = ReportSettingsDialog(self)
        if dialog.exec():
            self.load_data()

    def run_recon(self):
        selected = self.target_table.currentRow()
        if selected >= 0:
            target = self.target_table.item(selected, 1).text()
            self.recon_output.clear()
            self.recon_output.append(f"Running recon on {target}...")
            results = asyncio.run(run_all_recon(target))
            for tool, output in results.items():
                self.recon_output.append(f"\n=== {tool.upper()} ===\n{output}")
            logging.info(f"Recon completed on {target}—check the output, hotshot!")
        else:
            self.recon_output.append("Select a target first, you clever hunter!")
