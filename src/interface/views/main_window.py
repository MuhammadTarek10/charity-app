from PySide6.QtWidgets import QMainWindow, QWidget
from Custom_Widgets.Widgets import loadJsonStyle

from typing import Optional

from src.interface.views.main_window_view import Ui_MainWindow as View
from src.interface.views.donations import DonationsWidget
from src.interface.views.case_type import CaseTypesWidget


class MainWindow(QMainWindow, View):
    def __init__(self, parent: Optional[QMainWindow] = None) -> None:
        super().__init__(parent)
        self.widget: Optional[QWidget] = None
        self.setupUi(self)
        loadJsonStyle(self, self, jsonFiles=[":/style/style.json"])
        self.donationsButton.clicked.connect(
            lambda event: self.addWidget(DonationsWidget())
        )
        self.casesTypesButton.clicked.connect(
            lambda event: self.addWidget(CaseTypesWidget())
        )

    def addWidget(self, widget: QWidget) -> None:
        self.removeWidget()
        self.widget = widget
        self.mainLayout.addWidget(self.widget)

    def removeWidget(self) -> None:
        if self.widget is not None:
            self.mainLayout.removeWidget(self.widget)
            self.widget.setParent(None)
            self.widget.deleteLater()
