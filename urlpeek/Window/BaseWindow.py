from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow


class BaseWindow(QMainWindow):
    app: QApplication

    def __init__(
        self,
        app: QApplication,
    ) -> None:
        QMainWindow.__init__(self, None, Qt.WindowType.Window)
        self.app = app
