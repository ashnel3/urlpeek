from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QComboBox, QFileDialog, QSizePolicy

from urlpeek import Window
from .BaseToolBar import BaseToolBar
from ..LabelEdit import LabelEdit
from ..WebView import WebView

# TODO: add pdf support

class FormatComboBox(QComboBox):
    def __init__(self, parent: "RootToolBar") -> None:
        super().__init__(parent)
        self.addItems(["png", "jpg"])
        self.setMinimumHeight(31)

class RootToolBar(BaseToolBar):
    combobox: FormatComboBox
    label: LabelEdit
    webview: WebView

    def __init__(self, parent: "Window.MainWindow", url: str):
        super(RootToolBar, self).__init__(parent, icon_size=24, title="root")
        self.webview = parent.webview
        # capture action
        self.addAction(RootToolBar.ActionCapture(self))
        # url edit
        self.label = LabelEdit(self, url)
        self.label.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Preferred,
        )
        self.addWidget(self.label)
        # format combo
        self.combobox = FormatComboBox(self)
        self.addWidget(self.combobox)
        # add options action
        self.addAction(RootToolBar.ActionOptions(self))
        # connect signals
        self.label.changed.connect(self.webview.setUrl)

    @staticmethod
    def ActionCapture(parent: 'RootToolBar') -> QAction:
        def OnActionCapture() -> None:
            filename, _ = QFileDialog.getSaveFileName(
                parent, filter="Images (*.gif *.png *.jpg *.jpeg)"
            )
            if not filename:
                return
            parent.webview.screenshot().save(filename)

        action = QAction(QIcon.fromTheme("media-record"), "&Capture", parent)
        action.triggered.connect(OnActionCapture)
        return action

    @staticmethod
    def ActionOptions(parent: 'RootToolBar') -> QAction:
        action = QAction(QIcon.fromTheme("application-menu"), "&Options", parent)
        action.triggered.connect(lambda: print("menu"))
        return action
