from typing import Callable,  Generic, TypeVar
from typing_extensions import ParamSpec, Concatenate

from shall.SideEffectChecker import SideEffectChecker

P = ParamSpec("P")
R = TypeVar("R")

class ShallEntity(Generic[P, R]):
    callable: Callable[P, R]
    returnConstraints: list[tuple[str, Callable[Concatenate[R, P], bool]]]
    sideEffectCheckers: list[tuple[str, SideEffectChecker[P, R]]]
    parameters: tuple[P.args, P.kwargs] #type:ignore #https://github.com/python/mypy/issues/14622
    returnValue: R
    explanation: str
