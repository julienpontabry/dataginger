"""
Utility class to handle message boxes.
"""

from PySide2.QtCore import QObject
from PySide2.QtWidgets import QMessageBox


def closed_question(parent: QObject, title: str, message: str) -> bool:
    """
    Show a dialog box with a closed question (yes or no as possible answers).

    Parameters
    ----------
    parent: Parent object.
    title: Title of the dialog box.
    message: Message to show (it should be a question mark).

    Returns
    -------
        True if Yes was answered, False otherwise
    """
    return QMessageBox.question(parent, title, message) == QMessageBox.StandardButton.Yes
