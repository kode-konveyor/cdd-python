from typing import Callable
from unittest.mock import Mock
from Shall import Shall
from shall.ThenReturn import ThenReturn


class ThenreturnContract:
    mockSelf:ThenReturn[[int],str] = Mock()
    rules = [(
        Shall("Registers the return value", ThenReturn[[int],str].thenReturn)
        .ifCalledWith(mockSelf,"42")
        .thenReturn(mockSelf)
        .suchThat("the return value is registered", lambda returnValue, self, givenValue: self.returnValue == givenValue)
    )]