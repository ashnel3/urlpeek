from PySide6.QtCore import Signal
from PySide6.QtGui import QAction, QIcon, QMouseEvent
from PySide6.QtWidgets import QComboBox, QFileDialog, QLabel, QLineEdit, QHBoxLayout, QSizePolicy, QWidget

from urlpeek import Window
from .BaseToolBar import BaseToolBar
from ..WebView import WebView

# TODO: add pdf support
# TODO: add action hotkeys

class FormatComboBox(QComboBox):
    def __init__(self, parent: "RootToolBar") -> None:
        super().__init__(parent)
        self.addItems(["png", "jpg"])
        self.setMinimumHeight(31)


class ToggleEdit(QWidget):
    changed = Signal(str)
    _layout: QHBoxLayout
    _edit: QLineEdit
    _label: QLabel

    def __init__(self, parent: 'RootToolBar', text: str):
        super(ToggleEdit, self).__init__(parent)
        self._layout = QHBoxLayout(self)
        # label
        self._label = QLabel(str(text), self)
        self._label.setStyleSheet("padding: 4px 0;")
        self._layout.addWidget(self._label)
        # edit
        self._edit = QLineEdit(str(text), self)
        self._edit.hide()
        self._layout.addWidget(self._edit)
        # signals
        self._edit.editingFinished.connect(self._edit_stop)
        self._edit.returnPressed.connect(self._edit_start)
        self._edit.focusOutEvent = lambda event: self._edit_stop()

    def _edit_start(self) -> None:
        self._label.hide()
        self._edit.show()
        self._edit.setFocus()

    def _edit_stop(self) -> None:
        text = self._edit.text()
        if text != self._label.text():
            self.changed.emit(text)
            self._label.setText(text)
        self._edit.hide()
        self._label.show()

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        self._edit_start()


class RootToolBar(BaseToolBar):
    _combobox: FormatComboBox
    _edit: ToggleEdit
    _webview: WebView

    def __init__(self, parent: "Window.MainWindow", url: str):
        super(RootToolBar, self).__init__(parent, icon_size=24, title="root")
        self._webview = parent.webview
        # capture action
        self.addAction(RootToolBar.ActionCapture(self))
        # url edit bar
        self._edit = ToggleEdit(self, url)
        self._edit.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Preferred,
        )
        self.addWidget(self._edit)
        # format combo
        self._combobox = FormatComboBox(self)
        self.addWidget(self._combobox)
        # add options action
        self.addAction(RootToolBar.ActionOptions(self))
        # connect signals
        self._edit.changed.connect(self._webview.setUrl)

    @staticmethod
    def ActionCapture(parent: 'RootToolBar') -> QAction:
        def OnActionCapture() -> None:
            filename, _ = QFileDialog.getSaveFileName(
                parent, filter="Images (*.gif *.png *.jpg *.jpeg)"
            )
            if filename:
                parent._webview.screenshot().save(filename)

        action = QAction(QIcon.fromTheme("media-record"), "&Capture", parent)
        action.triggered.connect(OnActionCapture)
        return action

    @staticmethod
    def ActionOptions(parent: 'RootToolBar') -> QAction:
        action = QAction(QIcon.fromTheme("application-menu"), "&Options", parent)
        action.triggered.connect(lambda: print("menu"))
        return action
