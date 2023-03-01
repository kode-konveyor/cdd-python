from src.shall.ShallEntity import ShallEntity, P, R


class CheckReturnConstraints(ShallEntity[P, R]):
    def checkReturnConstraints(self, paramlist:P.args, paramkwargs: P.kwargs) -> None: #type:ignore # https://github.com/python/mypy/issues/14622
        for (explanation, checker) in self.returnConstraints:
            checked = checker(self.returnValue, *paramlist, **paramkwargs)
            if checked:
                print("+"+explanation+": PASSED")
            else:
                raise AssertionError(explanation+" did not hold")
