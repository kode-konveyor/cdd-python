from unittest.mock import MagicMock
from Shall import Shall
from shall.ShallConstructor import ShallConstructor

def callable(self:int) ->int:
    return self

class ShallConstructorContract:
    mockSelf = MagicMock()
    explanation = "explanation"
    rules = [(
        Shall("initializes the contract runner", ShallConstructor.init)
        .ifCalledWith(mockSelf, explanation, callable)
        .thenReturn(None)
        .suchThat("registers the callable", lambda returned, self, explanation, callable: self.callable == callable)
        .suchThat("registers the explanation", lambda returned, self, explanation, callable: self.explanation == explanation)
        .suchThat("creates an empty list of return constraints", lambda returned, self, explanation, callable: self.returnConstraints == list())
        .suchThat("creates an empty list of side effect checks", lambda returned, self, explanation, callable: self.sideEffectCheckers == list())
    )]
