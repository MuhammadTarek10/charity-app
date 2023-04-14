from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton
from Custom_Widgets.Widgets import loadJsonStyle

from typing import Optional
from src.logic.utils.helpers.pops import Pops

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
        pops: Pops,
        parent: Optional[QMainWindow] = None,
    ) -> None:
        super().__init__(parent)
        self.widget: Optional[QWidget] = None
        self.widgetIndex: int = None
        self.storage = storage
        self.pops = pops
        self.storage.setPops(pops)
        self.setupUi(self)
        self.buttons = [
            self.donationsButton,
            self.casesButton,
            self.casesTypesButton,
            self.invoicesButton,
            self.storageButton,
            self.settingsButton,
            self.aboutButton,
        ]
        self.setAll()

    def setAll(self) -> None:
        loadJsonStyle(self, self, jsonFiles=Config.STYLE)
        self.donationsButton.clicked.connect(
            lambda event: self.addWidget(
                button=self.donationsButton,
                widget=DonationsWidget(storage=self.storage, pops=self.pops),
                index=Config.DONATIONS_WIDGET_INDEX,
            )
        )
        self.casesButton.clicked.connect(
            lambda event: self.addWidget(
                button=self.casesButton,
                widget=CasesWidget(storage=self.storage, pops=self.pops),
                index=Config.CASES_WIDGET_INDEX,
            )
        )
        self.casesTypesButton.clicked.connect(
            lambda event: self.addWidget(
                button=self.casesTypesButton,
                widget=CaseTypesWidget(storage=self.storage, pops=self.pops),
                index=Config.CASES_TYPES_WIDGET_INDEX,
            )
        )
        self.invoicesButton.clicked.connect(
            lambda event: self.addWidget(
                button=self.invoicesButton,
                widget=InvoicesWidget(storage=self.storage, pops=self.pops),
                index=Config.INVOICES_WIDGET_INDEX,
            )
        )

        self.storageButton.clicked.connect(
            lambda event: self.addWidget(
                button=self.storageButton,
                widget=StorageWidget(pops=self.pops),
                index=Config.STORAGE_WIDGET_INDEX,
            )
        )

    def addWidget(
        self,
        button: QPushButton,
        widget: QWidget,
        index: int,
    ) -> None:
        if self.widgetIndex != index:
            self.removeWidget()
            self.widgetIndex = index
            self.widget = widget
            self.mainLayout.addWidget(self.widget)
            button.setStyleSheet(Config.SELECTED_STYLE_BUTTON)
        for b in self.buttons:
            if b == button:
                continue
            b.setStyleSheet(Config.UNSELECTED_STYLE_BUTTON)

    def removeWidget(self) -> None:
        if self.widget is not None:
            self.mainLayout.removeWidget(self.widget)
            self.widget.setParent(None)
            self.widget.deleteLater()
