from PySide6.QtCore import QSize
from PySide6.QtWidgets import QSizePolicy, QWidget

from typing import Optional


class Spacer(QWidget):
    def __init__(
        self,
        parent: Optional[QWidget] = None,
        max_size: Optional[QSize] = None,
        min_size: Optional[QSize] = None,
        x_size_policy: QSizePolicy.Policy = QSizePolicy.Policy.Expanding,
        y_size_policy: QSizePolicy.Policy = QSizePolicy.Policy.Expanding,
    ) -> None:
        super().__init__(parent)
        if max_size:
            self.setMaximumSize(max_size)
        if min_size:
            self.setMinimumSize(min_size)
        self.setSizePolicy(x_size_policy, y_size_policy)
