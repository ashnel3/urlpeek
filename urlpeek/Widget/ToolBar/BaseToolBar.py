from PySide6.QtCore import QSize
from PySide6.QtWidgets import QToolBar, QWidget


class BaseToolBar(QToolBar):
    def __init__(
        self,
        parent: QWidget,
        title: str,
        icon_size=16,
        movable=False,
    ):
        super(BaseToolBar, self).__init__(title, parent)
        self.setIconSize(QSize(icon_size, icon_size))
        self.setMovable(movable)
