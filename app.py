from typing import Optional
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

from src.app.main_window import MainWindow


class App(QMainWindow):
    def __init__(self, parent: Optional[QMainWindow] = None) -> None:
        super().__init__(parent)
        self.main = MainWindow()
        self.main.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec())
