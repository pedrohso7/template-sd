from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt, pyqtSignal
from view.components.botao import BotaoCustomizado
from view.components.campo_texto import CampoTextoCustomizado

class PaginaRegistro(QWidget):
    trocar_para_login = pyqtSignal()
    requisitar_registro = pyqtSignal(str, str)
    
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(15)
        
        self.titulo = QLabel("Cadastro")
        self.titulo.setStyleSheet("font-size: 28px; font-weight: bold; margin-bottom: 20px; color: #2c3e50;")
        layout.addWidget(self.titulo)
        
        self.input_usuario = CampoTextoCustomizado("Nome de Usuário")
        layout.addWidget(self.input_usuario)
        
        self.input_senha = CampoTextoCustomizado("Senha", senha=True)
        layout.addWidget(self.input_senha)
        
        self.btn_registro = BotaoCustomizado("Registrar", cor_fundo="#3498db")
        self.btn_registro.clicked.connect(self.ao_clicar_registrar)
        layout.addWidget(self.btn_registro)
        
        self.btn_ir_login = BotaoCustomizado("Já tenho uma conta", cor_fundo="#34495e")
        self.btn_ir_login.setFlat(True)
        self.btn_ir_login.clicked.connect(self.trocar_para_login.emit)
        layout.addWidget(self.btn_ir_login)
        
        self.setLayout(layout)
        
    def ao_clicar_registrar(self):
        self.requisitar_registro.emit(self.input_usuario.text(), self.input_senha.text())
