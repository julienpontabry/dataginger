"""
Class for handling of data tables
"""

import pandas as pd
from PySide2.QtWidgets import QMdiArea, QTableWidget, QTableWidgetItem


class DataTableViewer(QMdiArea):
    """
    Class that handle views of data tables.
    """

    def __init__(self, *args, **kwargs):
        """
        Create an instance of a data table viewer.

        Parameters
        ----------
        args: Arguments of QMdiArea object.
        kwargs: Dictionary of arguments for QMdiArea object.
        """
        super(DataTableViewer, self).__init__(*args, **kwargs)

        self.setViewMode(QMdiArea.TabbedView)

    def open_table(self, file_path: str):
        """
        Open table from file at given path.

        Parameters
        ----------
        file_path: Path to the file to open.
        """
        data = pd.read_csv(file_path)
        n_rows, n_cols = data.shape
        table = QTableWidget(n_rows, n_cols, self)

        for j, column_name in enumerate(data.columns):
            table.setHorizontalHeaderItem(j, QTableWidgetItem(column_name))

        for (i, row), index in zip(enumerate(data.values), data.index.values):
            table.setVerticalHeaderItem(i, QTableWidgetItem(str(index)))

            for j, element in enumerate(row):
                table.setItem(i, j, QTableWidgetItem(str(element)))

        tab = self.addSubWindow(table)
        tab.setWindowTitle(file_path)
        tab.showMaximized()
