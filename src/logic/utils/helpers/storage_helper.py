import openpyxl as op

from types import FunctionType
from src.logic.data.database import Database


from src.logic.data.models import *


class StorageHelper:
    def __init__(self, adjustTable: FunctionType = None) -> None:
        self.database: Database = Database(db_url=Config.DATABASE_URL)
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

    def totalMoney(self) -> float:
        return self.database.totalMoney()

    # *Cases
    def getAllCases(self) -> list:
        return self.database.getAllCases()

    def getCaseByName(self, name: str) -> Case:
        return self.database.getCaseByName(name)

    def insertCase(self, data: dict) -> None:
        self.database.insertCase(data)

    # *Cases Types
    def getAllCaseTypes(self) -> list:
        return self.database.getCaseAllTypes()

    def insertCaseType(self, data: dict) -> bool:
        if self.database.getCaseTypeByName(data[Config.CASES_TYPES_NAME]) is None:
            self.database.insertCaseType(data)
            return True
        return False

    def deleteCaseType(self, name: str) -> bool:
        if self.database.getCaseTypeByName(name) is not None:
            self.database.deleteCaseType(name)
            return True
        return False

    # *Invoices
    def getAllInvoices(self) -> list:
        return self.database.getAllInvoices()

    def getInvoiceByName(self, name: str) -> Invoice:
        return self.database.getInvoiceByName(name)

    def insertInvoice(self, data: dict) -> None:
        invoice = {
            Config.INVOICES_DATE: data[Config.INVOICES_DATE],
            Config.INVOICES_VALUE: data[Config.INVOICES_VALUE],
            Config.INVOICES_CASE_ID: data[Config.INVOICES_CASE_ID],
        }
        try:
            item = {
                Config.ITEMS_NAME: data[Config.ITEMS_NAME],
                Config.ITEMS_UNIT: data[Config.ITEMS_UNIT],
                Config.ITEMS_QUANTITY: data[Config.ITEMS_QUANTITY],
                Config.ITEMS_PRICE: data[Config.ITEMS_PRICE],
            }
            # get id of item and make it in invoice
            invoice[Config.INVOICES_ITEM_ID] = self.database.insertItem(item)
        except:
            pass
        self.database.insertInvoice(invoice)

    # *Donators
    def getAllDonators(self) -> list:
        return self.database.getAllDonators()

    def insertDonator(self, data: dict) -> None:
        self.database.insertDonator(data)

    # *Donations
    def getAllDonations(self) -> list:
        return self.database.getAllDonations()

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
            donation[Config.DONATIONS_ITEM_ID] = self.database.insertItem(item)
        except:
            pass
        self.database.insertDonation(donation)

    # *Items
