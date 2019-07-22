"""
This module contains everything related to the GUI.
"""

import sys

from PySide2.QtGui import QKeySequence
from PySide2.QtWidgets import QMainWindow, QMenuBar, QStatusBar

from gui.action_utility import ActionFactory
from gui.data_table import DataTableViewer
from gui.message_box import closed_question


class DataGingerWindow(QMainWindow):
    """
    Main frame of the Data Ginger application.
    """

    def __init__(self, *args, **kwargs):
        """
        Create an instance of the main application's frame.

        Parameters
        ----------
        args: Arguments of QMainWindow object.
        kwargs: Dictionary of arguments for QMainWindow object.
        """
        super(DataGingerWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Data Ginger")
        self.setMenuBar(self.build_menu())
        self.status = self.build_status_bar()
        self.setCentralWidget(DataTableViewer(self))

    def build_menu(self) -> QMenuBar:
        """
        Build the top menu.

        Returns
        -------
            The top menu.
        """
        menu = self.menuBar()

        file_menu = menu.addMenu(self.tr("File"))
        file_menu.addAction(ActionFactory(self.tr("Quit"), self, self.quit).with_shortcut(QKeySequence.Quit).create())

        help_menu = menu.addMenu(self.tr("Help"))
        help_menu.addAction(ActionFactory(self.tr("About"), self, self.about).create())

        return menu

    def build_status_bar(self) -> QStatusBar:
        """
        Build and initialize the status bar.

        Returns
        -------
            The status bar.
        """
        status = self.statusBar()
        status.showMessage(self.tr("Initialized."))

        return status

    def quit(self):
        """
        Exit the application.
        """
        if closed_question(self, self.windowTitle(), "Do you really want to leave the application?"):
            sys.exit()

    @staticmethod
    def about():
        """
        Show "about" dialog.
        """
        # TODO make the about dialog
        print("about")
