"""
Contains the main entry point to the application.
"""
import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QStyle

from gui import DataGingerWindow

if __name__ == "__main__":
    APP = QApplication(sys.argv)
    GEOMETRY = APP.desktop().availableGeometry()

    MAIN_WINDOW = DataGingerWindow()
    MAIN_WINDOW.show()
    MAIN_WINDOW.setGeometry(QStyle.alignedRect(
        Qt.LeftToRight, Qt.AlignCenter, GEOMETRY.size() * 0.75, GEOMETRY))

    sys.exit(APP.exec_())
