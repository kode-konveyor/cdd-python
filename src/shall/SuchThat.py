from typing import TypeVar, ParamSpec, Self, Callable, Concatenate

from shall.ShallEntity import ShallEntity, P, R

class SuchThat(ShallEntity[P, R]):
    def suchThat(self, explanation: str, checker: Callable[Concatenate[R, P], bool]) -> Self:
        self.returnConstraints.append((explanation, checker))
        return self
