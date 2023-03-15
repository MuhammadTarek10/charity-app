from PySide6.QtCore import QDateTime
from PySide6.QtWidgets import QWidget

from typing import Optional

from src.interface.views.donations_view import Ui_Form as View


class DonationsWidget(View):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setAll()

    def setAll(self) -> None:
        self.quantityEdit.textChanged.connect(self.updateTotalPrice)
        self.priceEdit.textChanged.connect(self.updateTotalPrice)
        self.timeNowBox.clicked.connect(self.timeNow)
        self.saveButton.clicked.connect(self.save)

    def updateTotalPrice(self) -> None:
        quantity = self.quantityEdit.text()
        price = self.priceEdit.text()
        if quantity and price:
            try:
                self.totalPriceEdit.setText(str(float(quantity) * float(price)))
            except:
                pass

    def timeNow(self) -> None:
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())

    def save(self) -> None:
        pass
