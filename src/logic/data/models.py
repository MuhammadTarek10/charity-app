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

    def toJson(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "national_id": self.national_id,
            "phone_number": self.phone_number,
            "age": self.age,
            "address": self.address,
            "type_id": self.type_id,
        }

    def fromJson(self, json: dict) -> None:
        self.name = json["name"]
        self.national_id = json["national_id"]
        self.phone_number = json["phone_number"]
        self.age = json["age"]
        self.address = json["address"]
        self.type_id = json["type_id"]


class CaseType(Base):
    __tablename__ = Config.CASES_TYPES_TABLE
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), nullable=False)

    cases = relationship("Case", back_populates="type")

    def toJson(self) -> dict:
        return {"id": self.id, "name": self.name}

    def fromJson(self, json: dict) -> None:
        self.name = json["name"]


class Child(Base):
    __tablename__ = Config.CHILDREN_TABLE
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), nullable=False)
    national_id = sa.Column(sa.String(255), nullable=False)
    age = sa.Column(sa.Integer, nullable=False)
    case_id = sa.Column(sa.Integer, sa.ForeignKey("cases.id"), nullable=False)

    case = relationship("Case", back_populates="children")

    def __init__(self, data: dict) -> None:
        super().__init__()
        self.fromJson(data)

    def toJson(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "national_id": self.national_id,
            "age": self.age,
            "case_id": self.case_id,
        }

    def fromJson(self, json: dict) -> None:
        self.name = json["name"]
        self.national_id = json["national_id"]
        self.age = json["age"]
        self.case_id = json["case_id"]


class Comment(Base):
    __tablename__ = Config.COMMENT_TABLE
    id = sa.Column(sa.Integer, primary_key=True)
    text = sa.Column(sa.String(255), nullable=False)
    case_id = sa.Column(sa.Integer, sa.ForeignKey("cases.id"), nullable=False)

    case = relationship("Case", back_populates="comments")

    def __init__(self, data: dict) -> None:
        super().__init__()
        self.fromJson(data)

    def toJson(self) -> dict:
        return {"id": self.id, "text": self.text, "case_id": self.case_id}

    def fromJson(self, json: dict) -> None:
        self.text = json["text"]
        self.case_id = json["case_id"]


class Invoice(Base):
    __tablename__ = Config.INVOICES_TABLE
    id = sa.Column(sa.Integer, primary_key=True)
    date = sa.Column(sa.Date, nullable=False)
    price = sa.Column(sa.Integer, nullable=False)
    quantity = sa.Column(sa.Integer, nullable=False)
    item_type = sa.Column(sa.String(255), nullable=False)
    unit = sa.Column(sa.String(255), nullable=False)
    case_id = sa.Column(sa.Integer, sa.ForeignKey("cases.id"), nullable=False)
    invoice_type_id = sa.Column(
        sa.Integer, sa.ForeignKey("invoice_type.id"), nullable=False
    )

    invoice_type = relationship("InvoiceType", back_populates="invoices")
    case = relationship("Case", back_populates="invoice")

    def __init__(self, data: dict) -> None:
        super().__init__()
        self.fromJson(data)

    def toJson(self) -> dict:
        return {
            "id": self.id,
            "date": self.date,
            "price": self.price,
            "quantity": self.quantity,
            "item_type": self.item_type,
            "unit": self.unit,
            "case_id": self.case_id,
            "invoice_type_id": self.invoice_type_id,
        }

    def fromJson(self, json: dict) -> None:
        self.date = json["date"]
        self.price = json["price"]
        self.quantity = json["quantity"]
        self.item_type = json["item_type"]
        self.unit = json["unit"]
        self.case_id = json["case_id"]
        self.invoice_type_id = json["invoice_type_id"]


class InvoiceType(Base):
    __tablename__ = Config.INVOICES_TYPES_TABLE
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), nullable=False)

    invoices = relationship("Invoice", back_populates="invoice_type")
    donates = relationship("Donate", back_populates="invoice_type")

    def __init__(self, data: dict) -> None:
        super().__init__()
        self.fromJson(data)

    def toJson(self) -> dict:
        return {"id": self.id, "name": self.name}

    def fromJson(self, json: dict) -> None:
        self.name = json["name"]


class Donate(Base):
    __tablename__ = Config.DONATE_TABLE
    id = sa.Column(sa.Integer, primary_key=True)
    date = sa.Column(sa.Date, nullable=False)
    price = sa.Column(sa.Integer, nullable=False)
    quantity = sa.Column(sa.Integer, nullable=False)
    item_type = sa.Column(sa.String(255), nullable=False)
    unit = sa.Column(sa.String(255), nullable=False)
    invoice_type_id = sa.Column(
        sa.Integer, sa.ForeignKey("invoice_type.id"), nullable=False
    )
    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"), nullable=False)

    invoice_type = relationship("InvoiceType", back_populates="donates")
    user = relationship("User", back_populates="donations")

    def __init__(self, data: dict) -> None:
        super().__init__()
        self.fromJson(data)

    def toJson(self) -> dict:
        return {
            "id": self.id,
            "date": self.date,
            "price": self.price,
            "quantity": self.quantity,
            "item_type": self.item_type,
            "unit": self.unit,
            "invoice_type_id": self.invoice_type_id,
            "user_id": self.user_id,
        }

    def fromJson(self, json: dict) -> None:
        self.date = json["date"]
        self.price = json["price"]
        self.quantity = json["quantity"]
        self.item_type = json["item_type"]
        self.unit = json["unit"]
        self.invoice_type_id = json["invoice_type_id"]
        self.user_id = json["user_id"]


class User(Base):
    __tablename__ = Config.USERS_TABLE
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), nullable=False)
    national_id = sa.Column(sa.String(255), nullable=True)
    age = sa.Column(sa.Integer, nullable=False)
    phone_number = sa.Column(sa.String(255), nullable=True)
    address = sa.Column(sa.String(255), nullable=True)

    donations = relationship("Donate", back_populates="user")

    def __init__(self, data: dict) -> None:
        super().__init__()
        self.fromJson(data)

    def toJson(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "national_id": self.national_id,
            "age": self.age,
            "phone_number": self.phone_number,
            "address": self.address,
        }

    def fromJson(self, json: dict) -> None:
        self.name = json["name"]
        self.national_id = json["national_id"]
        self.age = json["age"]
        self.phone_number = json["phone_number"]
        self.address = json["address"]
