from typing import TypeVar, ParamSpec, Self

from shall.ShallEntity import ShallEntity, P, R

class When(ShallEntity[P, R]):
    def when(self) -> Self:
        return self
