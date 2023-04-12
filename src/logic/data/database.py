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

    def totalMoney(self) -> float:
        from sqlalchemy.sql import functions

        income = self.session.query(functions.sum(Donations.value)).scalar()
        outcome = self.session.query(functions.sum(Invoice.value)).scalar()
        income = income if income is not None else 0
        outcome = outcome if outcome is not None else 0
        return income - outcome

    # *Cases
    def getAllCases(self) -> list:
        return self.session.query(Case).all()

    def getCaseByName(self, name: str) -> Case:
        return self.session.query(Case).filter(Case.name == name).first()

    def insertCase(self, data: dict) -> None:
        self.session.add(Case(**data))
        self.session.commit()

    # *CasesTypes
    def getCaseAllTypes(self) -> list:
        return self.session.query(CaseType).all()

    def getCaseTypeByName(self, name: str) -> CaseType:
        return self.session.query(CaseType).filter(CaseType.name == name).first()

    def insertCaseType(self, data: dict) -> None:
        self.session.add(CaseType(**data))
        self.session.commit()

    def deleteCaseType(self, name: str) -> bool:
        self.session.query(CaseType).filter(CaseType.name == name).delete()
        self.session.commit()
        return True

    # *Donations
    def getAllDonations(self) -> list:
        return self.session.query(Donations).all()

    def insertDonation(self, data: dict) -> None:
        self.session.add(Donations(**data))
        self.session.commit()

    # *Donators
    # *Invoices
    def getAllInvoices(self) -> None:
        return self.session.query(Invoice).all()

    def getInvoiceByName(self, name: str) -> Invoice:
        return self.session.query(Invoice).filter(Invoice.name == name).first()

    def insertInvoice(self, data: dict) -> None:
        self.session.add(Invoice(**data))
        self.session.commit()

    # *Items
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

    def __enter__(self) -> "Database":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()
