from PySide6.QtWidgets import QWidget, QTableWidgetItem

from typing import List, Optional

from src.interface.views.storage_view import Ui_Form as View
from src.logic.utils.helpers.storage_helper import StorageHelper


class StorageWidget(QWidget, View):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.helper: StorageHelper = StorageHelper(adjustTable=self.adjustTable)
        self.setupUi(self)
        self.storageTableWidget.verticalHeader().setVisible(False)
        self.setAll()

    def setAll(self) -> None:
        self.helper.getDataExcel()

    def adjustTable(self, values: List[tuple], maxRows: int, maxCols: int) -> None:
        self.storageTableWidget.setRowCount(maxRows)
        self.storageTableWidget.setColumnCount(maxCols)
        self.insertItems(values)

    def insertItems(self, values: list) -> None:
        self.storageTableWidget.setHorizontalHeaderLabels(values[0])
        rowIndex, colIndex = 0, 0
        for colValues in values[1:]:
            for rowValues in colValues:
                self.storageTableWidget.setItem(
                    rowIndex,
                    colIndex,
                    QTableWidgetItem(str(rowValues)),
                )
                colIndex += 1
            rowIndex += 1
            colIndex = 0
