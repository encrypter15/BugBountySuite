# ai_config_dialog.py—GUI for setting up AI providers
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
import json
import os

CONFIG_FILE = "data/ai_config.json"

class AIConfigDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Configure AI Providers")
        self.layout = QVBoxLayout(self)
        
        # Load existing config—fill those fields!
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r") as f:
                self.config = json.load(f)
        else:
            self.config = {
                "Gemini": {"api_key": "", "endpoint": "https://api.gemini.com/v1/analyze"},
                "xAI": {"api_key": "", "endpoint": "https://api.x.ai/v1/completions"},
                "ChatGPT": {"api_key": "", "endpoint": "https://api.openai.com/v1/chat/completions"}
            }
        
        self.entries = {}
        for provider, details in self.config.items():
            label = QLabel(f"{provider} API Key:")
            entry = QLineEdit(details["api_key"])
            self.entries[provider] = entry
            self.layout.addWidget(label)
            self.layout.addWidget(entry)
        
        self.save_btn = QPushButton("Save")
        self.save_btn.clicked.connect(self.save_config)
        self.layout.addWidget(self.save_btn)

    def save_config(self):
        # Save those keys—don’t fuck it up!
        for provider, entry in self.entries.items():
            self.config[provider]["api_key"] = entry.text()
        with open(CONFIG_FILE, "w") as f:
            json.dump(self.config, f, indent=4)
        self.accept()
