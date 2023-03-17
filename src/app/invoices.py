from PySide6.QtCore import QDate
from PySide6.QtWidgets import QWidget

from typing import Optional

from src.interface.views.invoices_view import Ui_Form as View


class InvoicesWidget(View):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setAll()

    def setAll(self) -> None:
        self.dateCheckBox.clicked.connect(self.dateNow)
        self.saveButton.clicked.connect(self.save)

    def dateNow(self) -> None:
        self.dateEdit.setDate(QDate.currentDate())

    def save(self) -> None:
        pass
