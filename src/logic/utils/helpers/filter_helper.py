from typing import List
from src.logic.config.config import Config

from src.logic.data.models import *
from src.logic.utils.helpers.storage_helper import StorageHelper


class FilterHelper:
    @classmethod
    def getColumns(cls, value: str) -> list:
        key = cls.getTableIndex(value)
        match key:
            case Config.CASES_TYPES_WIDGET_INDEX:
                pass
            case Config.CASES_WIDGET_INDEX:
                pass
            case Config.DONATIONS_WIDGET_INDEX:
                pass
            case Config.INVOICES_WIDGET_INDEX:
                pass
            case Config.ITEMS_WIDGET_INDEX:
                pass
        return []

    @classmethod
    def getTableData(cls, value: str) -> list:
        result: List[Base] = []
        key = cls.getTableIndex(value)
        storage = StorageHelper()
        match key:
            case Config.CASES_TYPES_WIDGET_INDEX:
                result = storage.getAllCaseTypes()
            case Config.CASES_WIDGET_INDEX:
                result = storage.getAllCases()
            case Config.DONATIONS_WIDGET_INDEX:
                result = storage.getAllDonations()
            case Config.INVOICES_WIDGET_INDEX:
                result = storage.getAllInvoices()
            case Config.ITEMS_WIDGET_INDEX:
                pass
            case _:
                print("ERROR")
        return cls.extractResult(key, result)

    @classmethod
    def extractResult(cls, key: int, values: List[Base]) -> List[tuple]:
        cols = Config.COLUMNS[key]
        rows: List[tuple] = []
        for value in values:
            rows.append(value.toTuple())
        return cols, rows

    @classmethod
    def getTableIndex(cls, value: str) -> int:
        return list(Config.TABLES.keys())[list(Config.TABLES.values()).index(value)]
