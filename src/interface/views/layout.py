# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'layout.ui'
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
    QVBoxLayout,
    QWidget,
)

from Custom_Widgets.Widgets import QCustomSlideMenu
import src.interface.assets.resources


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 662)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet(
            "*{\n"
            "	border: none;\n"
            "	background-color: transparent;\n"
            "	color: #FFFFFF;\n"
            "}\n"
            "#centralwidget{\n"
            "	background-color: #040F13;\n"
            "}\n"
            "#sideMenu{\n"
            "	background-color: #071E26;\n"
            "	border-radius: 20px;\n"
            "}\n"
            "#mainBody{\n"
            "	background-color: #071E26;\n"
            "	border-radius: 10px;\n"
            "}\n"
            "QPushButton{\n"
            "	padding: 10px;\n"
            "	background-color: #040F13;\n"
            "	border-radius: 4px;\n"
            "}\n"
            ""
        )
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName("header")
        self.header.setMinimumSize(QSize(0, 70))
        self.header.setMaximumSize(QSize(16777215, 70))
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.header)
        self.frame.setObjectName("frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menuButton = QPushButton(self.frame)
        self.menuButton.setObjectName("menuButton")
        self.menuButton.setMinimumSize(QSize(0, 30))
        self.menuButton.setMaximumSize(QSize(16777215, 30))
        icon = QIcon()
        icon.addFile(
            ":/icons/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off
        )
        self.menuButton.setIcon(icon)
        self.menuButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.menuButton)

        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignLeft)

        self.frame_3 = QFrame(self.header)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName("label")
        font = QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.horizontalLayout_2.addWidget(self.frame_3)

        self.verticalLayout.addWidget(self.header, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName("frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sideMenu = QCustomSlideMenu(self.frame_2)
        self.sideMenu.setObjectName("sideMenu")
        sizePolicy.setHeightForWidth(self.sideMenu.sizePolicy().hasHeightForWidth())
        self.sideMenu.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.sideMenu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.sideMenu)
        self.frame_4.setObjectName("frame_4")
        self.frame_4.setMinimumSize(QSize(150, 0))
        self.frame_4.setMaximumSize(QSize(150, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName("pushButton_2")
        icon1 = QIcon()
        icon1.addFile(":/icons/icons/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName("pushButton_4")

        self.verticalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_4)
        self.pushButton_5.setObjectName("pushButton_5")

        self.verticalLayout_3.addWidget(self.pushButton_5)

        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName("pushButton_3")

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.verticalLayout_2.addWidget(self.frame_4, 0, Qt.AlignLeft | Qt.AlignTop)

        self.horizontalLayout.addWidget(self.sideMenu)

        self.mainBody = QFrame(self.frame_2)
        self.mainBody.setObjectName("mainBody")
        self.mainBody.setFrameShape(QFrame.StyledPanel)
        self.mainBody.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.mainBody)

        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.menuButton.setText(QCoreApplication.translate("MainWindow", "MENU", None))
        self.label.setText(QCoreApplication.translate("MainWindow", "APP", None))
        self.pushButton_2.setText(
            QCoreApplication.translate("MainWindow", "Item 1", None)
        )
        self.pushButton_4.setText(
            QCoreApplication.translate("MainWindow", "Item 2", None)
        )
        self.pushButton_5.setText(
            QCoreApplication.translate("MainWindow", "Item 3", None)
        )
        self.pushButton_3.setText(
            QCoreApplication.translate("MainWindow", "Item 4", None)
        )

    # retranslateUi
