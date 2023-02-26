from Shall import Shall
from shall.When import When
from unittest.mock import MagicMock


class WhenContract:
    foo = MagicMock()
    rules = [(

        Shall("When describes global states",
              When.when)
        .ifCalledWith(foo)
        .thenReturn(foo)

    )]
