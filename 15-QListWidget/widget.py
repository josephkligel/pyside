from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QButtonGroup, QListWidget

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QListWidget")