from PySide6.QtWidgets import QWidget, QTableWidgetItem

from typing import List, Optional

from src.interface.views.storage_view import Ui_Form as View
from src.logic.utils.helpers.storage_helper import StorageHelper
from src.logic.utils.helpers.filter_helper import FilterHelper
from src.logic.utils.helpers.pops import Pops
from src.logic.config.config import Config


class StorageWidget(QWidget, View):
    def __init__(
        self,
        pops: Pops,
        parent: Optional[QWidget] = None,
    ) -> None:
        super().__init__(parent)
        self.storage: StorageHelper = StorageHelper(adjustTable=self.adjustTable)
        self.pops = pops
        self.setupUi(self)
        self.storageTableWidget.verticalHeader().setVisible(False)
        self.setAll()

    def setAll(self) -> None:
        self.tableComboBox.addItems(Config.TABLES.values())
        self.totalPriceValue.setText(str(self.storage.totalMoney()))
        self.tableComboBox.currentIndexChanged.connect(self.changeColumns)
        self.columnComboBox.addItems(
            FilterHelper.getColumns(self.tableComboBox.currentText())
        )
        self.insert(FilterHelper.getTableData(self.tableComboBox.currentText()))

    def changeColumns(self, index) -> None:
        self.columnComboBox.addItems(
            FilterHelper.getColumns(self.tableComboBox.currentText())
        )
        self.insert(FilterHelper.getTableData(self.tableComboBox.currentText()))

    def adjustTable(self, values: List[tuple], maxRows: int, maxCols: int) -> None:
        self.storageTableWidget.setRowCount(maxRows)
        self.storageTableWidget.setColumnCount(maxCols)
        self.insertItems(values)

    def insertItems(self, values: list) -> None:
        if len(values) > 1:
            self.storageTableWidget.setHorizontalHeaderLabels(values[0])
            rowIndex, colIndex = 0, 0
            try:
                for colValues in values[1]:
                    for rowValues in colValues:
                        self.storageTableWidget.setItem(
                            rowIndex,
                            colIndex,
                            QTableWidgetItem(str(rowValues)),
                        )
                        colIndex += 1
                    rowIndex += 1
                    colIndex = 0
            except:
                pass

    def insert(self, values: list) -> None:
        if len(values) > 1:
            self.adjustTable(values, len(values[1]), len(values[0]))
