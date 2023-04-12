class Config:
    STYLE = [":/style/style.json"]
    LOGO = ":/images/images/logo1.png"

    SELECTED_STYLE_BUTTON = """
    QPushButton{\n background-color: #90EE90;\n 
    border-radius: 5px;\n 
    border: 1px solid;\n}\n
    QPushButton:pressed{\n
    	background-color: #AA77FF;\n
    	border: 4px solid;\n
    }\n
    \n
    QPushButton:hover{\n
    	background-color: #90EE90;\n
    }\n"""
    UNSELECTED_STYLE_BUTTON = """
    QPushButton{\n background-color: #97DEFF;\n 
    border-radius: 5px;\n 
    border: 1px solid;\n}\n
    QPushButton:pressed{\n
    	background-color: #AA77FF;\n
    	border: 4px solid;\n
    }\n
    \n
    QPushButton:hover{\n
    	background-color: #62CDFF;\n
    }\n
    """

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
    ITEMS_WIDGET_INDEX = 6

    TABLES = {
        CASES_WIDGET_INDEX: "الحالات",
        CASES_TYPES_WIDGET_INDEX: "انواع الحالات",
        DONATIONS_WIDGET_INDEX: "التبرعات",
        INVOICES_WIDGET_INDEX: "المصروفات",
        ITEMS_WIDGET_INDEX: "الاغراض",
    }

    COLUMNS = {
        CASES_WIDGET_INDEX: (
            "الرقم التعريفي",
            "الاسم",
            "الرقم القومي",
            "رقم الهاتف",
            "السن",
            "العنوان",
            "الاطفال",
            "النوع",
        ),
        CASES_TYPES_WIDGET_INDEX: (
            "الرقم التعريفي",
            "الاسم",
        ),
        INVOICES_WIDGET_INDEX: (
            "الرقم التعريفي",
            "التاريخ",
            "الغرض",
            "القيمة",
            "الحالة",
        ),
        DONATIONS_WIDGET_INDEX: (
            "الرقم التعريفي",
            "الاسم",
            "التاريخ",
            "القيمة",
            "الصنف",
            "المتبرع",
        ),
        ITEMS_WIDGET_INDEX: (
            "الرقم التعريفي",
            "الاسم",
            "الكمية",
            "الوحدة",
            "السعر",
            "المتبرع",
        ),
    }

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
    INVOICES_ID = "id"
    INVOICES_DATE = "date"
    INVOICES_VALUE = "value"
    INVOICES_ITEM_ID = "item_id"
    INVOICES_CASE_ID = "case_id"
    INVOICES_INVOICE_TYPE_ID = "invoice_type_id"

    INVOICES_TYPES_TABLE = "invoice_type"

    CHILDREN_TABLE = "children"

    COMMENT_TABLE = "comment"

    DONATIONS_TABLE = "donations"
    DONATIONS_ID = "id"
    DONATION_NAME = "name"
    DONATION_DATE = "date"
    DONATIONS_PRICE = "price"
    DONATIONS_QUANTITY = "quantity"
    DONATIONS_ITEM_TYPE = "item_type"
    DONATIONS_UNIT = "unit"
    DONATIONS_INVOICE_TYPE = "invoice_type_id"
    DONATIONS_VALUE = "value"
    DONATIONS_DONATOR_ID = "donator_id"
    DONATIONS_ITEM_ID = "item_id"

    ITEMS_TABLE = "items"
    ITEMS_NAME = "name"
    ITEMS_PRICE = "price"
    ITEMS_UNIT = "unit"
    ITEMS_QUANTITY = "quantity"
