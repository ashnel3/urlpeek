from PySide6.QtCore import QSize, QCoreApplication
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QFileDialog, QToolBar, QSizePolicy

from urlpeek import Window
from ..LabelEdit import LabelEdit
from ..WebView import WebView


class RootToolBar(QToolBar):
    label: LabelEdit
    webview: WebView

    def __init__(self, parent: "Window.MainWindow", url: str):
        super(RootToolBar, self).__init__("root", parent)
        self.setIconSize(QSize(24, 24))
        self.setMovable(False)
        self.webview = parent.webview
        # actions right
        self.addActions([self.ActionCapture()])
        # url edit
        self.label = LabelEdit(self, url)
        self.label.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Preferred,
        )
        self.addWidget(self.label)
        # actions left
        self.addActions(
            [
                self.ActionProperties(),
                self.ActionQuit(),
            ]
        )
        # connect signals
        self.label.changed.connect(lambda url: self.webview.setUrl(url))

    def ActionCapture(self) -> QAction:
        def OnActionCapture() -> None:
            filename, _ = QFileDialog.getSaveFileName(
                self, filter="Images (*.gif *.png *.jpg *.jpeg)"
            )
            if not filename:
                return
            self.webview.screenshot().save(filename)

        action = QAction(QIcon.fromTheme("media-record"), "&Capture", self)
        action.triggered.connect(OnActionCapture)
        return action

    def ActionProperties(self) -> QAction:
        action = QAction(QIcon.fromTheme("application-menu"), "&Properties", self)
        action.triggered.connect(lambda: print("menu"))
        return action

    def ActionQuit(self) -> QAction:
        action = QAction(QIcon.fromTheme("window-close"), "&Quit", self)
        action.triggered.connect(lambda: QCoreApplication.quit())
        return action
