from src.logic.data.database import Database
from src.logic.config.config import Config
from src.logic.data.models import *


class DatabaseHelper:
    # TODO: getting by foreign keys is not working, fix it
    def __init__(self, db_url: str = Config.DATABASE_URL):
        self.database = Database(db_url)

    def insertCase(self, data: dict) -> None:
        return self.database.insertCase(data)

    def insertDonation(self, data: dict) -> None:
        return self.database.insertDonation(data)

    def insertItem(self, data: dict) -> int:
        return self.database.insertItem(data)

    def insertInvoice(self, data: dict) -> None:
        return self.database.insertInvoice(data)

    def insertCaseType(self, data: dict) -> None:
        return self.database.insertCaseType(data)

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

    def getCaseAllTypes(self) -> list:
        return self.database.getCaseAllTypes()
    
    def getCaseTypeByName(self, name: str) -> CaseType:
        return self.database.getCaseTypeByName(name)
    
    def deleteCaseType(self, name: str) -> bool:
        return self.database.deleteCaseType(name)
