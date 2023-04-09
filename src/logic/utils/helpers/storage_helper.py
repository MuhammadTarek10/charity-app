import openpyxl as op

from types import FunctionType

from src.logic.utils.helpers.database_helper import DatabaseHelper


class StorageHelper:
    def __init__(self, adjustTable: FunctionType = None) -> None:
        self.databaseHelper: DatabaseHelper = DatabaseHelper()
        self.adjustTable: FunctionType = adjustTable
        self.data: list[tuple] = None
        self.sheet: op.Worksheet = None

    def getDataExcel(self) -> None:
        filepath = "test.xlsx"  # TODO: Remove
        try:
            workbook: op.Workbook = op.load_workbook(filepath)
            self.sheet = workbook.active
            self.data = list(self.sheet.values)
            if len(self.data) > 1:
                self.adjustTable(self.data, self.sheet.max_row, self.sheet.max_column)
        except:
            pass

    def getData(self) -> None:
        pass

    def insertCase(self, data: dict) -> None:
        self.databaseHelper.insertCase(data)

    def insertDonation(self, data: dict) -> None:
        self.databaseHelper.insertDonations(data)

    def insertCaseType(self, data: dict) -> None:
        self.databaseHelper.insertCaseType(data)

    def getAllCases(self) -> list:
        return self.databaseHelper.getAllCases()
    
    def getAllDonations(self) -> list:
        return self.databaseHelper.getAllDonations()

    def getCaseTypes(self) -> list:
        return self.databaseHelper.getCaseTypes()
