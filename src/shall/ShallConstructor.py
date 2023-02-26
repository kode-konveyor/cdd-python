from typing import TypeVar, ParamSpec, Self, Callable

from shall.ShallEntity import ShallEntity, P, R

class ShallConstructor(ShallEntity[P, R]):

    def init(self, explanation: str, callable: Callable[P, R]) -> None:
        self.callable = callable
        self.explanation = explanation
        self.returnConstraints = list()
        self.sideEffectCheckers = list()
