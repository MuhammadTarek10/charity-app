from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


from src.logic.data.models import *


class Database:
    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)
        self.session = sessionmaker(bind=self.engine)()
        self.createAll()

    def createAll(self):
        Base.metadata.create_all(self.engine)

    def insertCase(self, data: dict) -> None:
        self.session.add(Case(**data))
        self.session.commit()

    def insertDonations(self, data: dict) -> None:
        self.session.add(Donate(**data))
        self.session.commit()

    def insertCaseType(self, data: dict) -> None:
        self.session.add(CaseType(**data))
        self.session.commit()

    def getAllCases(self) -> list:
        return self.session.query(Case).all()

    def getAllDonations(self) -> list:
        return self.session.query(Donate).all()

    def getCaseTypes(self) -> list:
        return self.session.query(CaseType).all()

    def __enter__(self) -> "Database":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()
