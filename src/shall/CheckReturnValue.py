from src.shall.ShallEntity import ShallEntity, P, R


class CheckReturnValue(ShallEntity[P, R]):
    def checkReturnValue(self, callResult: R) ->None:
        if self.returnValue == callResult:
            print("/return value PASSED")
        else:
            raise AssertionError(self.explanation +
                                 " did return " + str(callResult) + " instead of " + str(self.returnValue))
