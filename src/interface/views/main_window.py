from PySide6.QtWidgets import QMainWindow, QWidget
from Custom_Widgets.Widgets import loadJsonStyle

from typing import Optional

from src.interface.views.main_window_view import Ui_MainWindow as View


class MainWindow(QMainWindow, View):
    def __init__(self, parent: Optional[QMainWindow] = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        loadJsonStyle(self, self, jsonFiles=[":/style/style.json"])

    def addWidget(self, widget: QWidget) -> None:
        self.widget = widget
        self.mainLayout.addWidget(self.widget)

    def removeWidget(self) -> None:
        self.mainLayout.removeWidget(self.widget)
        self.widget.setParent(None)
        self.widget.deleteLater()
