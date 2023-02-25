
from typing import Callable, Concatenate, Generic, ParamSpec, Self, TypeVar

from SideEffectChecker import SideEffectChecker

P = ParamSpec("P")
R = TypeVar("R")


class Shall(Generic[P, R]):

    def __init__(self, explanation: str, callable: Callable[P, R]) -> None:
        self.callable = callable
        self.explanation = explanation
        self.returnConstraints: list[tuple[str, Callable[Concatenate[R, P], bool]]] = list(
        )
        self.sideEffectCheckers: list[tuple[str,
                                            SideEffectChecker[P, R]]] = list()

    def when(self) -> Self:
        return self

    def ifCalledWith(self, *args: P.args, **kwargs: P.kwargs) -> Self:
        self.parameters = (args, kwargs)
        return self

    def thenReturn(self, returnValue: R) -> "Shall[P,R]":
        self.returnValue = returnValue
        return self

    def suchThat(self, explanation: str, checker: Callable[Concatenate[R, P], bool]) -> Self:
        self.returnConstraints.append((explanation, checker))
        return self

    def meanWhile(self, explanation: str, checker: SideEffectChecker[P, R]) -> Self:
        self.sideEffectCheckers.append((explanation, checker))
        return self

    def check(self) -> None:
        paramlist = self.parameters[0]
        paramkwargs = self.parameters[1]
        for (explanation, checker) in self.returnConstraints:
            checked = checker(self.returnValue, *paramlist, **paramkwargs)
            if checked:
                print(explanation+": PASSED")
            else:
                raise AssertionError(explanation+" did not hold")
        for (explanation, sideEffectChecker) in self.sideEffectCheckers:
            sideEffectChecker.setUp(self.callable, *paramlist, **paramkwargs)
            result = sideEffectChecker.runTest()
            sideEffectChecker.tearDown()
            if result:
                print(explanation+": PASSED")
            else:
                raise AssertionError(
                    explanation+" did not hold: " + str(result))
