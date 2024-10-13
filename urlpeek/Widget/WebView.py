from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView

from urlpeek import Window

# TODO: resize tooltip


class WebView(QWebEngineView):
    def __init__(self, parent: "Window.MainWindow", url: str):
        super(WebView, self).__init__(parent)
        self.setUrl(url)

    def screenshot(self) -> QPixmap:
        pixmap = QPixmap(self.frameSize())
        self.render(pixmap)
        return pixmap
