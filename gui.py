"""
This module contains everything related to the GUI.
"""

import sys

from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QAction, QWidget, QPushButton


class DataGingerWindow(QMainWindow):
    """
    Main frame of the Data Ginger application.
    """

    def __init__(self, *args, **kwargs):
        super(DataGingerWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Data Ginger")

        # menu
        self.menu = self.menuBar()
        self.setMenuBar(self.menu)
        self.file_menu = self.menu.addMenu(self.tr("File"))
        self.help_menu = self.menu.addMenu(self.tr("Help"))

        quit_action = QAction(self.tr("Quit"), self)
        quit_action.setShortcut("Ctrl+Q")
        quit_action.triggered.connect(self.quit)
        quit_action.setMenuRole(QAction.NoRole)
        self.file_menu.addAction(quit_action)

        about_action = QAction(self.tr("About"), self)
        about_action.triggered.connect(self.about)
        about_action.setMenuRole(QAction.NoRole)
        self.help_menu.addAction(about_action)

        # status bar
        self.status = self.statusBar()
        self.status.showMessage(self.tr("Done."))

        # add center
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)
        layout.addWidget(QLabel(self.tr("Coucou !")))
        button = QPushButton(self.tr("Prout"))
        button.clicked.connect(self.test)
        layout.addWidget(button)
        self.setCentralWidget(widget)

    @staticmethod
    def quit():
        sys.exit()

    @staticmethod
    def about():
        print("about")

    def test(self):
        print(self.tr("Et voilà !"))
