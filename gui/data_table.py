"""
Class for handling of data tables
"""

from PySide2.QtWidgets import QMdiArea, QPushButton, QVBoxLayout, QLabel, QWidget, QTableWidget, QTableWidgetItem


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

        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)
        layout.addWidget(QLabel(self.tr("Coucou !")))
        button = QPushButton(self.tr("Prout"))
        layout.addWidget(button)

        widget2 = QTableWidget(5, 2, self)
        widget2.setHorizontalHeaderItem(1, QTableWidgetItem("Prout"))
        widget2.setVerticalHeaderItem(2, QTableWidgetItem("Prout v"))
        widget2.setItem(2, 1, QTableWidgetItem("Test"))

        w1 = self.addSubWindow(widget)
        w1.setWindowTitle("Document 1")
        w2 = self.addSubWindow(widget2)
        w2.setWindowTitle("Document 2")
