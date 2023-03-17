# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'storage_view.ui'
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
    QFrame,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QPushButton,
    QSizePolicy,
    QTableWidget,
    QTableWidgetItem,
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
        Form.setLayoutDirection(Qt.RightToLeft)
        Form.setStyleSheet("")
        Form.setLocale(QLocale(QLocale.Arabic, QLocale.Egypt))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widgetFrame = QFrame(Form)
        self.widgetFrame.setObjectName("widgetFrame")
        self.widgetFrame.setFrameShape(QFrame.StyledPanel)
        self.widgetFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.widgetFrame)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.storageFrame = QFrame(self.widgetFrame)
        self.storageFrame.setObjectName("storageFrame")
        self.storageFrame.setFrameShape(QFrame.StyledPanel)
        self.storageFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.storageFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.storageTableWidget = QTableWidget(self.storageFrame)
        self.storageTableWidget.setObjectName("storageTableWidget")

        self.verticalLayout_2.addWidget(self.storageTableWidget)

        self.verticalLayout.addWidget(self.storageFrame)

        self.totalPriceFrame = QFrame(self.widgetFrame)
        self.totalPriceFrame.setObjectName("totalPriceFrame")
        self.totalPriceFrame.setFrameShape(QFrame.StyledPanel)
        self.totalPriceFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.totalPriceFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.totalPriceLabel = QLabel(self.totalPriceFrame)
        self.totalPriceLabel.setObjectName("totalPriceLabel")
        self.totalPriceLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.totalPriceLabel)

        self.totalPriceValue = QLabel(self.totalPriceFrame)
        self.totalPriceValue.setObjectName("totalPriceValue")
        self.totalPriceValue.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.totalPriceValue)

        self.saveButton = QPushButton(self.totalPriceFrame)
        self.saveButton.setObjectName("saveButton")
        self.saveButton.setEnabled(False)
        self.saveButton.setLayoutDirection(Qt.LeftToRight)
        icon = QIcon()
        icon.addFile(":/icons/icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.saveButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.saveButton)

        self.verticalLayout.addWidget(self.totalPriceFrame)

        self.horizontalLayout.addWidget(self.widgetFrame)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.totalPriceLabel.setText(
            QCoreApplication.translate(
                "Form",
                "\u0627\u0644\u0645\u0628\u0644\u063a \u0627\u0644\u0643\u0644\u064a",
                None,
            )
        )
        self.totalPriceValue.setText(QCoreApplication.translate("Form", "0.0", None))
        self.saveButton.setText(
            QCoreApplication.translate("Form", "\u062d\u0641\u0638", None)
        )

    # retranslateUi
