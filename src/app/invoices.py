from PySide6.QtCore import QDate
from PySide6.QtWidgets import QWidget

from typing import Optional

from src.interface.views.invoices_view import Ui_Form as View

from src.logic.config.strings import Strings
from src.logic.utils.helpers.storage_helper import StorageHelper
from src.logic.config.config import Config
from src.logic.utils.helpers.pops import Pops


class InvoicesWidget(QWidget, View):
    def __init__(
        self,
        storage: StorageHelper,
        pops: Pops,
        parent: Optional[QWidget] = None,
    ):
        super().__init__(parent)
        self.storage = storage
        self.pops = pops
        self.setupUi(self)
        self.setAll()

    def setAll(self) -> None:
        self.dateCheckBox.clicked.connect(self.dateNow)
        self.saveButton.clicked.connect(self.save)

    def dateNow(self) -> None:
        self.dateEdit.setDate(QDate.currentDate())

    def save(self) -> None:
        if self.allGood:
            self.storage.insertInvoice(
                {
                    Config.INVOICES_CASE_ID: self.getCaseID,
                    Config.INVOICES_DATE: self.dateEdit.text(),
                    Config.INVOICES_VALUE: self.priceEdit.text(),
                    Config.ITEMS_QUANTITY: self.quantityEdit.text(),
                    Config.ITEMS_NAME: self.typeEdit.text(),
                    Config.ITEMS_UNIT: self.unitEdit.text(),
                }
            )
            self.pops.info(Strings.SAVED)
            self.clearAll()

    @property
    def allGood(self) -> None:
        if self.getCaseID is None:
            self.pops.error(Strings.NO_MATCHING_CASE)
            return False
        if self.dateEdit.date().year() < 2010 and (
            len(self.priceEdit.text()) < 1 or len(self.quantityEdit.text()) < 1
        ):
            self.pops.error(Strings.FILL)
            return False
        return True

    @property
    def getCaseID(self) -> str:
        case = self.storage.getCaseByName(name=self.nameEdit.text())
        if case:
            return case.id

    def clearAll(self) -> None:
        self.nameEdit.clear()
        self.priceEdit.clear()
        self.quantityEdit.clear()
        self.typeEdit.clear()
        self.unitEdit.clear()
        self.dateEdit.clear()
