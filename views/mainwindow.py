from PySide6.QtWidgets import QMainWindow, QLabel, QFrame, QPushButton, QLineEdit, QFormLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('POKEMON')
        self.setWindowIcon(QPixmap('views/images/icon_pokebola.png'))
        self.setFixedSize(QSize(500,400))