from typing import TypeVar, ParamSpec, Self

from shall.ShallEntity import ShallEntity

P = ParamSpec("P")
R = TypeVar("R")


class ThenReturn(ShallEntity[P, R]):
    def thenReturn(self, returnValue: R) -> Self:
        self.returnValue = returnValue
        return self
