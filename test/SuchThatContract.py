from typing import Callable
from unittest.mock import Mock
from Shall import Shall
from shall.SuchThat import SuchThat

def checkerTestArtifact(returnValue:str, parameter:int) -> bool:
    return True

def realChecker(returnValue:str, self:SuchThat[[int],int], explanation: str, checker: Callable[[int,  int ], bool]) -> bool:
    return self.returnConstraints== [("explanation",checker )]


class SuchThatContract:
    selfMock:SuchThat[[int],str] = Mock()
    selfMock.returnConstraints = []
    rules = [(
        Shall("Registers side effects", SuchThat[[int],str].suchThat)
        .ifCalledWith(selfMock, "explanation", checkerTestArtifact) #type:ignore #https://github.com/python/mypy/issues/14806
        .thenReturn(selfMock)
        .suchThat("Registers the side effect check and explanation", realChecker) #type:ignore #https://github.com/python/mypy/issues/14806
    )]
