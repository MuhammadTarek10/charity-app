from PySide6.QtWidgets import QWidget

from typing import Optional

from src.interface.views.case_types_view import Ui_Form as View

from src.logic.config.config import Config
from src.logic.utils.helpers.storage_helper import StorageHelper


class CaseTypesWidget(QWidget, View):
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
        self.saveButton.clicked.connect(self.save)

    def save(self) -> None:
        if self.allGood:
            self.storage.insertCaseType(
                {
                    Config.CASES_TYPES_NAME: self.caseEdit.text(),
                }
            )
        else:
            print("FILL")

    @property
    def allGood(self) -> bool:
        return True if len(self.caseEdit.text()) > 0 else False
