# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
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
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)

from Custom_Widgets.Widgets import QCustomSlideMenu
import src.interface.assets.resources


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 560)
        MainWindow.setStyleSheet(
            "*{\n"
            "	border: none;\n"
            "	background-color: #FFFFFF;\n"
            "	color: #000000;\n"
            "}\n"
            "\n"
            "QLabel{\n"
            "	color: #000000;\n"
            "}\n"
            "\n"
            "QPushButton{\n"
            "	background-color: #97DEFF;\n"
            "	border-radius: 5px;\n"
            "	border: 1px solid;\n"
            "\n"
            " }\n"
            "\n"
            "QPushButton:pressed{\n"
            "	background-color: #AA77FF;\n"
            "	border: 4px solid;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "	background-color: #62CDFF;\n"
            "}\n"
            "\n"
            "#sideMenuFrame{\n"
            "	border: 1px solid;\n"
            "	border-radius: 5px;\n"
            "}\n"
            "#mainBodyFrame{\n"
            "	background-color: #000000;\n"
            "	margin-right: 10px;\n"
            "	border-radius: 14px;\n"
            "}"
        )
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setLocale(QLocale(QLocale.Arabic, QLocale.Egypt))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName("header")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.titleFrame = QFrame(self.header)
        self.titleFrame.setObjectName("titleFrame")
        self.titleFrame.setFrameShape(QFrame.StyledPanel)
        self.titleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.titleFrame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.titleLabel = QLabel(self.titleFrame)
        self.titleLabel.setObjectName("titleLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.titleLabel)

        self.horizontalLayout.addWidget(self.titleFrame)

        self.menuFrame = QFrame(self.header)
        self.menuFrame.setObjectName("menuFrame")
        self.menuFrame.setFrameShape(QFrame.StyledPanel)
        self.menuFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.menuFrame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.menuButton = QPushButton(self.menuFrame)
        self.menuButton.setObjectName("menuButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.menuButton.sizePolicy().hasHeightForWidth())
        self.menuButton.setSizePolicy(sizePolicy1)
        self.menuButton.setMinimumSize(QSize(100, 0))
        self.menuButton.setMaximumSize(QSize(100, 16777215))
        font1 = QFont()
        font1.setFamilies(["Arial"])
        font1.setPointSize(20)
        self.menuButton.setFont(font1)
        self.menuButton.setCursor(QCursor(Qt.OpenHandCursor))
        self.menuButton.setLayoutDirection(Qt.LeftToRight)
        icon = QIcon()
        icon.addFile(":/icons/icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuButton.setIcon(icon)
        self.menuButton.setIconSize(QSize(16, 16))

        self.verticalLayout_3.addWidget(self.menuButton)

        self.horizontalLayout.addWidget(
            self.menuFrame, 0, Qt.AlignRight | Qt.AlignVCenter
        )

        self.verticalLayout.addWidget(self.header, 0, Qt.AlignTop)

        self.appFrame = QFrame(self.centralwidget)
        self.appFrame.setObjectName("appFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.appFrame.sizePolicy().hasHeightForWidth())
        self.appFrame.setSizePolicy(sizePolicy2)
        self.appFrame.setFrameShape(QFrame.StyledPanel)
        self.appFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.appFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mainBodyFrame = QFrame(self.appFrame)
        self.mainBodyFrame.setObjectName("mainBodyFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.mainBodyFrame.sizePolicy().hasHeightForWidth()
        )
        self.mainBodyFrame.setSizePolicy(sizePolicy3)
        self.mainBodyFrame.setFrameShape(QFrame.StyledPanel)
        self.mainBodyFrame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.mainBodyFrame)

        self.sideMenuFrame = QCustomSlideMenu(self.appFrame)
        self.sideMenuFrame.setObjectName("sideMenuFrame")
        sizePolicy2.setHeightForWidth(
            self.sideMenuFrame.sizePolicy().hasHeightForWidth()
        )
        self.sideMenuFrame.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamilies(["Arial"])
        font2.setPointSize(18)
        self.sideMenuFrame.setFont(font2)
        self.sideMenuFrame.setFrameShape(QFrame.StyledPanel)
        self.sideMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.sideMenuFrame)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.casesButton = QPushButton(self.sideMenuFrame)
        self.casesButton.setObjectName("casesButton")
        self.casesButton.setMaximumSize(QSize(16777215, 16777215))
        self.casesButton.setFont(font2)
        self.casesButton.setCursor(QCursor(Qt.OpenHandCursor))
        self.casesButton.setLocale(QLocale(QLocale.Arabic, QLocale.Egypt))
        icon1 = QIcon()
        icon1.addFile(":/icons/icons/case.png", QSize(), QIcon.Normal, QIcon.Off)
        self.casesButton.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.casesButton)

        self.donationsButton = QPushButton(self.sideMenuFrame)
        self.donationsButton.setObjectName("donationsButton")
        self.donationsButton.setFont(font2)
        self.donationsButton.setCursor(QCursor(Qt.OpenHandCursor))
        icon2 = QIcon()
        icon2.addFile(":/icons/icons/donation.png", QSize(), QIcon.Normal, QIcon.Off)
        self.donationsButton.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.donationsButton)

        self.invoicesButton = QPushButton(self.sideMenuFrame)
        self.invoicesButton.setObjectName("invoicesButton")
        self.invoicesButton.setFont(font2)
        self.invoicesButton.setCursor(QCursor(Qt.OpenHandCursor))
        icon3 = QIcon()
        icon3.addFile(":/icons/icons/money.png", QSize(), QIcon.Normal, QIcon.Off)
        self.invoicesButton.setIcon(icon3)

        self.verticalLayout_2.addWidget(self.invoicesButton)

        self.casesTypesButton = QPushButton(self.sideMenuFrame)
        self.casesTypesButton.setObjectName("casesTypesButton")
        self.casesTypesButton.setFont(font2)
        self.casesTypesButton.setCursor(QCursor(Qt.OpenHandCursor))
        icon4 = QIcon()
        icon4.addFile(":/icons/icons/types.png", QSize(), QIcon.Normal, QIcon.Off)
        self.casesTypesButton.setIcon(icon4)

        self.verticalLayout_2.addWidget(self.casesTypesButton)

        self.verticalSpacer = QSpacerItem(
            20, 2000, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.settingsFrame = QFrame(self.sideMenuFrame)
        self.settingsFrame.setObjectName("settingsFrame")
        sizePolicy2.setHeightForWidth(
            self.settingsFrame.sizePolicy().hasHeightForWidth()
        )
        self.settingsFrame.setSizePolicy(sizePolicy2)
        self.settingsFrame.setCursor(QCursor(Qt.ArrowCursor))
        self.settingsFrame.setFrameShape(QFrame.StyledPanel)
        self.settingsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.settingsFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 0, 0, 0)
        self.settingsButton = QPushButton(self.settingsFrame)
        self.settingsButton.setObjectName("settingsButton")
        self.settingsButton.setEnabled(True)
        self.settingsButton.setFont(font2)
        self.settingsButton.setCursor(QCursor(Qt.OpenHandCursor))
        icon5 = QIcon()
        icon5.addFile(":/icons/icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsButton.setIcon(icon5)

        self.verticalLayout_4.addWidget(self.settingsButton)

        self.verticalLayout_2.addWidget(self.settingsFrame, 0, Qt.AlignBottom)

        self.horizontalLayout_2.addWidget(self.sideMenuFrame, 0, Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.appFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.titleLabel.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u062c\u0645\u0639\u064a\u0629 \u0627\u0644\u0644\u064a \u062c\u064a \u0623\u062d\u0644\u0649",
                None,
            )
        )
        self.menuButton.setText(
            QCoreApplication.translate(
                "MainWindow", "\u0627\u0644\u0642\u0627\u0626\u0645\u0629", None
            )
        )
        self.casesButton.setText(
            QCoreApplication.translate(
                "MainWindow", "\u0627\u0644\u062d\u0627\u0644\u0627\u062a", None
            )
        )
        self.donationsButton.setText(
            QCoreApplication.translate(
                "MainWindow", "\u0627\u0644\u062a\u0628\u0631\u0639\u0627\u062a", None
            )
        )
        self.invoicesButton.setText(
            QCoreApplication.translate(
                "MainWindow", "\u0627\u0644\u0645\u0646\u0635\u0631\u0641", None
            )
        )
        self.casesTypesButton.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0627\u0646\u0648\u0627\u0639 \u0627\u0644\u062d\u0627\u0644\u0627\u062a",
                None,
            )
        )
        self.settingsButton.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0627\u0644\u0627\u0639\u062f\u0627\u062f\u0627\u062a",
                None,
            )
        )

    # retranslateUi
