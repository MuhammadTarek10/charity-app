from src.logic.data.database import Database
from src.logic.config.config import Config
from src.logic.data.models import *


class DatabaseHelper:
    # TODO: getting by foreign keys is not working, fix it
    def __init__(self, db_url: str = Config.DATABASE_URL):
        self.database = Database(db_url)

    def insertCase(self, data: dict) -> None:
        self.database.insertCase(data)

    def insertDonations(self, data: dict) -> None:
        self.database.insertDonations(data)

    def insertInvoice(self, data: dict) -> None:
        self.database.insertInvoice(data)

    def insertCaseType(self, data: dict) -> None:
        self.database.insertCaseType(data)

    def getAllCases(self) -> list:
        return self.database.getAllCases()

    def getCaseByName(self, name: str) -> Case:
        return self.database.getCaseByName(name)

    def getAllDonations(self) -> list:
        return self.database.getAllDonations()

    def getAllInvoices(self) -> list:
        return self.database.getAllInvoices()

    def getInvoiceByName(self, name: str) -> Invoice:
        return self.database.getInvoiceByName(name)

    def getCaseTypes(self) -> list:
        return self.database.getCaseTypes()
