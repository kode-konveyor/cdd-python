
from typing import Callable, Concatenate, Generic, ParamSpec, Self, TypeVar

from shall.SideEffectChecker import SideEffectChecker
from shall.ShallEntity import ShallEntity
from shall.When import When
from shall.IfCalledWith import IfCalledWith
from shall.ThenReturn import ThenReturn
from shall.SuchThat import SuchThat
from shall.MeanWhile import MeanWhile
from shall.Check import Check
from shall.ShallConstructor import ShallConstructor

P = ParamSpec("P")
R = TypeVar("R")


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
