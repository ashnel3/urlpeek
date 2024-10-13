from PySide6.QtWidgets import QApplication
from .Window.MainWindow import MainWindow

import sys
from typing import Sequence


class Application(QApplication):
    def __init__(self):
        QApplication.__init__(self, [])

    @staticmethod
    def Main(args: Sequence[str] = sys.argv) -> int:
        self = Application()
        window = MainWindow(self, "https://example.com")
        window.show()
        return self.exec()
