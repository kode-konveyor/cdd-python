from typing import Any
from unittest.mock import MagicMock
from Shall import Shall
from shall.IfCalledWith import IfCalledWith
from shall.ShallEntity import ShallEntity, P, R

def checker(returnValue:IfCalledWith[[int, str], None], self:IfCalledWith[[int, str], None], otherparam: int, foo: str) -> bool:
    expected = ((1,), {'foo': 'bar'})
    return self.parameters == expected

class IfCalledWithContract:
    mockSelf:IfCalledWith[[int, str], None] = MagicMock()
    rules = [(
        Shall[IfCalledWith[[int,str], None],IfCalledWith[[int,str], None]](
            "defines the parameters with which the SUT is called",
            IfCalledWith[[int,str], None].ifCalledWith) #type: ignore #https://github.com/python/mypy/issues/14806
        .ifCalledWith(mockSelf,1,foo="bar") #type:ignore # https://github.com/python/mypy/issues/14806
        .thenReturn(mockSelf) 
        .suchThat("registers the return value", checker)  #type: ignore # https://github.com/python/mypy/issues/14806
    )]

