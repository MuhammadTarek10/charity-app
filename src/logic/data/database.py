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

    def insertDonation(self, data: dict) -> None:
        self.session.add(Donations(**data))
        self.session.commit()

    def insertItem(self, data: dict) -> int:
        self.session.add(Item(**data))
        self.session.commit()
        return (
            self.session.query(Item)
            .filter(
                Item.name == data["name"],
                Item.unit == data["unit"],
                Item.quantity == data["quantity"],
            )
            .first()
            .id
        )

    def insertInvoice(self, data: dict) -> None:
        self.session.add(Invoice(**data))
        self.session.commit()

    def insertCaseType(self, data: dict) -> None:
        self.session.add(CaseType(**data))
        self.session.commit()

    def getAllCases(self) -> list:
        return self.session.query(Case).all()

    def getCaseByName(self, name: str) -> Case:
        return self.session.query(Case).filter(Case.name == name).first()

    def getAllDonations(self) -> list:
        return self.session.query(Donations).all()

    def getAllInvoices(self) -> None:
        return self.session.query(Invoice).all()

    def getInvoiceByName(self, name: str) -> Invoice:
        return self.session.query(Invoice).filter(Invoice.name == name).first()

    def getCaseTypes(self) -> list:
        return self.session.query(CaseType).all()

    # *

    def __enter__(self) -> "Database":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()
