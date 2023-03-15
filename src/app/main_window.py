from PySide6.QtWidgets import QMainWindow, QWidget
from Custom_Widgets.Widgets import loadJsonStyle

from typing import Optional

from src.interface.views.main_window_view import Ui_MainWindow as View
from src.app.donations import DonationsWidget
from src.app.case_type import CaseTypesWidget
from src.app.invoices import InvoicesWidget
from src.logic.config.config import Config


class MainWindow(QMainWindow, View):
    def __init__(self, parent: Optional[QMainWindow] = None) -> None:
        super().__init__(parent)
        self.widget: Optional[QWidget] = None
        self.widgetIndex = None
        self.setupUi(self)
        loadJsonStyle(self, self, jsonFiles=[":/style/style.json"])
        self.donationsButton.clicked.connect(
            lambda event: self.addWidget(
                DonationsWidget(), Config.DONATIONS_WIDGET_INDEX
            )
        )
        self.casesTypesButton.clicked.connect(
            lambda event: self.addWidget(
                CaseTypesWidget(), Config.CASES_TYPES_WIDGET_INDEX
            )
        )
        self.invoicesButton.clicked.connect(
            lambda event: self.addWidget(InvoicesWidget(), Config.INVOICES_WIDGET_INDEX)
        )

    def addWidget(self, widget: QWidget, index: int) -> None:
        if self.widgetIndex != index:
            self.removeWidget()
            self.widgetIndex = index
            self.widget = widget
            self.mainLayout.addWidget(self.widget)

    def removeWidget(self) -> None:
        if self.widget is not None:
            self.mainLayout.removeWidget(self.widget)
            self.widget.setParent(None)
            self.widget.deleteLater()
