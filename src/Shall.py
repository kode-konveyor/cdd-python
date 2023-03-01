
from typing import Callable, Generic

from shall.ShallEntity import P, R
from shall.When import When
from shall.IfCalledWith import IfCalledWith
from shall.ThenReturn import ThenReturn
from shall.SuchThat import SuchThat
from shall.MeanWhile import MeanWhile
from shall.Check import Check
from shall.ShallConstructor import ShallConstructor


class Shall(
        Generic[P, R],
        When[P, R],
        IfCalledWith[P, R],
        ThenReturn[P, R],
        SuchThat[P, R],
        MeanWhile[P, R],
        Check[P, R],
        ShallConstructor[P, R]):

    def __init__(self, explanation: str, callable: Callable[P, R]) -> None:
        self.init(explanation, callable)
