# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cases_view.ui'
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
    QComboBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)
import src.interface.assets.resources


class Ui_Form(object):
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
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.nameFrame = QFrame(self.widgetFrame)
        self.nameFrame.setObjectName("nameFrame")
        self.nameFrame.setFrameShape(QFrame.StyledPanel)
        self.nameFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.nameFrame)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.nameEdit = QLineEdit(self.nameFrame)
        self.nameEdit.setObjectName("nameEdit")
        self.nameEdit.setMinimumSize(QSize(0, 0))
        self.nameEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.nameEdit, 0, Qt.AlignVCenter)

        self.nameLabel = QLabel(self.nameFrame)
        self.nameLabel.setObjectName("nameLabel")

        self.horizontalLayout_2.addWidget(self.nameLabel, 0, Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.nameFrame)

        self.iDFrame = QFrame(self.widgetFrame)
        self.iDFrame.setObjectName("iDFrame")
        self.iDFrame.setFrameShape(QFrame.StyledPanel)
        self.iDFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.iDFrame)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.iDEdit = QLineEdit(self.iDFrame)
        self.iDEdit.setObjectName("iDEdit")
        self.iDEdit.setMinimumSize(QSize(0, 0))
        self.iDEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.iDEdit, 0, Qt.AlignVCenter)

        self.iDLabel = QLabel(self.iDFrame)
        self.iDLabel.setObjectName("iDLabel")

        self.horizontalLayout_3.addWidget(self.iDLabel, 0, Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.iDFrame)

        self.ageFrame = QFrame(self.widgetFrame)
        self.ageFrame.setObjectName("ageFrame")
        self.ageFrame.setFrameShape(QFrame.StyledPanel)
        self.ageFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.ageFrame)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.ageEdit = QSpinBox(self.ageFrame)
        self.ageEdit.setObjectName("ageEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ageEdit.sizePolicy().hasHeightForWidth())
        self.ageEdit.setSizePolicy(sizePolicy)
        self.ageEdit.setMinimumSize(QSize(0, 0))
        self.ageEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.ageEdit, 0, Qt.AlignVCenter)

        self.ageLabel = QLabel(self.ageFrame)
        self.ageLabel.setObjectName("ageLabel")

        self.horizontalLayout_6.addWidget(self.ageLabel, 0, Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.ageFrame)

        self.addressFame = QFrame(self.widgetFrame)
        self.addressFame.setObjectName("addressFame")
        self.addressFame.setFrameShape(QFrame.StyledPanel)
        self.addressFame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.addressFame)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.addressEdit = QLineEdit(self.addressFame)
        self.addressEdit.setObjectName("addressEdit")
        self.addressEdit.setMinimumSize(QSize(0, 0))
        self.addressEdit.setInputMethodHints(Qt.ImhDigitsOnly)
        self.addressEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.addressEdit, 0, Qt.AlignVCenter)

        self.addressLabel = QLabel(self.addressFame)
        self.addressLabel.setObjectName("addressLabel")

        self.horizontalLayout_5.addWidget(self.addressLabel, 0, Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.addressFame)

        self.phoneFrame = QFrame(self.widgetFrame)
        self.phoneFrame.setObjectName("phoneFrame")
        self.phoneFrame.setFrameShape(QFrame.StyledPanel)
        self.phoneFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.phoneFrame)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.phoneEdit = QLineEdit(self.phoneFrame)
        self.phoneEdit.setObjectName("phoneEdit")
        self.phoneEdit.setMinimumSize(QSize(0, 0))
        self.phoneEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.phoneEdit, 0, Qt.AlignVCenter)

        self.phoneLabel = QLabel(self.phoneFrame)
        self.phoneLabel.setObjectName("phoneLabel")

        self.horizontalLayout_7.addWidget(self.phoneLabel, 0, Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.phoneFrame)

        self.caseFrame = QFrame(self.widgetFrame)
        self.caseFrame.setObjectName("caseFrame")
        self.caseFrame.setFrameShape(QFrame.StyledPanel)
        self.caseFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.caseFrame)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.caseEdit = QComboBox(self.caseFrame)
        self.caseEdit.setObjectName("caseEdit")
        sizePolicy.setHeightForWidth(self.caseEdit.sizePolicy().hasHeightForWidth())
        self.caseEdit.setSizePolicy(sizePolicy)
        self.caseEdit.setCursor(QCursor(Qt.PointingHandCursor))
        self.caseEdit.setMouseTracking(True)
        self.caseEdit.setLayoutDirection(Qt.LeftToRight)
        self.caseEdit.setStyleSheet("")

        self.horizontalLayout_4.addWidget(self.caseEdit)

        self.caseLabel = QLabel(self.caseFrame)
        self.caseLabel.setObjectName("caseLabel")

        self.horizontalLayout_4.addWidget(
            self.caseLabel, 0, Qt.AlignRight | Qt.AlignVCenter
        )

        self.verticalLayout.addWidget(self.caseFrame)

        self.childrenFrame = QFrame(self.widgetFrame)
        self.childrenFrame.setObjectName("childrenFrame")
        self.childrenFrame.setFrameShape(QFrame.StyledPanel)
        self.childrenFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.childrenFrame)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.saveButton = QPushButton(self.childrenFrame)
        self.saveButton.setObjectName("saveButton")
        self.saveButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(":/icons/icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.saveButton.setIcon(icon)

        self.horizontalLayout_8.addWidget(
            self.saveButton, 0, Qt.AlignLeft | Qt.AlignVCenter
        )

        self.childrenEdit = QSpinBox(self.childrenFrame)
        self.childrenEdit.setObjectName("childrenEdit")
        sizePolicy.setHeightForWidth(self.childrenEdit.sizePolicy().hasHeightForWidth())
        self.childrenEdit.setSizePolicy(sizePolicy)
        self.childrenEdit.setMinimumSize(QSize(0, 0))
        self.childrenEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.childrenEdit, 0, Qt.AlignVCenter)

        self.childrenLabel = QLabel(self.childrenFrame)
        self.childrenLabel.setObjectName("childrenLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.childrenLabel.sizePolicy().hasHeightForWidth()
        )
        self.childrenLabel.setSizePolicy(sizePolicy1)

        self.horizontalLayout_8.addWidget(self.childrenLabel, 0, Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.childrenFrame)

        self.horizontalLayout.addWidget(self.widgetFrame)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.nameLabel.setText(
            QCoreApplication.translate("Form", "\u0627\u0644\u0627\u0633\u0645", None)
        )
        self.iDEdit.setPlaceholderText("")
        self.iDLabel.setText(
            QCoreApplication.translate(
                "Form",
                "\u0627\u0644\u0631\u0642\u0645 \u0627\u0644\u0642\u0648\u0645\u064a",
                None,
            )
        )
        self.ageLabel.setText(
            QCoreApplication.translate("Form", "\u0627\u0644\u0633\u0646", None)
        )
        self.addressLabel.setText(
            QCoreApplication.translate(
                "Form", "\u0627\u0644\u0639\u0646\u0648\u0627\u0646", None
            )
        )
        self.phoneLabel.setText(
            QCoreApplication.translate(
                "Form", "\u0631\u0642\u0645 \u0627\u0644\u0647\u0627\u062a\u0641", None
            )
        )
        self.caseLabel.setText(
            QCoreApplication.translate(
                "Form", "\u0627\u0644\u062d\u0627\u0644\u0629", None
            )
        )
        self.saveButton.setText(
            QCoreApplication.translate("Form", "\u062d\u0641\u0638", None)
        )
        self.childrenLabel.setText(
            QCoreApplication.translate(
                "Form",
                "\u0639\u062f\u062f \u0627\u0644\u0623\u0648\u0644\u0627\u062f",
                None,
            )
        )

    # retranslateUi
