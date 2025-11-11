from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QListWidget, QListWidgetItem, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

class Widget(QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        self.setWindowTitle("QListWidget QSS - Demo")

        menu_widget = QListWidget()
        for i in range(10):
            item = QListWidgetItem(f"Item {i}")
            item.setTextAlignment(Qt.AlignCenter)
            menu_widget.addItem(item)
        menu_widget.itemClicked.connect(self.item_clicked)
        
        self.text_widget = QLabel()
        button = QPushButton("Something")

        content_layout = QVBoxLayout()
        content_layout.addWidget(self.text_widget)
        content_layout.addWidget(button)
        main_widget = QWidget()
        main_widget.setLayout(content_layout)

        layout = QHBoxLayout()
        layout.addWidget(menu_widget, 1)
        layout.addWidget(main_widget, 4)

        self.setLayout(layout)

    def item_clicked(self, item):
        print(item.text())
        self.text_widget.setText(item.text())