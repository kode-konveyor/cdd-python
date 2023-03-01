from src.shall.ShallEntity import ShallEntity, P, R


class CheckSideEffects(ShallEntity[P, R]):
    def checkSideEffects(self, paramlist:P.args, paramkwargs: P.kwargs) ->None: #type:ignore #https://github.com/python/mypy/issues/14622
        for (explanation, sideEffectChecker) in self.sideEffectCheckers:
            sideEffectChecker.setUp(self.callable, *paramlist, **paramkwargs)
            result = sideEffectChecker.runTest()
            sideEffectChecker.tearDown()
            if result:
                print("-"+explanation+": PASSED")
            else:
                raise AssertionError(
                    explanation+" did not hold: " + str(result))
