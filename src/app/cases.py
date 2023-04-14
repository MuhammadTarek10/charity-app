from PySide6.QtWidgets import QWidget

from typing import Optional

from src.interface.views.cases_view import Ui_Form as View

from src.logic.config.config import Config
from src.logic.config.strings import Strings
from src.logic.utils.helpers.storage_helper import StorageHelper
from src.logic.utils.helpers.input_helper import InputHelper
from src.logic.utils.helpers.pops import Pops


class CasesWidget(QWidget, View):
    def __init__(
        self,
        storage: StorageHelper,
        pops: Pops,
        parent: Optional[QWidget] = None,
    ) -> None:
        super().__init__(parent)
        self.storage = storage
        self.pops = pops
        self.types = self.storage.getAllCaseTypes()
        self.setupUi(self)
        self.setAll()

    def setAll(self) -> None:
        self.saveButton.clicked.connect(self.save)
        self.caseEdit.addItem(Strings.CHOOSE_CASE)
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
            self.pops.info(Strings.SAVED)
            self.clearAll()
        else:
            pass

    @property
    def allGood(self) -> bool:
        if (
            len(self.nameEdit.text()) < 1
            or len(self.ageEdit.text()) < 1
            or self.caseEdit.currentIndex() == 0
        ):
            self.pops.error(Strings.FILL)
            return False
        if not InputHelper.validateNationalId(self.iDEdit.text()):
            print(self.iDEdit.text())
            self.pops.error(Strings.INVALID_ID)
            return False
        if not InputHelper.validatePhoneNumber(self.phoneEdit.text()):
            print(self.phoneEdit.text())
            self.pops.error(Strings.INVALID_PHONE)
            return False
        return True

    @property
    def caseTypeId(self) -> int:
        for type in self.types:
            if type.name == self.caseEdit.currentText():
                return type.id

    def clearAll(self) -> None:
        self.nameEdit.clear()
        self.iDEdit.clear()
        self.phoneEdit.clear()
        self.ageEdit.clear()
        self.addressEdit.clear()
        self.caseEdit.setCurrentIndex(0)
