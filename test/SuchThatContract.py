from unittest.mock import Mock
from Shall import Shall
from shall.SuchThat import SuchThat


class SuchThatContract:
    selfMock = Mock()
    rules = [(
        Shall("Registers side effects", SuchThat.suchThat)
        .ifCalledWith(selfMock, "explanation", lambda returnValue, self, explanation, checker: True)
        .thenReturn(selfMock)
    )]
