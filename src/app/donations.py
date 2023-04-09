from PySide6.QtCore import QDate
from PySide6.QtWidgets import QWidget

from typing import Optional

from src.interface.views.donations_view import Ui_Form as View

from src.logic.config.config import Config
from src.logic.utils.helpers.storage_helper import StorageHelper


class DonationsWidget(QWidget, View):
    def __init__(
        self,
        storage: StorageHelper,
        parent: Optional[QWidget] = None,
    ) -> None:
        super().__init__(parent)
        self.storage = storage
        self.setupUi(self)
        self.setAll()

    def setAll(self) -> None:
        self.quantityEdit.textChanged.connect(self.updateTotalPrice)
        self.priceEdit.textChanged.connect(self.updateTotalPrice)
        self.dateNowBox.clicked.connect(self.dateNow)
        self.saveButton.clicked.connect(self.save)

    def updateTotalPrice(self) -> None:
        quantity = self.quantityEdit.text()
        price = self.priceEdit.text()
        if quantity and price:
            try:
                self.totalPriceEdit.setText(str(float(quantity) * float(price)))
            except:
                pass

    def dateNow(self) -> None:
        self.dateEdit.setDate(QDate.currentDate())

    def save(self) -> None:
        if self.allGood:
            self.storage.insertDonation(
                {
                    Config.DONATE_NAME: self.nameEdit.text(),
                    Config.DONATE_PRICE: self.totalPriceEdit.text(),
                    Config.DONATE_QUANTITY: self.quantityEdit.text(),
                    Config.DONATE_ITEM_TYPE: self.typeEdit.text(),
                    Config.DONATE_UNIT: self.unitEdit.text(),
                    Config.DONATE_DATE: self.dateEdit.text(),
                    Config.DONATE_VALUE: self.valueEdit.text(),
                }
            )

    @property
    def allGood(self) -> bool:
        return (
            True
            if len(self.nameEdit.text()) > 1
            and len(self.typeEdit.text()) > 1
            and self.dateEdit.date().year() > 2010
            else False
        )
