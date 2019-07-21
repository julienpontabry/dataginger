"""
Utility module for GUI actions.
"""

from typing import Callable

from PySide2.QtCore import QObject
from PySide2.QtGui import QKeySequence
from PySide2.QtWidgets import QAction


class ActionFactory:
    """
    Factory class for actions.
    """
    def __init__(self, name: str, parent: QObject, callback: Callable):
        """
        Create an action factory instance with given basic properties.

        Parameters
        ----------
        name: Name of the action.
        parent: Parent object of the action.
        callback: Callback of the action when used.
        """
        self.action = QAction(name, parent)
        self.action.triggered.connect(callback)

    def create(self) -> QAction:
        """
        Create the action.

        Returns
        -------
            The action with all defined properties.
        """
        return self.action

    def with_shortcut(self, shortcut: QKeySequence):
        """
        Add a shortcut to the action.

        Parameters
        ----------
        shortcut: Shortcut to add to the action.

        Returns
        -------
            The current factory instance for fluent programming style;
        """
        self.action.setShortcut(shortcut)
        return self
