from PySide6.QtWidgets import QWidget

from typing import Optional

from src.interface.views.case_types_view import Ui_Form as View


class CaseTypesWidget(View):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setAll()

    def setAll(self) -> None:
        self.saveButton.clicked.connect(self.save)

    def save(self) -> None:
        pass
