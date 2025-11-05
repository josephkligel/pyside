#Version1
"""
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys
app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Our first main window app!")

button = QPushButton()
button.setText("Press me")

window.setCentralWidget(button)

window.show()

app.exec()
"""
#Version 2: Setting up a seperate class

"""
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Holder App")
        button = QPushButton("Press me!")

        self.setCentralWidget(button)

app = QApplication(sys.argv)

window = ButtonHolder()
window.setWindowTitle("Our first main window app!")

window.show()

app.exec()
"""

from PySide6.QtWidgets import QApplication
from button_holder import ButtonHolder

import sys
app = QApplication(sys.argv)

window = ButtonHolder()
window.show()
app.exec()