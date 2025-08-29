import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow,
    QPushButton, QWidget, QHBoxLayout, QVBoxLayout, QFileDialog
)
from PyQt6.QtGui import QIcon, QPalette, QBrush, QPixmap

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

        # --- Left column (buttons) ---
        # save button
        self.save_btn = QPushButton("Save")
        self.save_btn.setIcon(QIcon("save_icon.png"))
        self.save_btn.setFixedSize(100, 40)
        self.save_btn.clicked.connect(self.save_text)

        # open file button
        self.open_btn = QPushButton("Open")
        self.open_btn.setIcon(QIcon("open_icon.png"))
        self.open_btn.setFixedSize(100, 40)
        self.open_btn.clicked.connect(self.open_text)

        # insert image button
        self.img_btn = QPushButton("Image")
        self.img_btn.setIcon(QIcon("img_icon.png"))
        self.img_btn.setFixedSize(100, 40)
        # TODO: implement insert_image function
        # self.save_btn.clicked.connect(self.insert_image)

        # insert image button
        self.style_btn = QPushButton("Style")
        self.style_btn.setIcon(QIcon("style_icon.png"))
        self.style_btn.setFixedSize(100, 40)
        # TODO: implement style function
        # self.save_btn.clicked.connect(self.style)

        left_column = QVBoxLayout()
        left_column.addWidget(self.save_btn)
        left_column.addStretch()
        left_column.addWidget(self.open_btn)
        left_column.addStretch()
        left_column.addWidget(self.img_btn)
        left_column.addStretch()
        left_column.addWidget(self.style_btn)
        left_column.addStretch() 

        # --- Main layout: left column + text editor ---
        layout = QHBoxLayout(central)
        layout.addLayout(left_column)          # left buttons
        layout.addWidget(self.text_area, 1)    # right editor expands

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
