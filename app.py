from PySide6.QtWidgets import QApplication, QMainWindow
from Custom_Widgets.Widgets import loadJsonStyle

from typing import Optional

from src.interface.views.mainWindow import Ui_MainWindow as View


class MainWindow(QMainWindow, View):
    def __init__(self, parent: Optional[QMainWindow] = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        loadJsonStyle(self, self, jsonFiles=[":/style/style.json"])
        self.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
