from typing import Callable
from typing_extensions import Self, Concatenate

from shall.ShallEntity import ShallEntity, P, R

class SuchThat(ShallEntity[P, R]):
    def suchThat(self, explanation: str, checker: Callable[Concatenate[R, P], bool]) -> Self:
        self.returnConstraints.append((explanation, checker))
        return self
