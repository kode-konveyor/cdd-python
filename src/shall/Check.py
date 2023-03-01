
from shall.ShallEntity import ShallEntity, P, R
from injector import inject
from src.shall.CheckReturnConstraints import CheckReturnConstraints
from src.shall.CheckReturnValue import CheckReturnValue
from src.shall.CheckSideEffects import CheckSideEffects

class Check():
    @inject
    def __init__(self,
                 checkReturnValue:CheckReturnValue[P,R],
                 checkReturnConstraints: CheckReturnConstraints[P,R],
                 checkSideEffects: CheckSideEffects[P,R]
                 ) -> None:
        self.checkReturnValue = checkReturnValue
        self.checkReturnConstraints = checkReturnConstraints
        self.checkSideEffects = checkSideEffects

    def check(self) -> None:
        paramlist = self.parameters[0]
        paramkwargs = self.parameters[1]
        print(self.explanation)
        callResult = self.callable(*paramlist, **paramkwargs)
        self.checkReturnValue.checkReturnValue(callResult)
        self.checkReturnConstraints.checkReturnConstraints( paramlist, paramkwargs)
        self.checkSideEffects.checkSideEffects(paramlist,paramkwargs)
