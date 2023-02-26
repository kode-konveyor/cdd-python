from typing import TypeVar, ParamSpec, Self

from shall.ShallEntity import ShallEntity

P = ParamSpec("P")
R = TypeVar("R")


class Check(ShallEntity[P, R]):
    def check(self) -> None:
        paramlist = self.parameters[0]
        paramkwargs = self.parameters[1]
        print(self.explanation)
        callResult = self.callable(*paramlist, **paramkwargs)
        if self.returnValue == callResult:
            print("/return value PASSED")
        else:
            raise AssertionError(self.explanation +
                                 " did return " + str(callResult) + " instead of " + str(self.returnValue))
        for (explanation, checker) in self.returnConstraints:
            checked = checker(self.returnValue, *paramlist, **paramkwargs)
            if checked:
                print("+"+explanation+": PASSED")
            else:
                raise AssertionError(explanation+" did not hold")
        for (explanation, sideEffectChecker) in self.sideEffectCheckers:
            sideEffectChecker.setUp(self.callable, *paramlist, **paramkwargs)
            result = sideEffectChecker.runTest()
            sideEffectChecker.tearDown()
            if result:
                print("-"+explanation+": PASSED")
            else:
                raise AssertionError(
                    explanation+" did not hold: " + str(result))
