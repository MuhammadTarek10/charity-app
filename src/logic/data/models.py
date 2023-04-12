import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from src.logic.config.config import Config

Base = declarative_base()


class Case(Base):
    __tablename__ = Config.CASES_TABLE
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), nullable=False)
    national_id = sa.Column(sa.String(255), nullable=False)
    phone_number = sa.Column(sa.String(255), nullable=True)
    age = sa.Column(sa.Integer, nullable=False)
    address = sa.Column(sa.String(255), nullable=False)
    num_children = sa.Column(sa.Integer, nullable=False, default=0)
    type_id = sa.Column(sa.Integer, sa.ForeignKey("case_type.id"), nullable=False)

    type = relationship("CaseType", back_populates="cases")
    children = relationship("Child", back_populates="case")
    comments = relationship("Comment", back_populates="case")
    invoice = relationship("Invoice", back_populates="case")

    def __str__(self) -> str:
        return f"id: {self.id}, name: {self.name}, national id: {self.national_id}, phone number: {self.phone_number}, type: {self.type.id}"

    def fromJson(self, json: dict) -> None:
        self.name = json["name"]
        self.national_id = json["national_id"]
        self.phone_number = json["phone_number"]
        self.age = json["age"]
        self.address = json["address"]
        self.type_id = json["type_id"]

    def toTuple(self) -> tuple:
        return (
            self.id,
            self.name,
            self.national_id,
            self.phone_number,
            self.age,
            self.address,
            self.num_children,
            self.type.name,
        )


class CaseType(Base):
    __tablename__ = Config.CASES_TYPES_TABLE
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), nullable=False)

    cases = relationship("Case", back_populates="type")

    def __str__(self) -> str:
        return f"id: {self.id}, name: {self.name}"

    def toTuple(self) -> tuple:
        return (
            self.id,
            self.name,
        )


class Child(Base):
    __tablename__ = Config.CHILDREN_TABLE
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), nullable=False)
    national_id = sa.Column(sa.String(255), nullable=False)
    age = sa.Column(sa.Integer, nullable=False)
    case_id = sa.Column(sa.Integer, sa.ForeignKey("cases.id"), nullable=False)

    case = relationship("Case", back_populates="children")

    def __str__(self) -> str:
        return f"id: {self.id}, name: {self.name}, national_id: {self.national_id}, age: {self.age}, case_id: {self.case_id}"

    def toTuple(self) -> tuple:
        return (
            self.id,
            self.name,
            self.national_id,
            self.age,
            self.case_id,
        )


class Comment(Base):
    __tablename__ = Config.COMMENT_TABLE
    id = sa.Column(sa.Integer, primary_key=True)
    text = sa.Column(sa.String(255), nullable=False)
    case_id = sa.Column(sa.Integer, sa.ForeignKey("cases.id"), nullable=False)

    case = relationship("Case", back_populates="comments")

    def __str__(self) -> str:
        return f"id: {self.id}, text: {self.text}, case_id: {self.case_id}"

    def toTuple(self) -> tuple:
        return (
            self.id,
            self.text,
            self.case.name,
        )


class Invoice(Base):
    __tablename__ = Config.INVOICES_TABLE
    id = sa.Column(sa.Integer, primary_key=True)
    date = sa.Column(sa.String(255), nullable=False)
    item_type = sa.Column(sa.String(255), nullable=True)
    value = sa.Column(sa.Float, nullable=False)
    case_id = sa.Column(sa.Integer, sa.ForeignKey("cases.id"), nullable=False)
    item_id = sa.Column(sa.Integer, sa.ForeignKey("items.id"), nullable=True)

    case = relationship("Case", back_populates="invoice")
    item = relationship("Item", back_populates="invoice")

    def __str__(self) -> str:
        return f"id: {self.id}, date: {self.date}, value: {self.value}, item_type: {self.item_type}, case_id: {self.case_id}"

    def toTuple(self) -> tuple:
        return (
            self.id,
            self.date,
            self.item.name if self.item is not None else "",
            self.value,
            self.case.name,
        )


class Donations(Base):
    __tablename__ = Config.DONATIONS_TABLE
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), nullable=False)
    date = sa.Column(sa.String(255), nullable=False)
    value = sa.Column(sa.Float, nullable=True)
    item_id = sa.Column(sa.Integer, sa.ForeignKey("items.id"), nullable=True)
    donator_id = sa.Column(sa.Integer, sa.ForeignKey("donators.id"), nullable=True)

    donator = relationship("Donator", back_populates=Config.DONATIONS_TABLE)
    item = relationship("Item", back_populates="donation")

    def __str__(self) -> str:
        return f"id: {self.id}, name: {self.name}, value: {self.value}, date: {self.date}, value: {self.value}"

    def toTuple(self) -> tuple:
        return (
            self.id,
            self.name,
            self.date,
            self.value,
            self.item.name,
            self.donator.name,
        )


class Item(Base):
    __tablename__ = Config.ITEMS_TABLE
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), nullable=False)
    quantity = sa.Column(sa.Integer, nullable=False)
    unit = sa.Column(sa.String(255), nullable=False)
    price = sa.Column(sa.Float, nullable=True)

    invoice = relationship("Invoice", back_populates="item")
    donation = relationship("Donations", back_populates="item")

    def __str__(self) -> str:
        return f"id: {self.id}, name: {self.name}, unit: {self.unit}, quantity: {self.quantity}, price: {self.price}"

    def toTuple(self) -> tuple:
        return (
            self.id,
            self.name,
            self.quantity,
            self.unit,
            self.price,
            self.donation.donator.name,
        )


class Donator(Base):
    __tablename__ = Config.DONATOR_TABLE
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), nullable=False)
    national_id = sa.Column(sa.String(255), nullable=True)
    age = sa.Column(sa.Integer, nullable=False)
    phone_number = sa.Column(sa.String(255), nullable=True)
    address = sa.Column(sa.String(255), nullable=True)

    donations = relationship("Donations", back_populates="donator")

    def __str__(self) -> str:
        return f"id: {self.id}, name: {self.name}, national_id: {self.national_id}, age: {self.age}, phone_number: {self.phone_number}, address: {self.address}"

    def toTuple(self) -> tuple:
        return (
            self.id,
            self.name,
            self.national_id,
            self.age,
            self.phone_number,
            self.address,
            sum(self.donations.value),
        )
