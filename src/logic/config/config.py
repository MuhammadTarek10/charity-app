class Config:
    STYLE = [":/style/style.json"]

    DONATIONS_WIDGET = "DONATIONS_WIDGET"
    DONATIONS_WIDGET_INDEX = 0
    CASES_TYPES_WIDGET = "CASES_TYPES_WIDGET"
    CASES_TYPES_WIDGET_INDEX = 4
    INVOICES_WIDGET = "INVOICES_WIDGET"
    INVOICES_WIDGET_INDEX = 2
    CASES_WIDGET = "CASES_WIDGET"
    CASES_WIDGET_INDEX = 1
    STORAGE_WIDGET = "STORAGE_WIDGET"
    STORAGE_WIDGET_INDEX = 5

    widgetIndices = {
        DONATIONS_WIDGET: DONATIONS_WIDGET_INDEX,
        CASES_TYPES_WIDGET: CASES_TYPES_WIDGET_INDEX,
        INVOICES_WIDGET: INVOICES_WIDGET_INDEX,
        CASES_WIDGET: CASES_TYPES_WIDGET_INDEX,
        STORAGE_WIDGET: STORAGE_WIDGET_INDEX,
    }

    DATABASE_URL = "sqlite:///data.db"

    DONATOR_TABLE = "donators"

    CASES_TABLE = "cases"
    CASES_ID = "id"
    CASES_NAME = "name"
    CASES_NATIONAL_ID = "national_id"
    CASES_PHONE_NUMBER = "phone_number"
    CASES_AGE = "age"
    CASES_ADDRESS = "address"
    CASES_TYPE_ID = "type_id"
    CASES_NUM_CHILDREN = "num_children"

    CASES_TYPES_TABLE = "case_type"
    CASES_TYPES_ID = "id"
    CASES_TYPES_NAME = "name"

    INVOICES_TABLE = "invoices"

    INVOICES_TYPES_TABLE = "invoice_type"

    CHILDREN_TABLE = "children"

    COMMENT_TABLE = "comment"

    DONATE_TABLE = "donate"
    DONATE_ID = "id"
    DONATE_NAME = "name"
    DONATE_DATE = "date"
    DONATE_PRICE = "price"
    DONATE_QUANTITY = "quantity"
    DONATE_ITEM_TYPE = "item_type"
    DONATE_UNIT = "unit"
    DONATE_INVOICE_TYPE = "invoice_type_id"
    DONATE_DONATOR_ID = "donator_id"
    DONATE_VALUE = "value"