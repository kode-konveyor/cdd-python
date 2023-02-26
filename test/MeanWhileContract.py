from typing import Any, Callable
from unittest.mock import Mock
from ExampleService import ExampleService
from Shall import Shall
from shall.MeanWhile import MeanWhile

from ExampleChecker import ExampleChecker
from shall.ShallEntity import ShallEntity
from shall.SideEffectChecker import SideEffectChecker

# crashes mypy
#def checker(returned: int, self:ShallEntity[[int], int], explanation: str, checker: SideEffectChecker[[ExampleService, int], int]) -> bool: 
#    return self.sideEffectCheckers == [(explanation, checker)]

def checker(returned: int, self:Any, explanation: str, checker: Any) -> bool: 
    return self.sideEffectCheckers == [(explanation, checker)] #type:ignore


class MeanWhileContract:
    selfMock:ShallEntity[[int], int] = Mock()
    selfMock.sideEffectCheckers = []
    rules = [(
        Shall("Registers side effects", MeanWhile[[int],int].meanWhile) #type:ignore
        .ifCalledWith(selfMock, "explanation", ExampleChecker) #type:ignore
        .thenReturn(selfMock)
        .suchThat("registers the side efect checker", checker) #type:ignore
    )]
