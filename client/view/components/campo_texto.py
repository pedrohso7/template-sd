from PyQt6.QtWidgets import QLineEdit

class CampoTextoCustomizado(QLineEdit):
    def __init__(self, placeholder, senha=False):
        super().__init__()
        self.setPlaceholderText(placeholder)
        if senha:
            self.setEchoMode(QLineEdit.EchoMode.Password)
        
        self.setStyleSheet("""
            QLineEdit {
                border: 2px solid #bdc3c7;
                border-radius: 5px;
                padding: 8px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 2px solid #3498db;
            }
        """)
