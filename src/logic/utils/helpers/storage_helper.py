import openpyxl as op

from types import FunctionType

from src.logic.utils.helpers.database_helper import DatabaseHelper

from src.logic.data.models import *


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
        donation = {
            Config.DONATION_NAME: data[Config.DONATION_NAME],
            Config.DONATION_DATE: data[Config.DONATION_DATE],
            Config.DONATIONS_VALUE: data[Config.DONATIONS_VALUE],
        }
        try:
            item = {
                Config.ITEMS_NAME: data[Config.ITEMS_NAME],
                Config.ITEMS_UNIT: data[Config.ITEMS_UNIT],
                Config.ITEMS_QUANTITY: data[Config.ITEMS_QUANTITY],
                Config.ITEMS_PRICE: data[Config.ITEMS_PRICE],
            }
            # get id of item and make it in donation
            donation[Config.DONATIONS_ITEM_ID] = self.databaseHelper.insertItem(item)
        except:
            pass
        self.databaseHelper.insertDonation(donation)

    def insertInvoice(self, data: dict) -> None:
        self.databaseHelper.insertInvoice(data)

    def insertCaseType(self, data: dict) -> None:
        self.databaseHelper.insertCaseType(data)

    def getAllCases(self) -> list:
        return self.databaseHelper.getAllCases()

    def getCaseByName(self, name: str) -> Case:
        return self.databaseHelper.getCaseByName(name)

    def getAllInvoices(self) -> list:
        return self.databaseHelper.getAllInvoices()

    def getInvoiceByName(self, name: str) -> Invoice:
        return self.databaseHelper.getInvoiceByName(name)

    def getAllDonations(self) -> list:
        return self.databaseHelper.getAllDonations()

    def getCaseTypes(self) -> list:
        return self.databaseHelper.getCaseTypes()
