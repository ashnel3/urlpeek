from PySide6.QtCore import QUrl
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView

# TODO: resize tooltip
# TODO: class type forwarding

class WebView(QWebEngineView):
    def __init__(self, parent: QWidget, url: str):
        super(WebView, self).__init__(parent)
        self.setUrl(url)

    def setUrl(self, url: str) -> None:
        self.parent().setWindowTitle(f"Urlpeek - {url}")
        return super().setUrl(url)

    def screenshot(self) -> QPixmap:
        pixmap = QPixmap(self.frameSize())
        self.render(pixmap)
        return pixmap
