import os
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow,
    QPushButton, QWidget, QHBoxLayout, QVBoxLayout, QFileDialog
)
from PyQt6.QtGui import QIcon, QPalette, QBrush, QPixmap
from PyQt6.QtCore import QSize
from RichTextEdit import RichTextEdit

class NotesApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cute Notes")
        self.setGeometry(200, 200, 800, 500)

        # central widget
        central = QWidget(self)
        self.setCentralWidget(central)

        # background image
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(QPixmap("background.png")))
        central.setAutoFillBackground(True)
        central.setPalette(palette)

        # text editor
        self.text_area = RichTextEdit()
        self.text_area.setAcceptRichText(True)

        # --- Main layout: left column + text editor ---
        layout = QHBoxLayout(central)
        layout.addLayout(self.build_left_column())  # left buttons
        layout.addWidget(self.text_area, 1) # right editor expands

    def build_left_column(self)->QVBoxLayout:
        self.save_btn = self.create_button("save_icon.png", self.save_text)
        self.open_btn = self.create_button("open_icon.png",self.open_text)
        self.img_btn = self.create_button("img_icon.png")
        # TODO: implement insert_image function
        # self.save_btn.clicked.connect(self.insert_image)
        self.style_btn = self.create_button("style_icon.png")
        # TODO: implement style function
        # self.save_btn.clicked.connect(self.style)

        left_column = QVBoxLayout()
        left_column.addStretch()
        left_column.addWidget(self.save_btn)
        left_column.addStretch()
        left_column.addWidget(self.open_btn)
        left_column.addStretch()
        left_column.addWidget(self.img_btn)
        left_column.addStretch()
        left_column.addWidget(self.style_btn)
        left_column.addStretch() 
        return left_column

    def create_button(self, icon_name, callback=None) -> QPushButton:
        # Absolute path (avoids relative issues)
        icon_path = os.path.join(os.path.dirname(__file__), "assets", icon_name)
        print("Loading icon from:", icon_path, "Exists?", os.path.exists(icon_path))

        # create button
        btn = QPushButton()
        btn.setIcon(QIcon(icon_path))
        btn.setFixedSize(40, 40)
        
        btn.setIconSize(QSize(40, 40))  # scale icon to fit button
        if callback is not None:
            btn.clicked.connect(callback)
        return btn

    def save_text(self):
        with open("note.html", "w", encoding="utf-8") as f:
            f.write(self.text_area.toHtml())

    def open_text(self):
        # open a file dialog
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open HTML File", "", "HTML Files (*.html);;All Files (*)"
        )        
        if file_path:
            with open(file_path, "r", encoding="utf-8") as f:
                self.text_area.setHtml(f.read())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NotesApp()
    window.show()
    sys.exit(app.exec())
