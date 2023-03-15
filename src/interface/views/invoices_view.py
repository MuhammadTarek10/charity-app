# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'invoices_view.ui'
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
    QCheckBox,
    QDateEdit,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)
import src.interface.assets.resources


class Ui_Form(QWidget):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(651, 595)
        Form.setMinimumSize(QSize(548, 548))
        Form.setStyleSheet("")
        Form.setLocale(QLocale(QLocale.Arabic, QLocale.Egypt))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widgetFrame = QFrame(Form)
        self.widgetFrame.setObjectName("widgetFrame")
        self.widgetFrame.setFrameShape(QFrame.StyledPanel)
        self.widgetFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.widgetFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.nameFrame = QFrame(self.widgetFrame)
        self.nameFrame.setObjectName("nameFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameFrame.sizePolicy().hasHeightForWidth())
        self.nameFrame.setSizePolicy(sizePolicy)
        self.nameFrame.setFrameShape(QFrame.StyledPanel)
        self.nameFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.nameFrame)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.nameEdit = QLineEdit(self.nameFrame)
        self.nameEdit.setObjectName("nameEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.nameEdit.sizePolicy().hasHeightForWidth())
        self.nameEdit.setSizePolicy(sizePolicy1)
        self.nameEdit.setMinimumSize(QSize(0, 0))
        self.nameEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.nameEdit)

        self.nameLabel = QLabel(self.nameFrame)
        self.nameLabel.setObjectName("nameLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.nameLabel.sizePolicy().hasHeightForWidth())
        self.nameLabel.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.nameLabel)

        self.verticalLayout.addWidget(self.nameFrame)

        self.priceFrame = QFrame(self.widgetFrame)
        self.priceFrame.setObjectName("priceFrame")
        self.priceFrame.setFrameShape(QFrame.StyledPanel)
        self.priceFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.priceFrame)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.priceEdit = QLineEdit(self.priceFrame)
        self.priceEdit.setObjectName("priceEdit")
        self.priceEdit.setMinimumSize(QSize(0, 0))
        self.priceEdit.setInputMethodHints(Qt.ImhDigitsOnly)
        self.priceEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.priceEdit)

        self.priceLabel = QLabel(self.priceFrame)
        self.priceLabel.setObjectName("priceLabel")

        self.horizontalLayout_4.addWidget(self.priceLabel)

        self.verticalLayout.addWidget(self.priceFrame)

        self.typeFrame = QFrame(self.widgetFrame)
        self.typeFrame.setObjectName("typeFrame")
        self.typeFrame.setFrameShape(QFrame.StyledPanel)
        self.typeFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.typeFrame)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.typeEdit = QLineEdit(self.typeFrame)
        self.typeEdit.setObjectName("typeEdit")
        self.typeEdit.setMinimumSize(QSize(0, 0))
        self.typeEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.typeEdit)

        self.typeLabel = QLabel(self.typeFrame)
        self.typeLabel.setObjectName("typeLabel")

        self.horizontalLayout_3.addWidget(self.typeLabel)

        self.verticalLayout.addWidget(self.typeFrame)

        self.unitFrame = QFrame(self.widgetFrame)
        self.unitFrame.setObjectName("unitFrame")
        self.unitFrame.setFrameShape(QFrame.StyledPanel)
        self.unitFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.unitFrame)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.unitEdit = QLineEdit(self.unitFrame)
        self.unitEdit.setObjectName("unitEdit")
        self.unitEdit.setMinimumSize(QSize(0, 0))
        self.unitEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.unitEdit)

        self.unitLabel = QLabel(self.unitFrame)
        self.unitLabel.setObjectName("unitLabel")

        self.horizontalLayout_6.addWidget(self.unitLabel)

        self.verticalLayout.addWidget(self.unitFrame)

        self.quantityFrame = QFrame(self.widgetFrame)
        self.quantityFrame.setObjectName("quantityFrame")
        self.quantityFrame.setFrameShape(QFrame.StyledPanel)
        self.quantityFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.quantityFrame)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.quantityEdit = QLineEdit(self.quantityFrame)
        self.quantityEdit.setObjectName("quantityEdit")
        self.quantityEdit.setMinimumSize(QSize(0, 0))
        self.quantityEdit.setInputMethodHints(Qt.ImhDigitsOnly)
        self.quantityEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.quantityEdit)

        self.quantityLabel = QLabel(self.quantityFrame)
        self.quantityLabel.setObjectName("quantityLabel")

        self.horizontalLayout_5.addWidget(self.quantityLabel)

        self.verticalLayout.addWidget(self.quantityFrame)

        self.dateFrame = QFrame(self.widgetFrame)
        self.dateFrame.setObjectName("dateFrame")
        self.dateFrame.setFrameShape(QFrame.StyledPanel)
        self.dateFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.dateFrame)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.saveButton = QPushButton(self.dateFrame)
        self.saveButton.setObjectName("saveButton")
        self.saveButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(":/icons/icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.saveButton.setIcon(icon)

        self.horizontalLayout_7.addWidget(self.saveButton, 0, Qt.AlignLeft)

        self.dateCheckBox = QCheckBox(self.dateFrame)
        self.dateCheckBox.setObjectName("dateCheckBox")
        self.dateCheckBox.setMaximumSize(QSize(200, 16777215))
        self.dateCheckBox.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_7.addWidget(self.dateCheckBox, 0, Qt.AlignLeft)

        self.dateEdit = QDateEdit(self.dateFrame)
        self.dateEdit.setObjectName("dateEdit")
        sizePolicy1.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy1)
        self.dateEdit.setMinimumSize(QSize(400, 0))
        self.dateEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.dateEdit)

        self.dateLabel = QLabel(self.dateFrame)
        self.dateLabel.setObjectName("dateLabel")

        self.horizontalLayout_7.addWidget(self.dateLabel)

        self.verticalLayout.addWidget(self.dateFrame)

        self.horizontalLayout.addWidget(self.widgetFrame)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.nameLabel.setText(
            QCoreApplication.translate("Form", "\u0627\u0644\u0627\u0633\u0645", None)
        )
        self.priceLabel.setText(
            QCoreApplication.translate(
                "Form",
                "\u0627\u0644\u0635\u0631\u0641 \u0627\u0644\u0646\u0642\u062f\u064a",
                None,
            )
        )
        self.typeEdit.setPlaceholderText(
            QCoreApplication.translate(
                "Form", "\u0642\u0645\u062d\u060c \u0642\u0645\u0627\u0634...", None
            )
        )
        self.typeLabel.setText(
            QCoreApplication.translate("Form", "\u0627\u0644\u0635\u0646\u0641", None)
        )
        self.unitEdit.setPlaceholderText(
            QCoreApplication.translate(
                "Form", "\u0643\u064a\u0644\u0648\u060c \u0645\u062a\u0631...", None
            )
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
        self.saveButton.setText(
            QCoreApplication.translate("Form", "\u062d\u0641\u0638", None)
        )
        self.dateCheckBox.setText(
            QCoreApplication.translate("Form", "\u0627\u0644\u0627\u0646", None)
        )
        self.dateLabel.setText(
            QCoreApplication.translate(
                "Form", "\u0627\u0644\u062a\u0627\u0631\u064a\u062e", None
            )
        )

    # retranslateUi
