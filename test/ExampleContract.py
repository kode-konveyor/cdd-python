from unittest.mock import ANY, MagicMock
from ExampleChecker import ExampleChecker
from ExampleService import ExampleService
from Shall import Shall


class ExampleContract:
    rules = [
        (Shall("A contrived example of a service", ExampleService.run,)
         .when()
            .ifCalledWith(ANY, 2)
            .thenReturn(4)
            .suchThat(
                "The return value is twice the input",
                lambda returnValue, self, value: returnValue == 2 * value)
         # mypy does not think that "ExampleChecker" is a SideEffectChecker[[ExampleService, int], int]
         .meanWhile("Prints the result", ExampleChecker()) #type:ignore

         )
    ]
