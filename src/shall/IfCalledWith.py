from typing_extensions import Self

from shall.ShallEntity import ShallEntity, P, R


class IfCalledWith(ShallEntity[P, R]):
    def ifCalledWith(self, *args: P.args, **kwargs: P.kwargs) -> Self:
        self.parameters = (args, kwargs)
        return self
