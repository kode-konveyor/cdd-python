from typing import Callable, cast
from unittest.mock import Mock
from Shall import Shall
from shall.Check import Check
from shall.ShallConstructor import ShallConstructor

def check(returnValue: None, self: Check[[int],str] ) -> bool:
    mock = cast(Mock,self.callable)
    mock.assert_called_once()
    return True

class CheckContract:
    callableMock:Callable[[int], str] = Mock()
    cast(Mock,callableMock).return_value="2"
    selfMock= Mock()
    selfMock.callable = callableMock
    selfMock.parameters = ((2,),{})
    selfMock.returnValue = "2"
    selfMock.explanation = "explanation"
    selfMock.returnConstraints = list()
    selfMock.sideEffectCheckers = list()

    rules = [(
        Shall[[Check[[int],str]],None]("checks the contract", Check[[int],str].check) #type:ignore #https://github.com/python/mypy/issues/14806
        .ifCalledWith(selfMock)
        .thenReturn(None)
        .suchThat("the callable is called", check)
    )]

