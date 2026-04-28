from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import Qt

class BotaoCustomizado(QPushButton):
    def __init__(self, texto, cor_fundo="#2ecc71"):
        super().__init__(texto)
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {cor_fundo};
                color: white;
                border-radius: 5px;
                padding: 10px;
                font-weight: bold;
                font-size: 14px;
            }}
            QPushButton:hover {{
                background-color: #27ae60;
            }}
            QPushButton:pressed {{
                background-color: #1e8449;
            }}
        """)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
