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

    def number_of_opened_tables(self):
        """
        Get the number of currently opened tables.

        Returns
        -------
            The number of opened tables.
        """
        return len(self.subWindowList())

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

        header = table.horizontalHeader()
        header.setSectionsMovable(True)
        header.sectionMoved.connect(lambda _, i1, i2: self.column_rearranged(i1, i2))

        for j, column_name in enumerate(data.columns):
            table.setHorizontalHeaderItem(j, QTableWidgetItem(column_name))

        for (i, row), index in zip(enumerate(data.values), data.index.values):
            table.setVerticalHeaderItem(i, QTableWidgetItem(str(index)))

            for j, element in enumerate(row):
                table.setItem(i, j, QTableWidgetItem(str(element)))

        tab = self.addSubWindow(table)
        tab.data = data
        tab.setWindowTitle(file_path)
        tab.showMaximized()

    def close_current_table(self):
        """
        Close the currently selected table and free memory.
        """
        selected_tab = self.activeSubWindow()
        del selected_tab.data
        selected_tab.close()

    def column_rearranged(self, old_index: int, new_index: int):
        """
        Rearrange columns order in active table.

        Parameters
        ----------
        old_index: Old index of the column being moved.
        new_index: New index of the column being moved.
        """
        data = self.activeSubWindow().data
        columns = list(data.columns)
        columns.insert(new_index, columns.pop(old_index))
        self.activeSubWindow().data = data.loc[:, columns]
