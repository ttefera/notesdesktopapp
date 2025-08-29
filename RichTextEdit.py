from PyQt6.QtWidgets import QTextEdit, QApplication
from PyQt6.QtGui import QTextCursor, QPixmap
from PyQt6.QtCore import Qt, QBuffer, QIODevice
import base64
from io import BytesIO

class RichTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptRichText(True)

    def keyPressEvent(self, event):
        if (event.modifiers() == Qt.KeyboardModifier.ControlModifier or
            event.modifiers() == Qt.KeyboardModifier.MetaModifier) and event.key() == Qt.Key.Key_V:
            self.paste_image_from_clipboard()
        else:
            super().keyPressEvent(event)

    def contextMenuEvent(self, event):
        menu = self.createStandardContextMenu()
        for action in menu.actions():
            if "Paste" in action.text():
                action.triggered.disconnect()
                action.triggered.connect(self.paste_image_from_clipboard)
        menu.exec(event.globalPos())

    def paste_image_from_clipboard(self):
        clipboard = QApplication.clipboard()
        mime = clipboard.mimeData()

        if mime.hasImage():
            image = clipboard.image()  # QImage
            pixmap = QPixmap.fromImage(image)

            # Save to QBuffer (in-memory)
            buffer = QBuffer()
            buffer.open(QIODevice.OpenModeFlag.WriteOnly)
            pixmap.save(buffer, "PNG")
            b64_data = base64.b64encode(buffer.data()).decode("utf-8")

            # Insert as HTML
            html = f'<img src="data:image/png;base64,{b64_data}">'
            cursor = self.textCursor()
            cursor.insertHtml(html)
        else:
            self.paste()
