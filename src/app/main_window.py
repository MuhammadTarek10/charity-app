from PySide6.QtWidgets import QMainWindow, QWidget
from Custom_Widgets.Widgets import loadJsonStyle

from typing import Optional

from src.interface.views.main_window_view import Ui_MainWindow as View
from src.app.donations import DonationsWidget
from src.app.case_type import CaseTypesWidget
from src.app.invoices import InvoicesWidget
from src.app.cases import CasesWidget
from src.app.storage import StorageWidget
from src.logic.config.config import Config
from src.logic.utils.helpers.storage_helper import StorageHelper


class MainWindow(QMainWindow, View):
    def __init__(
        self,
        storage: StorageHelper,
        parent: Optional[QMainWindow] = None,
    ) -> None:
        super().__init__(parent)
        self.widget: Optional[QWidget] = None
        self.widgetIndex: int = None
        self.storage = storage
        self.setupUi(self)
        self.setAll()

    def setAll(self) -> None:
        loadJsonStyle(self, self, jsonFiles=Config.STYLE)
        self.donationsButton.clicked.connect(
            lambda event: self.addWidget(
                DonationsWidget(),
                Config.DONATIONS_WIDGET_INDEX,
            )
        )
        self.casesButton.clicked.connect(
            lambda event: self.addWidget(
                CasesWidget(storage=self.storage),
                Config.CASES_WIDGET_INDEX,
            )
        )
        self.casesTypesButton.clicked.connect(
            lambda event: self.addWidget(
                CaseTypesWidget(storage=self.storage),
                Config.CASES_TYPES_WIDGET_INDEX,
            )
        )
        self.invoicesButton.clicked.connect(
            lambda event: self.addWidget(
                InvoicesWidget(),
                Config.INVOICES_WIDGET_INDEX,
            )
        )

        self.storageButton.clicked.connect(
            lambda event: self.addWidget(
                StorageWidget(),
                Config.STORAGE_WIDGET_INDEX,
            )
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
