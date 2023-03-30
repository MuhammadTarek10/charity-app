# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'case_types_view.ui'
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
    QLabel,
    QLineEdit,
    QListView,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)
import src.interface.assets.resources


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(687, 583)
        Form.setStyleSheet("")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widgetFrame = QFrame(Form)
        self.widgetFrame.setObjectName("widgetFrame")
        self.widgetFrame.setFrameShape(QFrame.StyledPanel)
        self.widgetFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.widgetFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.editFrame = QFrame(self.widgetFrame)
        self.editFrame.setObjectName("editFrame")
        self.editFrame.setFrameShape(QFrame.StyledPanel)
        self.editFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.editFrame)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.saveButton = QPushButton(self.editFrame)
        self.saveButton.setObjectName("saveButton")
        self.saveButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(":/icons/icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.saveButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.saveButton)

        self.caseEdit = QLineEdit(self.editFrame)
        self.caseEdit.setObjectName("caseEdit")
        self.caseEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.caseEdit)

        self.caseLabel = QLabel(self.editFrame)
        self.caseLabel.setObjectName("caseLabel")

        self.horizontalLayout_2.addWidget(self.caseLabel)

        self.verticalLayout_2.addWidget(self.editFrame, 0, Qt.AlignTop)

        self.listFrame = QFrame(self.widgetFrame)
        self.listFrame.setObjectName("listFrame")
        self.listFrame.setFrameShape(QFrame.StyledPanel)
        self.listFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.listFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.listView = QListView(self.listFrame)
        self.listView.setObjectName("listView")
        self.listView.setLocale(QLocale(QLocale.Arabic, QLocale.Egypt))

        self.verticalLayout_3.addWidget(self.listView)

        self.verticalLayout_2.addWidget(self.listFrame)

        self.verticalLayout.addWidget(self.widgetFrame)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.saveButton.setText(
            QCoreApplication.translate("Form", "\u0627\u0636\u0627\u0641\u0629", None)
        )
        self.caseLabel.setText(
            QCoreApplication.translate(
                "Form", "\u0646\u0648\u0639 \u0627\u0644\u062d\u0627\u0644\u0629", None
            )
        )

    # retranslateUi
