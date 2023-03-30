from PySide6.QtWidgets import QWidget

from typing import Optional

from src.interface.views.cases_view import Ui_Form as View

from src.logic.config.config import Config
from src.logic.utils.helpers.storage_helper import StorageHelper


class CasesWidget(QWidget, View):
    def __init__(
        self,
        storage: StorageHelper,
        parent: Optional[QWidget] = None,
    ) -> None:
        super().__init__(parent)
        self.storage = storage
        self.types = self.storage.getCaseTypes()
        self.setupUi(self)
        self.setAll()

    def setAll(self) -> None:
        self.saveButton.clicked.connect(self.save)
        self.caseEdit.addItem("اختر الحالة")
        self.caseEdit.addItems([type.name for type in self.types])

    def save(self) -> None:
        if self.allGood:
            self.storage.insertCase(
                {
                    Config.CASES_NAME: self.nameEdit.text(),
                    Config.CASES_NATIONAL_ID: self.iDEdit.text(),
                    Config.CASES_PHONE_NUMBER: self.phoneEdit.text(),
                    Config.CASES_AGE: self.ageEdit.text(),
                    Config.CASES_ADDRESS: self.addressEdit.text(),
                    Config.CASES_NUM_CHILDREN: self.childrenEdit.text(),
                    Config.CASES_TYPE_ID: self.caseTypeId,
                }
            )
            self.clearAll()
        else:
            print("FILL")

    @property
    def allGood(self) -> bool:
        return (
            True
            if (
                len(self.nameEdit.text()) > 0
                and len(self.iDEdit.text()) > 0
                and len(self.ageEdit.text()) > 0
                and len(self.addressEdit.text()) > 0
                and len(self.phoneEdit.text()) > 0
                and len(self.childrenEdit.text()) > 0
                and self.caseEdit.currentRow() > 0
            )
            else False
        )

    @property
    def caseTypeId(self) -> int:
        for type in self.types:
            if type.name == self.caseEdit.currentItem().text():
                return type.id

    def clearAll(self) -> None:
        self.nameEdit.clear()
        self.iDEdit.clear()
        self.phoneEdit.clear()
        self.ageEdit.clear()
        self.addressEdit.clear()
        self.childrenEdit.clear()
        self.caseEdit.setCurrentRow(0)
