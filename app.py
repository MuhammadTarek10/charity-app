from typing import Optional
from PySide6.QtWidgets import QApplication, QMainWindow

from src.app.main_window import MainWindow
from src.logic.utils.helpers.storage_helper import StorageHelper


storage = StorageHelper()

class App(QMainWindow):
    def __init__(self, parent: Optional[QMainWindow] = None) -> None:
        super().__init__(parent)
        self.main = MainWindow(storage=storage)
        self.main.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec())
