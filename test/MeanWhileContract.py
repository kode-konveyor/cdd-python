from typing import Any, Callable
from unittest.mock import Mock
from ExampleService import ExampleService
from Shall import Shall
from shall.MeanWhile import MeanWhile

from ExampleChecker import ExampleChecker
from shall.ShallEntity import ShallEntity
from shall.SideEffectChecker import SideEffectChecker

def checker(returned: ShallEntity[[int], int], self:ShallEntity[[int], int], explanation: str, checker: SideEffectChecker[[ExampleService, int], int]) -> bool: 
    return self.sideEffectCheckers == [(explanation, checker)]

class MeanWhileContract:
    selfMock:ShallEntity[[int], int] = Mock()
    selfMock.sideEffectCheckers = []
    rules = [(
        Shall("Registers side effects", MeanWhile[[int],int].meanWhile) 
        .ifCalledWith(selfMock, "explanation", ExampleChecker) #type: ignore # https://github.com/python/mypy/issues/14785
        .thenReturn(selfMock)
        .suchThat("registers the side effect checker", checker) #type: ignore # 
    )]

#"Callable[[ShallEntity[[int], int], ShallEntity[[int], int], str, SideEffectChecker[[ExampleService, int], int]], bool]"; expected 
#"Callable[[ShallEntity[[int], int], ShallEntity[[int], int], str, SideEffectChecker[[ShallEntity[[int], int], str, SideEffectChecker[[ShallEntity[[int], int], str, SideEffectChecker[[ShallEntity[[int], int], str, SideEffectChecker[P, R]], R]], R]], R]], bool]"