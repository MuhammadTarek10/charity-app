from PySide6.QtCore import QDate
from PySide6.QtWidgets import QWidget

from typing import Optional

from src.interface.views.donations_view import Ui_Form as View

from src.logic.config.strings import Strings
from src.logic.config.config import Config
from src.logic.utils.helpers.storage_helper import StorageHelper
from src.logic.utils.helpers.pops import Pops


class DonationsWidget(QWidget, View):
    def __init__(
        self,
        storage: StorageHelper,
        pops: Pops,
        parent: Optional[QWidget] = None,
    ) -> None:
        super().__init__(parent)
        self.storage = storage
        self.pops = pops
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
                    Config.DONATIONS_DONATOR_NAME: self.nameEdit.text(),
                    Config.DONATIONS_VALUE: self.getValue,
                    Config.DONATION_DATE: self.dateEdit.text(),
                    Config.DONATIONS_ITEM_TYPE: self.typeEdit.text(),
                    Config.ITEMS_NAME: self.donationTypeEdit.text(),
                    Config.ITEMS_UNIT: self.unitEdit.text(),
                    Config.ITEMS_QUANTITY: self.quantityEdit.text(),
                    Config.ITEMS_PRICE: self.priceEdit.text(),
                }
            )
            self.pops.info(Strings.SAVED)
            self.clearAll()
        else:
            self.pops.error(Strings.FILL)

    @property
    def allGood(self) -> bool:
        return (
            True
            if len(self.nameEdit.text()) > 1
            and len(self.typeEdit.text()) > 1
            and self.dateEdit.date().year() > 2010
            else False
        )

    @property
    def getValue(self) -> float:
        try:
            if len(self.valueEdit.text()) > 0:
                return self.valueEdit.text()
            elif len(self.totalPriceEdit.text()) > 0:
                return self.totalPriceEdit.text()
            else:
                raise 0.0
        except:
            return 0.0

    def clearAll(self) -> None:
        self.nameEdit.setText("")
        self.quantityEdit.setText("")
        self.priceEdit.setText("")
        self.totalPriceEdit.setText("0.0")
        self.typeEdit.setText("")
        self.unitEdit.setText("")
        self.dateEdit.setDate(QDate.currentDate())
        self.valueEdit.setText("")
