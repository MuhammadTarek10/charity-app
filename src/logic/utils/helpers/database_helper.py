from src.logic.data.database import Database
from src.logic.config.config import Config


class DatabaseHelper:
    # TODO: getting by foreign keys is not working, fix it
    def __init__(self, db_url: str = Config.DATABASE_URL):
        self.database = Database(db_url)

    # * GET
    def get_all_users(self) -> list:
        return self.database.get_all(Config.USERS_TABLE)

    def get_user_by_id(self, user_id: int) -> dict:
        return self.database.get_by_id(Config.USERS_TABLE, user_id)

    def get_all_cases(self) -> list:
        return self.database.get_all(Config.CASES_TABLE)

    def get_case_by_id(self, case_id: int) -> dict:
        return self.database.get_by_id(Config.CASES_TABLE, case_id)

    def get_all_invoices(self) -> list:
        return self.database.get_all(Config.INVOICES_TABLE)

    def get_invoice_by_id(self, invoice_id: int) -> dict:
        return self.database.get_by_id(Config.INVOICES_TABLE, invoice_id)

    def get_invoices_by_type(self, invoice_type_id: str) -> dict:
        return self.database.get_by_id(Config.INVOICES_TABLE, invoice_type_id)

    def get_all_invoice_types(self) -> list:
        return self.database.get_all(Config.INVOICES_TYPES_TABLE)

    def get_all_children(self) -> list:
        return self.database.get_all(Config.CHILDREN_TABLE)

    def get_child_by_case_id(self, case_id: int) -> dict:
        return self.database.get_by_id(Config.CHILDREN_TABLE, case_id)

    def get_all_comments(self) -> list:
        return self.database.get_all(Config.COMMENT_TABLE)

    def get_comment_by_case_id(self, case_id: int) -> dict:
        return self.database.get_by_id(Config.COMMENT_TABLE, case_id)

    def get_all_donations(self) -> list:
        return self.database.get_all(Config.DONATE_TABLE)

    # * INSERT
    def insert_user(self, data: dict) -> None:
        self.database.insert(Config.USERS_TABLE, data)

    def insert_case(self, data: dict) -> None:
        self.database.insert(Config.CASES_TABLE, data)

    def insert_case_type(self, data: dict) -> None:
        self.database.insert("case_types", data)

    def insert_invoice(self, data: dict) -> None:
        self.database.insert(Config.INVOICES_TABLE, data)

    def insert_invoice_type(self, data: dict) -> None:
        self.database.insert(Config.INVOICES_TYPES_TABLE, data)

    def insert_child(self, data: dict) -> None:
        self.database.insert(Config.CHILDREN_TABLE, data)

    def insert_comment(self, data: dict) -> None:
        self.database.insert(Config.COMMENT_TABLE, data)

    def insert_donate(self, data: dict) -> None:
        self.database.insert(Config.DONATE_TABLE, data)

    # * UPDATE
    def update_user(self, user_id: int, data: dict) -> None:
        self.database.update(Config.USERS_TABLE, user_id, data)

    def update_case(self, case_id: int, data: dict) -> None:
        self.database.update(Config.CASES_TABLE, case_id, data)

    def update_invoice(self, invoice_id: int, data: dict) -> None:
        self.database.update(Config.INVOICES_TABLE, invoice_id, data)

    def update_invoice_type(self, invoice_type_id: int, data: dict) -> None:
        self.database.update(Config.INVOICES_TYPES_TABLE, invoice_type_id, data)

    def update_child(self, case_id: int, data: dict) -> None:
        self.database.update(Config.CHILDREN_TABLE, case_id, data)

    def update_comment(self, case_id: int, data: dict) -> None:
        self.database.update(Config.COMMENT_TABLE, case_id, data)

    def update_donate(self, case_id: int, data: dict) -> None:
        self.database.update(Config.DONATE_TABLE, case_id, data)

    # * DELETE
    def delete_user(self, user_id: int) -> None:
        self.database.delete(Config.USERS_TABLE, user_id)

    def delete_case(self, case_id: int) -> None:
        self.database.delete(Config.CASES_TABLE, case_id)

    def delete_case_type(self, case_type_id: int) -> None:
        self.database.delete("case_types", case_type_id)

    def delete_invoice(self, invoice_id: int) -> None:
        self.database.delete(Config.INVOICES_TABLE, invoice_id)

    def delete_invoice_type(self, invoice_type_id: int) -> None:
        self.database.delete(Config.INVOICES_TYPES_TABLE, invoice_type_id)

    def delete_child(self, case_id: int) -> None:
        self.database.delete(Config.CHILDREN_TABLE, case_id)

    def delete_comment(self, case_id: int) -> None:
        self.database.delete(Config.COMMENT_TABLE, case_id)

    def delete_donate(self, case_id: int) -> None:
        self.database.delete(Config.DONATE_TABLE, case_id)
