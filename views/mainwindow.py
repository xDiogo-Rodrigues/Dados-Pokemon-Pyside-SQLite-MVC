from PySide6.QtWidgets import QMainWindow, QLabel, QFrame, QPushButton, QLineEdit, QFormLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        """metodo que vai representa a tela principal da aplicação"""
        super().__init__()
        self.setStyleSheet('background-color: #00BFFF;')
        self.setWindowTitle('POKEMON')
        self.setWindowIcon(QPixmap('views/images/icon_pokemon.png'))
        self.setFixedSize(QSize(320,230))

        #widgets
        self.lbl_imagem_pokemon = QLabel()
        self.lbl_imagem_pokemon.setPixmap(QPixmap('views/images/mobile_icon.png'))
        self.lbl_imagem_pokemon.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.lbl_nome_pesuisa = QLabel('DIGITE O NOME DO POKEMON PARA SER PESQUISADO')
        self.line_edit_nome_pokemon = QLineEdit()
        self.line_edit_nome_pokemon.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.button = QPushButton('PESQUISAR')
       
        #layout
        layout = QFormLayout()
        layout.addWidget(self.lbl_imagem_pokemon)
        layout.addWidget(self.lbl_nome_pesuisa)
        layout.addWidget(self.line_edit_nome_pokemon)
        layout.addWidget(self.button)

        #container
        container = QFrame()
        container.setLayout(layout)
        self.setCentralWidget(container)