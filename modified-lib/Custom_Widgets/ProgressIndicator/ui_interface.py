# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacesWaDqd.ui'
##
## Created by: Qt User Interface Compiler version 5.15.7
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from Custom_Widgets.Widgets import FormProgressIndicator


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 311)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet(
            "#centralwidget{background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(9, 27, 27, 255), stop:1 rgba(15, 24, 40, 255));}\n"
            "QPushButton{\n"
            "background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(9, 27, 27, 255), stop:1 rgba(15, 24, 40, 255));\n"
            "padding: 5px;\n"
            "border-radius: 5px;\n"
            "border: 2px solid rgb(32, 50, 84)\n"
            "}"
        )
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignTop)

        self.widget_3 = FormProgressIndicator(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.widget_3)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName("label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.height = QLabel(self.frame_3)
        self.height.setObjectName("height")
        font = QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(QFont.Weight(75))
        self.height.setFont(font)

        self.horizontalLayout_3.addWidget(self.height)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName("label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.steps = QLabel(self.frame_3)
        self.steps.setObjectName("steps")
        self.steps.setFont(font)

        self.horizontalLayout_3.addWidget(self.steps)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName("label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.theme = QLabel(self.frame_3)
        self.theme.setObjectName("theme")
        self.theme.setFont(font)

        self.horizontalLayout_3.addWidget(self.theme)

        self.verticalLayout.addWidget(self.frame_3)

        self.widget_2 = FormProgressIndicator(self.centralwidget)
        self.widget_2.setObjectName("widget_2")

        self.verticalLayout.addWidget(self.widget_2)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.step_6 = QPushButton(self.frame_2)
        self.step_6.setObjectName("step_6")

        self.horizontalLayout_2.addWidget(self.step_6)

        self.step_7 = QPushButton(self.frame_2)
        self.step_7.setObjectName("step_7")

        self.horizontalLayout_2.addWidget(self.step_7)

        self.step_8 = QPushButton(self.frame_2)
        self.step_8.setObjectName("step_8")

        self.horizontalLayout_2.addWidget(self.step_8)

        self.step_9 = QPushButton(self.frame_2)
        self.step_9.setObjectName("step_9")

        self.horizontalLayout_2.addWidget(self.step_9)

        self.step_10 = QPushButton(self.frame_2)
        self.step_10.setObjectName("step_10")

        self.horizontalLayout_2.addWidget(self.step_10)

        self.verticalLayout.addWidget(self.frame_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.widget = FormProgressIndicator(self.centralwidget)
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet("")

        self.verticalLayout.addWidget(self.widget)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName("frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.step_1 = QPushButton(self.frame)
        self.step_1.setObjectName("step_1")

        self.horizontalLayout.addWidget(self.step_1)

        self.step_2 = QPushButton(self.frame)
        self.step_2.setObjectName("step_2")

        self.horizontalLayout.addWidget(self.step_2)

        self.step_3 = QPushButton(self.frame)
        self.step_3.setObjectName("step_3")

        self.horizontalLayout.addWidget(self.step_3)

        self.step_4 = QPushButton(self.frame)
        self.step_4.setObjectName("step_4")

        self.horizontalLayout.addWidget(self.step_4)

        self.step_5 = QPushButton(self.frame)
        self.step_5.setObjectName("step_5")

        self.horizontalLayout.addWidget(self.step_5)

        self.verticalLayout.addWidget(self.frame)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.label.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:22pt; font-weight:600; color:#55ffff;">F</span><span style=" font-size:18pt; font-weight:600;">orm </span><span style=" font-size:22pt; font-weight:600; color:#55ffff;">P</span><span style=" font-size:18pt; font-weight:600;">rogress </span><span style=" font-size:22pt; font-weight:600; color:#55ffff;">I</span><span style=" font-size:18pt; font-weight:600;">ndicator</span></p></body></html>',
                None,
            )
        )
        self.label_2.setText(
            QCoreApplication.translate("MainWindow", "Simulating Download Task", None)
        )
        self.label_5.setText(QCoreApplication.translate("MainWindow", "Height", None))
        self.height.setText(QCoreApplication.translate("MainWindow", "NA", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", "Steps", None))
        self.steps.setText(QCoreApplication.translate("MainWindow", "NA", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", "Theme", None))
        self.theme.setText(QCoreApplication.translate("MainWindow", "NA", None))
        self.step_6.setText(QCoreApplication.translate("MainWindow", "20%", None))
        self.step_7.setText(QCoreApplication.translate("MainWindow", "40%", None))
        self.step_8.setText(QCoreApplication.translate("MainWindow", "60%", None))
        self.step_9.setText(QCoreApplication.translate("MainWindow", "80%", None))
        self.step_10.setText(QCoreApplication.translate("MainWindow", "100%", None))
        self.label_3.setText(
            QCoreApplication.translate(
                "MainWindow", "Simulating Navigation Through A Form With 10 Steps", None
            )
        )
        self.step_1.setText(QCoreApplication.translate("MainWindow", "Step 1", None))
        self.step_2.setText(QCoreApplication.translate("MainWindow", "Step 2", None))
        self.step_3.setText(QCoreApplication.translate("MainWindow", "Step 3", None))
        self.step_4.setText(QCoreApplication.translate("MainWindow", "Step 4", None))
        self.step_5.setText(QCoreApplication.translate("MainWindow", "Step 5", None))
        self.label_4.setText(
            QCoreApplication.translate(
                "MainWindow", "Simulating Navgation Through A Form With 5 Steps", None
            )
        )

    # retranslateUi
