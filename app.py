from typing import Optional
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

from src.interface.views.main_window import MainWindow
from src.interface.views.donations import DonationsWidget


class App(QMainWindow):
    def __init__(self, parent: Optional[QMainWindow] = None) -> None:
        super().__init__(parent)
        self.main = MainWindow()
        self.widget: Optional[QWidget] = None
        self.main.addWidget(DonationsWidget())
        self.main.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec())
