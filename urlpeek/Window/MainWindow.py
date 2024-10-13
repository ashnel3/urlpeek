from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget

from .BaseWindow import BaseWindow
from ..Widget.WebView import WebView
from ..Widget.ToolBar.RootToolBar import RootToolBar


class MainWindow(BaseWindow):
    webview: WebView

    def __init__(self, parent: QWidget, url: str) -> None:
        super(MainWindow, self).__init__(parent)
        self.setMinimumSize(QSize(480, 320))
        self.setWindowTitle("Urlpeek")
        # webview
        self.webview = WebView(self, url)
        self.setCentralWidget(self.webview)
        # main toolbar
        self.addToolBar(RootToolBar(self, url))
