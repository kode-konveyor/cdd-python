from typing import Any, Callable, List, Self, Unpack
from unittest.mock import MagicMock
from Shall import Shall
from shall.IfCalledWith import IfCalledWith
from shall.ShallEntity import ShallEntity, P, R


def checker(returnValue:Any, self:ShallEntity[P,R], otherparam: int, foo: str) -> bool:
    print("---")
    print(self.parameters)
    expected = ((1,), {'foo': 'bar'})
    print(expected)
    return self.parameters == expected

class IfCalledWithContract:
    mockSelf:IfCalledWith[[int, str], None] = MagicMock()
    rules = [(
        Shall("defines the parameters with which the SUT is called",
              IfCalledWith[[int,str], None].ifCalledWith) #type:ignore
        .ifCalledWith(mockSelf,1,foo="bar") #type:ignore
        .thenReturn(mockSelf) #type:ignore
        .suchThat("registers the return value", checker) #type:ignore
    )]

