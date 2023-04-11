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
                    Config.INVOICE_PRICE: self.priceEdit.text(),
                    Config.INVOICE_QUANTITY: self.quantityEdit.text(),
                    Config.INVOICE_ITEM_TYPE: self.typeEdit.text(),
                    Config.INVOICE_UNIT: self.unitEdit.text(),
                    Config.INVOICE_INVOICE_TYPE_ID: self.typeEdit.text(),
                }
            )
            self.pops.info(Strings.SAVED)
            self.clearAll()
        else:
            self.pops.error(Strings.FILL)

    @property
    def allGood(self) -> None:
        return (
            True
            if self.getCaseID is not None
            and self.dateEdit.date().year() > 2010
            and (len(self.priceEdit.text()) > 1 or len(self.quantityEdit.text()) > 1)
            else False
        )

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
