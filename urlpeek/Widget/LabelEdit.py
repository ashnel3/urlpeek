from PySide6.QtCore import Signal
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QHBoxLayout, QLineEdit, QLabel, QWidget


class LabelEdit(QWidget):
    changed = Signal(str)
    edit: QLineEdit
    label: QLabel

    def __init__(self, parent: QWidget, text: str):
        super(LabelEdit, self).__init__(parent)
        layout = QHBoxLayout(self)
        self.label = QLabel(str(text), self)
        self.label.setStyleSheet("padding: 4px 0;")
        self.edit = QLineEdit(str(text), self)
        self.edit.hide()
        # signals
        self.edit.editingFinished.connect(self._edit_stop)
        self.edit.returnPressed.connect(self._edit_start)
        layout.addWidget(self.label)
        layout.addWidget(self.edit)

    def _edit_start(self) -> None:
        self.label.hide()
        self.edit.show()
        self.edit.setFocus()

    def _edit_stop(self) -> None:
        text = self.edit.text()
        self.edit.hide()
        self.label.show()
        if text != self.label.text():
            self.label.setText(text)
            self.changed.emit(text)

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        self._edit_start()
