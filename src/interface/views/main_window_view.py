# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_view.ui'
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
    QGroupBox,
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
        MainWindow.resize(860, 700)
        MainWindow.setMinimumSize(QSize(860, 0))
        MainWindow.setStyleSheet(
            "*{\n"
            "	border: none;\n"
            "	background-color: #FAFAFA;\n"
            "	color: #000000;\n"
            "	font-family: Arial;\n"
            "	font-size: 20px;\n"
            "	padding: 2px;\n"
            "}\n"
            "\n"
            "QLabel{\n"
            "	color: #000000;\n"
            "}\n"
            "\n"
            "#titleLabel{\n"
            "	font-size: 30px;\n"
            "}\n"
            "\n"
            "QPushButton{\n"
            "	background-color: #97DEFF;\n"
            "	border-radius: 5px;\n"
            "	border: 1px solid;\n"
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
            "QDateEdit{\n"
            "	background-color : #000000;\n"
            "	padding : 5px;\n"
            "	margin-right: 10px;\n"
            "}\n"
            "\n"
            "QDateEdit:up-arrow{\n"
            "	color: #000000;\n"
            "}\n"
            "\n"
            "QDateEdit:down-arrow{\n"
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
            "	border: 1px "
            "solid;\n"
            "	border-radius: 5px;\n"
            "}\n"
            "\n"
            "QSpinBox{\n"
            "	background-color: #C9EEFF;\n"
            "	border-radius: 5px;\n"
            "	border: 1px solid;\n"
            "	padding-left: 2px;\n"
            "	padding-right: 2px;\n"
            "}\n"
            "\n"
            "QSpinBox:focus{\n"
            "	background-color: #97DEFF;\n"
            "}\n"
            "\n"
            "QDoubleSpinBox{\n"
            "	background-color: #C9EEFF;\n"
            "	border-radius: 5px;\n"
            "	border: 1px solid;\n"
            "	padding-left: 2px;\n"
            "	padding-right: 2px;\n"
            "}\n"
            "\n"
            "QDoubleSpinBox:focus{\n"
            "	background-color: #97DEFF;\n"
            "}\n"
            "\n"
            "QListView{\n"
            "	border-radius: 5px;\n"
            "	border: 1px solid;\n"
            "	padding-left: 2px;\n"
            "	padding-right: 2px;\n"
            "}\n"
            "\n"
            "QListView:focus{\n"
            "	background-color: #97DEFF;\n"
            "}\n"
            "\n"
            "#sideMenuFrame{\n"
            "	border: 1px solid;\n"
            "	border-radius: 5px;\n"
            "}\n"
            "#mainBodyGroupBox{\n"
            "	margin-right: 10px;\n"
            "	border-radius: 5px;\n"
            "	border: 1px solid;\n"
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
            "#saveButton{\n"
            "	font-size: 18px;\n"
            "}\n"
            "\n"
            "#"
            "storageFrame{\n"
            "	border: 1px solid;\n"
            "	border-radius: 14px;\n"
            "}\n"
            "\n"
            "#QTableWidget{\n"
            "	color: #000000;\n"
            "	border: 1px solid;\n"
            "	border-radius: 14px;\n"
            "	padding: 8px;\n"
            "}\n"
            "\n"
            "QHeaderView{\n"
            "	border-radius: 5px;\n"
            "}\n"
            "\n"
            "QListWidget{\n"
            "	font-size: 12px;\n"
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
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.logoLabel = QLabel(self.titleFrame)
        self.logoLabel.setObjectName("logoLabel")
        self.logoLabel.setMaximumSize(QSize(50, 50))
        self.logoLabel.setPixmap(QPixmap(":/images/images/logo1.png"))
        self.logoLabel.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.logoLabel)

        self.titleLabel = QLabel(self.titleFrame)
        self.titleLabel.setObjectName("titleLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies(["Arial"])
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
        self.menuButton.setFont(font)
        self.menuButton.setCursor(QCursor(Qt.PointingHandCursor))
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
        self.mainBodyGroupBox = QGroupBox(self.appFrame)
        self.mainBodyGroupBox.setObjectName("mainBodyGroupBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.mainBodyGroupBox.sizePolicy().hasHeightForWidth()
        )
        self.mainBodyGroupBox.setSizePolicy(sizePolicy3)
        self.verticalLayout_6 = QVBoxLayout(self.mainBodyGroupBox)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setObjectName("mainLayout")

        self.verticalLayout_6.addLayout(self.mainLayout)

        self.horizontalLayout_2.addWidget(self.mainBodyGroupBox)

        self.sideMenuFrame = QCustomSlideMenu(self.appFrame)
        self.sideMenuFrame.setObjectName("sideMenuFrame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(
            self.sideMenuFrame.sizePolicy().hasHeightForWidth()
        )
        self.sideMenuFrame.setSizePolicy(sizePolicy4)
        self.sideMenuFrame.setMinimumSize(QSize(0, 0))
        self.sideMenuFrame.setFont(font)
        self.sideMenuFrame.setCursor(QCursor(Qt.ArrowCursor))
        self.sideMenuFrame.setFrameShape(QFrame.StyledPanel)
        self.sideMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.sideMenuFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 10, 0, 10)
        self.mainOptionsFrame = QFrame(self.sideMenuFrame)
        self.mainOptionsFrame.setObjectName("mainOptionsFrame")
        sizePolicy3.setHeightForWidth(
            self.mainOptionsFrame.sizePolicy().hasHeightForWidth()
        )
        self.mainOptionsFrame.setSizePolicy(sizePolicy3)
        self.mainOptionsFrame.setMinimumSize(QSize(0, 0))
        self.mainOptionsFrame.setFrameShape(QFrame.StyledPanel)
        self.mainOptionsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.mainOptionsFrame)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 0, 5, 0)
        self.donationsButton = QPushButton(self.mainOptionsFrame)
        self.donationsButton.setObjectName("donationsButton")
        self.donationsButton.setMinimumSize(QSize(0, 0))
        self.donationsButton.setFont(font)
        self.donationsButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(":/icons/icons/donation.png", QSize(), QIcon.Normal, QIcon.Off)
        self.donationsButton.setIcon(icon1)

        self.verticalLayout_5.addWidget(self.donationsButton)

        self.invoicesButton = QPushButton(self.mainOptionsFrame)
        self.invoicesButton.setObjectName("invoicesButton")
        self.invoicesButton.setMinimumSize(QSize(0, 0))
        self.invoicesButton.setFont(font)
        self.invoicesButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(":/icons/icons/money.png", QSize(), QIcon.Normal, QIcon.Off)
        self.invoicesButton.setIcon(icon2)

        self.verticalLayout_5.addWidget(self.invoicesButton)

        self.casesButton = QPushButton(self.mainOptionsFrame)
        self.casesButton.setObjectName("casesButton")
        self.casesButton.setMinimumSize(QSize(0, 0))
        self.casesButton.setMaximumSize(QSize(16777215, 16777215))
        self.casesButton.setFont(font)
        self.casesButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.casesButton.setLocale(QLocale(QLocale.Arabic, QLocale.Egypt))
        icon3 = QIcon()
        icon3.addFile(":/icons/icons/case.png", QSize(), QIcon.Normal, QIcon.Off)
        self.casesButton.setIcon(icon3)

        self.verticalLayout_5.addWidget(self.casesButton)

        self.casesTypesButton = QPushButton(self.mainOptionsFrame)
        self.casesTypesButton.setObjectName("casesTypesButton")
        self.casesTypesButton.setMinimumSize(QSize(0, 0))
        self.casesTypesButton.setFont(font)
        self.casesTypesButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(":/icons/icons/types.png", QSize(), QIcon.Normal, QIcon.Off)
        self.casesTypesButton.setIcon(icon4)

        self.verticalLayout_5.addWidget(self.casesTypesButton)

        self.storageButton = QPushButton(self.mainOptionsFrame)
        self.storageButton.setObjectName("storageButton")
        self.storageButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(":/icons/icons/storage.png", QSize(), QIcon.Normal, QIcon.Off)
        self.storageButton.setIcon(icon5)

        self.verticalLayout_5.addWidget(self.storageButton)

        self.verticalLayout_2.addWidget(self.mainOptionsFrame)

        self.spacerFrame = QFrame(self.sideMenuFrame)
        self.spacerFrame.setObjectName("spacerFrame")
        self.spacerFrame.setMinimumSize(QSize(0, 0))
        self.spacerFrame.setFrameShape(QFrame.StyledPanel)
        self.spacerFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.spacerFrame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalSpacer = QSpacerItem(
            20, 2000, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.horizontalLayout_3.addItem(self.verticalSpacer)

        self.verticalLayout_2.addWidget(self.spacerFrame)

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
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 0, 5, 0)
        self.settingsButton = QPushButton(self.settingsFrame)
        self.settingsButton.setObjectName("settingsButton")
        self.settingsButton.setEnabled(True)
        self.settingsButton.setMinimumSize(QSize(0, 0))
        self.settingsButton.setFont(font)
        self.settingsButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(":/icons/icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsButton.setIcon(icon6)

        self.verticalLayout_4.addWidget(self.settingsButton)

        self.aboutButton = QPushButton(self.settingsFrame)
        self.aboutButton.setObjectName("aboutButton")
        self.aboutButton.setMinimumSize(QSize(0, 0))
        self.aboutButton.setFont(font)
        self.aboutButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(":/icons/icons/about.png", QSize(), QIcon.Normal, QIcon.Off)
        self.aboutButton.setIcon(icon7)

        self.verticalLayout_4.addWidget(self.aboutButton)

        self.verticalLayout_2.addWidget(self.settingsFrame)

        self.horizontalLayout_2.addWidget(
            self.sideMenuFrame, 0, Qt.AlignHCenter | Qt.AlignVCenter
        )

        self.verticalLayout.addWidget(self.appFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.logoLabel.setText("")
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
        self.donationsButton.setText(
            QCoreApplication.translate("MainWindow", "\u062a\u0628\u0631\u0639", None)
        )
        self.invoicesButton.setText(
            QCoreApplication.translate("MainWindow", "\u0635\u0631\u0641", None)
        )
        self.casesButton.setText(
            QCoreApplication.translate(
                "MainWindow", "\u0627\u0644\u062d\u0627\u0644\u0627\u062a", None
            )
        )
        self.casesTypesButton.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0627\u0646\u0648\u0627\u0639 \u0627\u0644\u062d\u0627\u0644\u0627\u062a",
                None,
            )
        )
        self.storageButton.setText(
            QCoreApplication.translate(
                "MainWindow", "\u0627\u0644\u0645\u062e\u0632\u0646", None
            )
        )
        self.settingsButton.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0627\u0644\u0627\u0639\u062f\u0627\u062f\u0627\u062a",
                None,
            )
        )
        self.aboutButton.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0639\u0646 \u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c",
                None,
            )
        )

    # retranslateUi
