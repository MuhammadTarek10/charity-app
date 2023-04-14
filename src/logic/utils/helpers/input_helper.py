from src.logic.utils.helpers.storage_helper import StorageHelper


class InputHelper:
    @classmethod
    def validateNationalId(cls, id: str) -> bool:
        try:
            if (id[0] in ["2", "3"] or id[0] in ["٢", "٣"]) and len(id) == 14:
                return True
            else:
                return False
        except:
            return False

    @classmethod
    def validatePhoneNumber(cls, phoneNumber: str) -> bool:
        try:
            if (phoneNumber[0] == "0" or phoneNumber[0] == "٠") and len(
                phoneNumber
            ) == 11:
                return True
            else:
                return False
        except:
            return False

    @classmethod
    def validateMoney(cls, money: float) -> bool:
        storage = StorageHelper.getInstance()
        try:
            if float(money) <= storage.totalMoney():
                return True
            else:
                return False
        except:
            return False

    @classmethod
    def validateInvoice(cls, name: str, quantity: int) -> bool:
        storage = StorageHelper.getInstance()
        item = storage.getItemByName(name)
        if item is None:
            return False
        if int(quantity) > int(item.quantity):
            return False
        return True
