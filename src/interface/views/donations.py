# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'donations.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QDateTimeEdit,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_Form(QWidget):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(576, 548)
        Form.setMinimumSize(QSize(576, 548))
        Form.setStyleSheet(
            "*{\n"
            "	border: none;\n"
            "	background-color: #FFFFFF;\n"
            "	color: #000000;\n"
            "}\n"
            "\n"
            "#labelsFrame{\n"
            "	border-radius: 5px;\n"
            "}\n"
            "\n"
            "#valuesFrame{\n"
            "	border-radius: 8px;\n"
            "}\n"
            "\n"
            "QDateTimeEdit{\n"
            "	background-color : #000000;\n"
            "	padding : 5px;\n"
            "	margin-right: 5px;\n"
            "}\n"
            "\n"
            "QDateTimeEdit:up-arrow{\n"
            "	color: #000000;\n"
            "}\n"
            "\n"
            "QDateTimeEdit:down-arrow{\n"
            "	color: #000000;\n"
            "}\n"
            "\n"
            "\n"
            "QLineEdit{\n"
            "	background-color: #C9EEFF;\n"
            "	border-radius: 5px;\n"
            "	border: 1px solid;\n"
            "	padding-left: 2px;\n"
            "	padding-right: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit:focus{\n"
            "	background-color: #97DEFF;\n"
            "}\n"
            "\n"
            "QDateTimeEdit{\n"
            "	background-color: #C9EEFF;\n"
            "	border-radius: 5px;\n"
            "	border: 1px solid;\n"
            "}\n"
            "\n"
            "QPushButton{\n"
            "	background-color: #97DEFF;\n"
            "	border-radius: 5px;\n"
            "	border: 1px solid;\n"
            "}\n"
            "QPushButton:pressed{\n"
            "	background-color: #AA77FF;\n"
            "	border: 4px solid;\n"
            "}\n"
            "QPushButton:hover{\n"
            "	background-color: #62CDFF;\n"
            "}"
        )
        Form.setLocale(QLocale(QLocale.Arabic, QLocale.Egypt))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.windowFrame = QFrame(Form)
        self.windowFrame.setObjectName("windowFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.windowFrame.sizePolicy().hasHeightForWidth())
        self.windowFrame.setSizePolicy(sizePolicy)
        self.windowFrame.setMinimumSize(QSize(50, 0))
        self.windowFrame.setFrameShape(QFrame.StyledPanel)
        self.windowFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.windowFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.valuesFrame = QFrame(self.windowFrame)
        self.valuesFrame.setObjectName("valuesFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.valuesFrame.sizePolicy().hasHeightForWidth())
        self.valuesFrame.setSizePolicy(sizePolicy1)
        self.valuesFrame.setMinimumSize(QSize(0, 500))
        self.valuesFrame.setFrameShape(QFrame.StyledPanel)
        self.valuesFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.valuesFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 5, 10)
        self.editFrame = QFrame(self.valuesFrame)
        self.editFrame.setObjectName("editFrame")
        sizePolicy.setHeightForWidth(self.editFrame.sizePolicy().hasHeightForWidth())
        self.editFrame.setSizePolicy(sizePolicy)
        self.editFrame.setMinimumSize(QSize(0, 0))
        self.editFrame.setFrameShape(QFrame.StyledPanel)
        self.editFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.editFrame)
        self.verticalLayout_3.setSpacing(30)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 0, 5, -1)
        self.nameEdit = QLineEdit(self.editFrame)
        self.nameEdit.setObjectName("nameEdit")
        sizePolicy.setHeightForWidth(self.nameEdit.sizePolicy().hasHeightForWidth())
        self.nameEdit.setSizePolicy(sizePolicy)
        self.nameEdit.setMinimumSize(QSize(0, 40))
        self.nameEdit.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_3.addWidget(self.nameEdit)

        self.typeEdit = QLineEdit(self.editFrame)
        self.typeEdit.setObjectName("typeEdit")
        sizePolicy.setHeightForWidth(self.typeEdit.sizePolicy().hasHeightForWidth())
        self.typeEdit.setSizePolicy(sizePolicy)
        self.typeEdit.setMinimumSize(QSize(0, 40))
        self.typeEdit.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_3.addWidget(self.typeEdit)

        self.valueEdit = QLineEdit(self.editFrame)
        self.valueEdit.setObjectName("valueEdit")
        sizePolicy.setHeightForWidth(self.valueEdit.sizePolicy().hasHeightForWidth())
        self.valueEdit.setSizePolicy(sizePolicy)
        self.valueEdit.setMinimumSize(QSize(0, 40))
        self.valueEdit.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_3.addWidget(self.valueEdit)

        self.donationTypeEdit = QLineEdit(self.editFrame)
        self.donationTypeEdit.setObjectName("donationTypeEdit")
        sizePolicy.setHeightForWidth(
            self.donationTypeEdit.sizePolicy().hasHeightForWidth()
        )
        self.donationTypeEdit.setSizePolicy(sizePolicy)
        self.donationTypeEdit.setMinimumSize(QSize(0, 40))
        self.donationTypeEdit.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_3.addWidget(self.donationTypeEdit)

        self.quantityEdit = QLineEdit(self.editFrame)
        self.quantityEdit.setObjectName("quantityEdit")
        sizePolicy.setHeightForWidth(self.quantityEdit.sizePolicy().hasHeightForWidth())
        self.quantityEdit.setSizePolicy(sizePolicy)
        self.quantityEdit.setMinimumSize(QSize(0, 40))
        self.quantityEdit.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_3.addWidget(self.quantityEdit)

        self.unitEdit = QLineEdit(self.editFrame)
        self.unitEdit.setObjectName("unitEdit")
        sizePolicy.setHeightForWidth(self.unitEdit.sizePolicy().hasHeightForWidth())
        self.unitEdit.setSizePolicy(sizePolicy)
        self.unitEdit.setMinimumSize(QSize(0, 40))
        self.unitEdit.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_3.addWidget(self.unitEdit)

        self.priceEdit = QLineEdit(self.editFrame)
        self.priceEdit.setObjectName("priceEdit")
        self.priceEdit.setEnabled(False)
        sizePolicy.setHeightForWidth(self.priceEdit.sizePolicy().hasHeightForWidth())
        self.priceEdit.setSizePolicy(sizePolicy)
        self.priceEdit.setMinimumSize(QSize(0, 40))
        self.priceEdit.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_3.addWidget(self.priceEdit)

        self.totalPriceEdit = QLabel(self.editFrame)
        self.totalPriceEdit.setObjectName("totalPriceEdit")
        self.totalPriceEdit.setMinimumSize(QSize(0, 40))
        self.totalPriceEdit.setMaximumSize(QSize(16777215, 10))
        font = QFont()
        font.setFamilies(["Arial"])
        font.setPointSize(20)
        font.setBold(True)
        self.totalPriceEdit.setFont(font)
        self.totalPriceEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.totalPriceEdit)

        self.verticalLayout_2.addWidget(self.editFrame)

        self.dateFrame = QFrame(self.valuesFrame)
        self.dateFrame.setObjectName("dateFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.dateFrame.sizePolicy().hasHeightForWidth())
        self.dateFrame.setSizePolicy(sizePolicy2)
        self.dateFrame.setMinimumSize(QSize(0, 66))
        self.dateFrame.setStyleSheet("")
        self.dateFrame.setFrameShape(QFrame.StyledPanel)
        self.dateFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.dateFrame)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 0, 5, 0)
        self.timeNowButton = QPushButton(self.dateFrame)
        self.timeNowButton.setObjectName("timeNowButton")
        sizePolicy.setHeightForWidth(
            self.timeNowButton.sizePolicy().hasHeightForWidth()
        )
        self.timeNowButton.setSizePolicy(sizePolicy)
        self.timeNowButton.setMinimumSize(QSize(70, 40))
        self.timeNowButton.setMaximumSize(QSize(70, 40))
        font1 = QFont()
        font1.setFamilies(["Arial"])
        font1.setPointSize(13)
        self.timeNowButton.setFont(font1)
        self.timeNowButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.timeNowButton)

        self.dateTimeEdit = QDateTimeEdit(self.dateFrame)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        sizePolicy.setHeightForWidth(self.dateTimeEdit.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit.setSizePolicy(sizePolicy)
        self.dateTimeEdit.setMinimumSize(QSize(0, 40))
        self.dateTimeEdit.setMaximumSize(QSize(16777215, 40))
        self.dateTimeEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.dateTimeEdit)

        self.verticalLayout_2.addWidget(self.dateFrame, 0, Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.valuesFrame)

        self.labelsFrame = QFrame(self.windowFrame)
        self.labelsFrame.setObjectName("labelsFrame")
        self.labelsFrame.setFrameShape(QFrame.StyledPanel)
        self.labelsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.labelsFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(5, 0, 5, 0)
        self.nameLabel = QLabel(self.labelsFrame)
        self.nameLabel.setObjectName("nameLabel")
        font2 = QFont()
        font2.setFamilies(["Arial"])
        font2.setPointSize(18)
        self.nameLabel.setFont(font2)

        self.verticalLayout.addWidget(self.nameLabel)

        self.typeLabel = QLabel(self.labelsFrame)
        self.typeLabel.setObjectName("typeLabel")
        self.typeLabel.setFont(font2)

        self.verticalLayout.addWidget(self.typeLabel)

        self.valueLabel = QLabel(self.labelsFrame)
        self.valueLabel.setObjectName("valueLabel")
        self.valueLabel.setFont(font2)

        self.verticalLayout.addWidget(self.valueLabel)

        self.donationTypeLabel = QLabel(self.labelsFrame)
        self.donationTypeLabel.setObjectName("donationTypeLabel")
        self.donationTypeLabel.setFont(font2)

        self.verticalLayout.addWidget(self.donationTypeLabel)

        self.unitLabel = QLabel(self.labelsFrame)
        self.unitLabel.setObjectName("unitLabel")
        self.unitLabel.setFont(font2)

        self.verticalLayout.addWidget(self.unitLabel)

        self.quantityLabel = QLabel(self.labelsFrame)
        self.quantityLabel.setObjectName("quantityLabel")
        self.quantityLabel.setFont(font2)

        self.verticalLayout.addWidget(self.quantityLabel)

        self.priceLabel = QLabel(self.labelsFrame)
        self.priceLabel.setObjectName("priceLabel")
        self.priceLabel.setFont(font2)

        self.verticalLayout.addWidget(self.priceLabel)

        self.totalPriceLabel = QLabel(self.labelsFrame)
        self.totalPriceLabel.setObjectName("totalPriceLabel")
        self.totalPriceLabel.setFont(font2)

        self.verticalLayout.addWidget(self.totalPriceLabel)

        self.dateLabel = QLabel(self.labelsFrame)
        self.dateLabel.setObjectName("dateLabel")
        self.dateLabel.setFont(font2)

        self.verticalLayout.addWidget(self.dateLabel)

        self.horizontalLayout_2.addWidget(self.labelsFrame)

        self.horizontalLayout.addWidget(self.windowFrame)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.totalPriceEdit.setText(QCoreApplication.translate("Form", "0.0", None))
        self.timeNowButton.setText(
            QCoreApplication.translate(
                "Form", "\u0627\u0644\u0648\u0642\u062a \u0627\u0644\u0622\u0646", None
            )
        )
        self.nameLabel.setText(
            QCoreApplication.translate("Form", "\u0627\u0644\u0627\u0633\u0645", None)
        )
        self.typeLabel.setText(
            QCoreApplication.translate(
                "Form", "\u0646\u0648\u0639 \u0627\u0644\u062a\u0628\u0631\u0639", None
            )
        )
        self.valueLabel.setText(
            QCoreApplication.translate(
                "Form",
                "\u0642\u064a\u0645\u0629 \u0627\u0644\u062a\u0628\u0631\u0639",
                None,
            )
        )
        self.donationTypeLabel.setText(
            QCoreApplication.translate("Form", "\u0627\u0644\u0635\u0646\u0641", None)
        )
        self.unitLabel.setText(
            QCoreApplication.translate(
                "Form", "\u0627\u0644\u0648\u062d\u062f\u0629", None
            )
        )
        self.quantityLabel.setText(
            QCoreApplication.translate(
                "Form", "\u0627\u0644\u0643\u0645\u064a\u0629", None
            )
        )
        self.priceLabel.setText(
            QCoreApplication.translate("Form", "\u0627\u0644\u0633\u0639\u0631", None)
        )
        self.totalPriceLabel.setText(
            QCoreApplication.translate(
                "Form", "\u0627\u0644\u0642\u064a\u0645\u0629", None
            )
        )
        self.dateLabel.setText(
            QCoreApplication.translate(
                "Form", "\u0627\u0644\u062a\u0627\u0631\u064a\u062e", None
            )
        )

    # retranslateUi
