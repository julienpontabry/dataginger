"""
This module contains everything related to the GUI.
"""

import sys

from PySide2.QtWidgets import QMainWindow, QAction, QWidget, QMenuBar, QStatusBar, QTableWidget, QTableWidgetItem


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
        self.setCentralWidget(self.build_main_component())

    def build_menu(self) -> QMenuBar:
        """
        Build the top menu.

        Returns
        -------
            The top menu.
        """
        menu = self.menuBar()
        file_menu = menu.addMenu(self.tr("File"))
        help_menu = menu.addMenu(self.tr("Help"))

        quit_action = QAction(self.tr("Quit"), self)
        quit_action.setShortcut("Ctrl+Q")
        quit_action.triggered.connect(self.quit)
        quit_action.setMenuRole(QAction.NoRole)
        file_menu.addAction(quit_action)

        about_action = QAction(self.tr("About"), self)
        about_action.triggered.connect(self.about)
        about_action.setMenuRole(QAction.NoRole)
        help_menu.addAction(about_action)

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

    def build_main_component(self) -> QWidget:
        """
        Build the main frame's component.

        Returns
        -------
            The main component.
        """
        # widget = QWidget()
        # layout = QVBoxLayout()
        # widget.setLayout(layout)
        # layout.addWidget(QLabel(self.tr("Coucou !")))
        # button = QPushButton(self.tr("Prout"))
        # button.clicked.connect(self.test)
        # layout.addWidget(button)

        widget = QTableWidget(5, 2, self)
        widget.setHorizontalHeaderItem(1, QTableWidgetItem("Prout"))
        widget.setVerticalHeaderItem(2, QTableWidgetItem("Prout v"))
        widget.setItem(2, 1, QTableWidgetItem("Test"))

        return widget

    @staticmethod
    def quit():
        """
        Exit the application.
        """
        sys.exit()

    @staticmethod
    def about():
        """
        Show "about" dialog.
        """
        # TODO make the about dialog
        print("about")
