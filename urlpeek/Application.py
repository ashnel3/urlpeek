from PySide6.QtWidgets import QApplication

from .Window.MainWindow import MainWindow
from typing import Optional, Sequence


class Application(QApplication):
    def __init__(self):
        QApplication.__init__(self, [])

    @staticmethod
    def Main(args: Optional[Sequence[str]] = None) -> int:
        self = Application()
        window = MainWindow(self, "https://example.com")
        window.show()
        return self.exec()
