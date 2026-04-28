from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt, pyqtSignal
from view.components.botao import BotaoCustomizado
from view.components.campo_texto import CampoTextoCustomizado

class PaginaLogin(QWidget):
    trocar_para_registro = pyqtSignal()
    requisitar_login = pyqtSignal(str, str)
    
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(15)
        
        self.titulo = QLabel("Login")
        self.titulo.setStyleSheet("font-size: 28px; font-weight: bold; margin-bottom: 20px; color: #2c3e50;")
        layout.addWidget(self.titulo)
        
        self.input_usuario = CampoTextoCustomizado("Usuário")
        layout.addWidget(self.input_usuario)
        
        self.input_senha = CampoTextoCustomizado("Senha", senha=True)
        layout.addWidget(self.input_senha)
        
        self.btn_login = BotaoCustomizado("Entrar")
        self.btn_login.clicked.connect(self.ao_clicar_login)
        layout.addWidget(self.btn_login)
        
        self.btn_ir_registro = BotaoCustomizado("Criar nova conta", cor_fundo="#34495e")
        self.btn_ir_registro.setFlat(True)
        self.btn_ir_registro.clicked.connect(self.trocar_para_registro.emit)
        layout.addWidget(self.btn_ir_registro)
        
        self.setLayout(layout)
        
    def ao_clicar_login(self):
        self.requisitar_login.emit(self.input_usuario.text(), self.input_senha.text())
