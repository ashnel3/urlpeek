from PySide6.QtCore import QUrl, QSize

import urlpeek as Urlpeek
from .BaseWindow import BaseWindow
from ..Widget.WebView import WebView
from ..Widget.ToolBar.RootToolBar import RootToolBar


class MainWindow(BaseWindow):
    TITLE = "Urlpeek"
    webview: WebView

    def __init__(self, parent: "Urlpeek.Application", url: str) -> None:
        super(MainWindow, self).__init__(parent)
        self.setMinimumSize(QSize(480, 320))
        self.setWindowTitle(self.TITLE)
        # add webview
        self.webview = WebView(self, url)
        self.setCentralWidget(self.webview)
        # add root toolbar
        self.addToolBar(RootToolBar(self, url))
        # connect signals
        self.webview.urlChanged.connect(self.setTitle)

    def setTitle(self, url: QUrl) -> None:
        self.setWindowTitle(f"{url.url()} - {self.TITLE}")
