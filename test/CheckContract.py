from unittest.mock import Mock
from Shall import Shall
from shall.Check import Check
from shall.ShallConstructor import ShallConstructor

def callable(a:int)-> str:
    return str(a)

class CheckContract:
    selfMock= Mock()
    selfMock.callable = callable
    selfMock.parameters = ((2,),{})
    selfMock.returnValue = "2"
    selfMock.explanation = "explanation"
    selfMock.returnConstraints = list()
    selfMock.sideEffectCheckers = list()

    rules = [(
        Shall("checks the contract", Check[[int],str].check)
        .ifCalledWith(selfMock)
        .thenReturn(None)
    )]