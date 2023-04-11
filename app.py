from typing import Optional
from PySide6.QtWidgets import QApplication, QMainWindow

from src.app.main_window import MainWindow
from src.logic.utils.helpers.storage_helper import StorageHelper
from src.logic.utils.helpers.pops import Pops


class App(QMainWindow):
    def __init__(
        self,
        storage: StorageHelper,
        pops: Pops,
        parent: Optional[QMainWindow] = None,
    ) -> None:
        super().__init__(parent)
        self.main = MainWindow(storage=storage, pops=pops)
        self.main.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    storage = StorageHelper()
    pops = Pops()
    window = App(
        storage=storage,
        pops=pops,
    )
    sys.exit(app.exec())
