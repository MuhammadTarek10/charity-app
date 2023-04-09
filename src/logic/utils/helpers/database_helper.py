from src.logic.data.database import Database
from src.logic.config.config import Config


class DatabaseHelper:
    # TODO: getting by foreign keys is not working, fix it
    def __init__(self, db_url: str = Config.DATABASE_URL):
        self.database = Database(db_url)

    def insertCase(self, data: dict) -> None:
        self.database.insertCase(data)

    def insertDonations(self, data: dict) -> None:
        self.database.insertDonations(data)

    def insertCaseType(self, data: dict) -> None:
        self.database.insertCaseType(data)

    def getAllCases(self) -> list:
        return self.database.getAllCases()

    def getAllDonations(self) -> list:
        return self.database.getAllDonations()

    def getCaseTypes(self) -> list:
        return self.database.getCaseTypes()
