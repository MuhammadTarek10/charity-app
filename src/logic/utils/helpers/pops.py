from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QIcon

from src.logic.config.strings import Strings
from src.logic.config.config import Config


class Pops:
    def __init__(self) -> None:
        self.box = QMessageBox()
        self.box.setWindowIcon(QIcon(Config.LOGO))

    def error(self, key: str) -> None:
        self.box.setIcon(QMessageBox.Critical)
        self.box.setWindowTitle(Strings.ERROR_TITLE)
        self.box.setText(Strings.messages[key])
        self.box.setStandardButtons(QMessageBox.Ok)
        self.box.exec()

    def info(self, key: str) -> None:
        self.box.setIcon(QMessageBox.Information)
        self.box.setWindowTitle(Strings.INFORMATION_TITLE)
        self.box.setText(Strings.messages[key])
        self.box.setStandardButtons(QMessageBox.Ok)
        self.box.exec()

    def confirm(self, key: str) -> bool:
        self.box.setIcon(QMessageBox.Question)
        self.box.setWindowTitle(Strings.CONFIRM_TITLE)
        self.box.setText(Strings.messages[key])
        self.box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        return True if self.box.exec() == QMessageBox.Ok else False
