from typing import Callable, Generic, TypeVar
from typing_extensions import ParamSpec

P = ParamSpec("P")
R = TypeVar("R")

class SideEffectChecker(Generic[P, R]):

    def setUp(self, service: Callable[P, R], *
              args: P.args, **kwargs: P.kwargs) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def runTest(self) -> bool:
        return False
