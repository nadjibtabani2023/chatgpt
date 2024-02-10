import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont
import requests
import qdarkstyle

class GPTClient(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GPT API Client")

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Setting custom font for labels, buttons, and text edit
        font = QFont("Arial", 12)  # Example of using Arial font with size 12
        self.ask_label = QLabel("Enter the value for 'ask':")
        self.ask_label.setFont(font)
        self.ask_entry = QLineEdit()
        self.ask_entry.setFont(font)
        self.send_button = QPushButton("Send Request")
        self.send_button.setFont(font)
        self.send_button.clicked.connect(self.get_response)

        self.response_text = QTextEdit()
        self.response_text.setFont(font)
        self.response_text.setReadOnly(True)

        copy_button_layout = QHBoxLayout()
        self.copy_button = QPushButton("Copy Response")
        self.copy_button.setFont(font)
        self.copy_button.clicked.connect(self.copy_response)

        copy_button_layout.addWidget(self.copy_button)

        layout.addWidget(self.ask_label)
        layout.addWidget(self.ask_entry)
        layout.addWidget(self.send_button)
        layout.addWidget(self.response_text)
        layout.addLayout(copy_button_layout)

        self.setLayout(layout)

    def get_response(self):
        ask_input = self.ask_entry.text()
        url = "http://62.72.6.182:6699/gpt"
        params = {"ask": ask_input}
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cache-Control": "max-age=0",
            "Upgrade-Insecure-Requests": "1"
        }
        response = requests.get(url, headers=headers, params=params)
        self.response_text.setText(response.text)

    def copy_response(self):
        response_text = self.response_text.toPlainText()
        QApplication.clipboard().setText(response_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    window = GPTClient()
    window.show()
    sys.exit(app.exec_())
