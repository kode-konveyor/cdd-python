
from typing_extensions import Self

from shall.ShallEntity import ShallEntity, P, R

class ThenReturn(ShallEntity[P, R]):
    def thenReturn(self, returnValue: R) -> Self:
        self.returnValue = returnValue
        return self
