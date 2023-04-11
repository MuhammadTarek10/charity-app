from PySide6.QtWidgets import QWidget, QListWidgetItem

from typing import List, Optional

from src.interface.views.case_types_view import Ui_Form as View

from src.logic.data.models import CaseType
from src.logic.config.config import Config
from src.logic.utils.helpers.storage_helper import StorageHelper
from src.logic.utils.helpers.pops import Pops
from src.logic.config.strings import Strings


class CaseTypesWidget(QWidget, View):
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
        self.saveButton.clicked.connect(self.save)
        self.deleteTypeButton.clicked.connect(self.deleteItem)
        self.fillCases()

    def deleteItem(self) -> None:
        if self.casesTypes.currentItem():
            if self.pops.confirm(Strings.DELETE):
                self.storage.deleteCaseType(self.casesTypes.currentItem().text())
                self.fillCases()

    def save(self) -> None:
        if self.allGood:
            if self.storage.insertCaseType(
                {Config.CASES_TYPES_NAME: self.caseEdit.text()}
            ):
                self.pops.info(Strings.SAVED)
                self.clearAll()
                self.fillCases()
            else:
                self.pops.error(Strings.CASE_TYPE_ALREADY_EXISTS)
        else:
            self.pops.error(Strings.ADD_CASE_TYPE)

    @property
    def allGood(self) -> bool:
        return True if len(self.caseEdit.text()) > 0 else False

    def clearAll(self):
        self.caseEdit.clear()

    def fillCases(self) -> None:
        self.casesTypes.clear()
        for case in self.allCases:
            self.casesTypes.addItem(case.name)

    @property
    def allCases(self) -> List[CaseType]:
        return self.storage.getAllCaseTypes()
