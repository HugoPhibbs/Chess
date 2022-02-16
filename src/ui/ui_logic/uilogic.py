from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.ui.ui_shell.uishell import UIShell

class UILogic(ABC):
    """
    Represents a class to control a ui shell object

    Takes input from a UIShell Object and passes it onto the game logic
    """
    __shell: 'UIShell' = None

    def __init__(self):
        pass

    @abstractmethod
    def create_shell(self):
        """
        Creates the specific shell for this ui logic object

        :return: None
        """
        pass

    @property
    def shell(self) -> 'UIShell':
        return self.__shell

    @shell.setter
    def shell(self, shell) -> None:
        self.__shell = shell
