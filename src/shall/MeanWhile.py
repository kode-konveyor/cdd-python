from typing import TypeVar, ParamSpec, Self

from shall.ShallEntity import ShallEntity, P, R
from shall.SideEffectChecker import SideEffectChecker


class MeanWhile(ShallEntity[P, R]):
    def meanWhile(self, explanation: str, checker: SideEffectChecker[P, R]) -> Self:
        self.sideEffectCheckers.append((explanation, checker))
        return self
