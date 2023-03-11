from logic.data.database import Database


class DatabaseHelper:
    # TODO: getting by foreign keys is not working, fix it
    def __init__(self, db_url: str = "sqlite:///database.db"):
        self.database = Database(db_url)

    # * GET
    def get_all_users(self) -> list:
        return self.database.get_all("users")

    def get_user_by_id(self, user_id: int) -> dict:
        return self.database.get_by_id("users", user_id)

    def get_all_cases(self) -> list:
        return self.database.get_all("cases")

    def get_case_by_id(self, case_id: int) -> dict:
        return self.database.get_by_id("cases", case_id)

    def get_all_invoices(self) -> list:
        return self.database.get_all("invoices")

    def get_invoice_by_id(self, invoice_id: int) -> dict:
        return self.database.get_by_id("invoices", invoice_id)

    def get_invoices_by_type(self, invoice_type_id: str) -> dict:
        return self.database.get_by_id("invoices", invoice_type_id)

    def get_all_invoice_types(self) -> list:
        return self.database.get_all("invoice_types")

    def get_all_children(self) -> list:
        return self.database.get_all("child")

    def get_child_by_case_id(self, case_id: int) -> dict:
        return self.database.get_by_id("child", case_id)

    def get_all_comments(self) -> list:
        return self.database.get_all("comment")

    def get_comment_by_case_id(self, case_id: int) -> dict:
        return self.database.get_by_id("comment", case_id)

    def get_all_donations(self) -> list:
        return self.database.get_all("donate")

    # * INSERT
    def insert_user(self, data: dict) -> None:
        self.database.insert("users", data)

    def insert_case(self, data: dict) -> None:
        self.database.insert("cases", data)

    def insert_case_type(self, data: dict) -> None:
        self.database.insert("case_types", data)

    def insert_invoice(self, data: dict) -> None:
        self.database.insert("invoices", data)

    def insert_invoice_type(self, data: dict) -> None:
        self.database.insert("invoice_types", data)

    def insert_child(self, data: dict) -> None:
        self.database.insert("child", data)

    def insert_comment(self, data: dict) -> None:
        self.database.insert("comment", data)

    def insert_donate(self, data: dict) -> None:
        self.database.insert("donate", data)

    # * UPDATE
    def update_user(self, user_id: int, data: dict) -> None:
        self.database.update("users", user_id, data)

    def update_case(self, case_id: int, data: dict) -> None:
        self.database.update("cases", case_id, data)

    def update_invoice(self, invoice_id: int, data: dict) -> None:
        self.database.update("invoices", invoice_id, data)

    def update_invoice_type(self, invoice_type_id: int, data: dict) -> None:
        self.database.update("invoice_types", invoice_type_id, data)

    def update_child(self, case_id: int, data: dict) -> None:
        self.database.update("child", case_id, data)

    def update_comment(self, case_id: int, data: dict) -> None:
        self.database.update("comment", case_id, data)

    def update_donate(self, case_id: int, data: dict) -> None:
        self.database.update("donate", case_id, data)

    # * DELETE
    def delete_user(self, user_id: int) -> None:
        self.database.delete("users", user_id)

    def delete_case(self, case_id: int) -> None:
        self.database.delete("cases", case_id)

    def delete_case_type(self, case_type_id: int) -> None:
        self.database.delete("case_types", case_type_id)

    def delete_invoice(self, invoice_id: int) -> None:
        self.database.delete("invoices", invoice_id)

    def delete_invoice_type(self, invoice_type_id: int) -> None:
        self.database.delete("invoice_types", invoice_type_id)

    def delete_child(self, case_id: int) -> None:
        self.database.delete("child", case_id)

    def delete_comment(self, case_id: int) -> None:
        self.database.delete("comment", case_id)

    def delete_donate(self, case_id: int) -> None:
        self.database.delete("donate", case_id)
